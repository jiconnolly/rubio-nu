/* ============================================================
   Worker de datos deportivos — Club Rubio Ñu
   ------------------------------------------------------------
   Todavía NO está en uso. Se activa cuando el sitio migre de
   GitHub Pages a Cloudflare Workers.

   Qué hace: llama a API-Football con la key guardada como secret
   (nunca viaja al navegador), cachea la respuesta y devuelve un
   JSON con la misma forma que los archivos de /data, así el
   frontend no cambia.

   Puesta en marcha:
     1. Crear cuenta gratuita en dashboard.api-football.com
     2. wrangler secret put API_FOOTBALL_KEY
     3. Confirmar LIGA_ID con: GET /leagues?country=Paraguay
     4. En assets/js/main.js poner ORIGEN_VIVO = '/api'
   ============================================================ */

const BASE = 'https://v3.football.api-sports.io';
const LIGA_ID = 250;        // División Profesional de Paraguay — verificar contra /leagues
const TEMPORADA = 2026;
const EQUIPO_NOMBRE = 'Rubio Ñu';
const CACHE_SEGUNDOS = 300;

async function apiFootball(ruta, env) {
  const r = await fetch(BASE + ruta, {
    headers: { 'x-apisports-key': env.API_FOOTBALL_KEY },
    cf: { cacheTtl: CACHE_SEGUNDOS, cacheEverything: true }
  });
  if (!r.ok) throw new Error('API-Football respondió ' + r.status);
  const j = await r.json();
  return j.response;
}

function normalizarTabla(respuesta) {
  const grupo = respuesta[0]?.league?.standings?.[0] || [];
  return {
    torneo: 'Torneo Clausura ' + TEMPORADA,
    fecha_jugada: grupo[0]?.all?.played || 0,
    actualizado: new Date().toISOString().slice(0, 10),
    fuente: 'APF',
    equipos: grupo.map(e => ({
      pos: e.rank,
      equipo: e.team.name,
      pj: e.all.played,
      g: e.all.win,
      e: e.all.draw,
      p: e.all.lose,
      gf: e.all.goals.for,
      gc: e.all.goals.against,
      dg: e.goalsDiff,
      pts: e.points,
      forma: (e.form || '').split('').map(c => ({ W: 'G', D: 'E', L: 'P' }[c] || 'E')),
      esNosotros: e.team.name.includes('Rubio')
    }))
  };
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const json = (datos) => new Response(JSON.stringify(datos), {
      headers: {
        'content-type': 'application/json; charset=utf-8',
        'cache-control': 'public, max-age=' + CACHE_SEGUNDOS
      }
    });

    try {
      if (url.pathname === '/api/tabla') {
        const r = await apiFootball(`/standings?league=${LIGA_ID}&season=${TEMPORADA}`, env);
        return json(normalizarTabla(r));
      }

      if (url.pathname === '/api/partidos') {
        const equipos = await apiFootball(`/teams?league=${LIGA_ID}&season=${TEMPORADA}&search=Rubio`, env);
        const id = equipos[0]?.team?.id;
        const [jugados, porJugar] = await Promise.all([
          apiFootball(`/fixtures?team=${id}&season=${TEMPORADA}&last=1`, env),
          apiFootball(`/fixtures?team=${id}&season=${TEMPORADA}&next=3`, env)
        ]);

        const mapear = (f) => ({
          fecha: f.fixture.date.slice(0, 10),
          hora: f.fixture.date.slice(11, 16),
          competencia: f.league.name + ' · Fecha ' + (f.league.round || '').replace(/\D/g, ''),
          local: f.teams.home.name,
          visitante: f.teams.away.name,
          estadio: f.fixture.venue?.name || '',
          condicion: f.teams.home.name.includes('Rubio') ? 'local' : 'visitante'
        });

        const u = jugados[0];
        return json({
          actualizado: new Date().toISOString().slice(0, 10),
          ultimo: u ? { ...mapear(u), golesLocal: u.goals.home, golesVisitante: u.goals.away } : null,
          proximos: porJugar.map(mapear)
        });
      }

      return new Response('No encontrado', { status: 404 });
    } catch (err) {
      return new Response(JSON.stringify({ error: err.message }), {
        status: 502,
        headers: { 'content-type': 'application/json; charset=utf-8' }
      });
    }
  }
};
