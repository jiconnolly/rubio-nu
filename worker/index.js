/* ============================================================
   Club Rubio Ñu — Worker del sitio

   Sirve dos cosas:
   · /api/*  → datos deportivos en vivo desde API-Football
   · el resto → los archivos estáticos del sitio

   La API key vive como secret en Cloudflare (API_FOOTBALL_KEY) y
   nunca llega al navegador: el sitio solo ve el JSON ya procesado.
   ============================================================ */

const BASE = 'https://v3.football.api-sports.io';
const TEMPORADA = 2026;
const CACHE_SEGUNDOS = 300;      // tabla y partidos
const CACHE_ESTRUCTURA = 86400;  // liga y equipo: no cambian en toda la temporada

/* El plan gratuito limita las consultas por minuto, así que cada respuesta
   de la API se guarda en la caché del borde y solo se vuelve a pedir cuando
   vence. Sin esto, dos recargas seguidas agotan el cupo. */
async function api(ruta, env, ttl = CACHE_SEGUNDOS) {
  const clave = new Request('https://cache.rubionu.local' + ruta, { method: 'GET' });
  const cache = caches.default;

  let respuesta = await cache.match(clave);
  if (!respuesta) {
    const r = await fetch(BASE + ruta, {
      headers: { 'x-apisports-key': env.API_FOOTBALL_KEY }
    });
    const cuerpo = await r.text();
    if (!r.ok) throw new Error(`API-Football ${r.status} en ${ruta}`);

    const j = JSON.parse(cuerpo);
    if (j.errors && Object.keys(j.errors).length) {
      throw new Error('API-Football: ' + JSON.stringify(j.errors));
    }
    respuesta = new Response(cuerpo, {
      headers: {
        'content-type': 'application/json',
        'cache-control': 'public, max-age=' + ttl
      }
    });
    await cache.put(clave, respuesta.clone());
  }
  return (await respuesta.json()).response;
}

/* Busca la primera división paraguaya sin depender de un ID fijo. */
async function resolverLiga(env) {
  const ligas = await api(`/leagues?country=Paraguay&season=${TEMPORADA}&type=League`, env, CACHE_ESTRUCTURA);
  const primera = ligas.find(l => /division profesional|primera/i.test(l.league.name)) || ligas[0];
  if (!primera) throw new Error('No se encontró la liga paraguaya');
  return primera.league.id;
}

async function resolverEquipo(env) {
  const liga = await resolverLiga(env);
  const equipos = await api(`/teams?league=${liga}&season=${TEMPORADA}`, env, CACHE_ESTRUCTURA);
  const nuestro = equipos.find(e => /rubio/i.test(e.team.name));
  if (!nuestro) throw new Error('No se encontró a Rubio Ñu en la liga');
  return nuestro.team.id;
}

function nombreTorneo(nombreLiga, ronda) {
  const clausura = /clausura/i.test(ronda || '');
  return clausura
    ? { es: 'Torneo Clausura ' + TEMPORADA, en: 'Clausura ' + TEMPORADA }
    : { es: nombreLiga + ' ' + TEMPORADA, en: nombreLiga + ' ' + TEMPORADA };
}

async function tabla(env) {
  const liga = await resolverLiga(env);
  const r = await api(`/standings?league=${liga}&season=${TEMPORADA}`, env);
  const info = r[0]?.league;
  const grupos = info?.standings || [];
  /* Con Apertura y Clausura, el grupo vigente es el último. */
  const grupo = grupos[grupos.length - 1] || [];

  return {
    torneo: nombreTorneo(info?.name || 'Clausura', grupo[0]?.group),
    fecha_jugada: Math.max(...grupo.map(e => e.all.played), 0),
    actualizado: new Date().toISOString().slice(0, 10),
    fuente: { es: 'APF', en: 'APF' },
    equipos: grupo.map(e => ({
      pos: e.rank,
      equipo: e.team.name.replace(/\bNU\b/, 'Ñu'),
      pj: e.all.played,
      g: e.all.win,
      e: e.all.draw,
      p: e.all.lose,
      gf: e.all.goals.for,
      gc: e.all.goals.against,
      dg: e.goalsDiff,
      pts: e.points,
      forma: (e.form || '').slice(-5).split('').map(c => ({ W: 'G', D: 'E', L: 'P' }[c] || 'E')),
      ...(/rubio/i.test(e.team.name) ? { esNosotros: true } : {})
    }))
  };
}

function mapearPartido(f) {
  const ronda = (f.league.round || '').match(/\d+/);
  return {
    fecha: f.fixture.date.slice(0, 10),
    hora: f.fixture.date.slice(11, 16),
    torneo: /clausura/i.test(f.league.round || '') ? 'Clausura' : f.league.name,
    ronda: ronda ? Number(ronda[0]) : null,
    local: f.teams.home.name.replace(/\bNU\b/, 'Ñu'),
    visitante: f.teams.away.name.replace(/\bNU\b/, 'Ñu'),
    estadio: f.fixture.venue?.name || '',
    condicion: /rubio/i.test(f.teams.home.name) ? 'local' : 'visitante'
  };
}

async function partidos(env) {
  const equipo = await resolverEquipo(env);
  const [jugados, porJugar] = await Promise.all([
    api(`/fixtures?team=${equipo}&season=${TEMPORADA}&last=1`, env),
    api(`/fixtures?team=${equipo}&season=${TEMPORADA}&next=3`, env)
  ]);
  const u = jugados[0];
  return {
    actualizado: new Date().toISOString().slice(0, 10),
    ultimo: u ? { ...mapearPartido(u), golesLocal: u.goals.home, golesVisitante: u.goals.away } : null,
    proximos: porJugar.map(mapearPartido)
  };
}

/* Diagnóstico: confirma que la key funciona y qué liga y equipo resolvió. */
async function diagnostico(env) {
  const liga = await resolverLiga(env);
  const equipo = await resolverEquipo(env);
  return { ok: true, liga_id: liga, equipo_id: equipo, temporada: TEMPORADA };
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname.startsWith('/api/')) {
      const json = (datos, estado = 200) => new Response(JSON.stringify(datos, null, 2), {
        status: estado,
        headers: {
          'content-type': 'application/json; charset=utf-8',
          'cache-control': 'public, max-age=' + CACHE_SEGUNDOS
        }
      });

      if (!env.API_FOOTBALL_KEY) {
        return json({ error: 'Falta el secret API_FOOTBALL_KEY' }, 503);
      }

      try {
        if (url.pathname === '/api/tabla')       return json(await tabla(env));
        if (url.pathname === '/api/partidos')    return json(await partidos(env));
        if (url.pathname === '/api/diagnostico') return json(await diagnostico(env));
        return json({ error: 'Ruta no encontrada' }, 404);
      } catch (err) {
        /* Ante cualquier fallo devolvemos 502: el sitio cae solo a los
           archivos estáticos de /data y sigue mostrando la última tabla. */
        return json({ error: String(err.message || err) }, 502);
      }
    }

    return env.ASSETS.fetch(request);
  }
};
