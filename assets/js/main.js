/* ============================================================
   Club Rubio Ñu — comportamiento del sitio

   El idioma y el prefijo de rutas se leen del <html>:
     <html lang="es-PY" data-base="">      → páginas en la raíz
     <html lang="en"    data-base="../">   → páginas en /en/
   ============================================================ */

/* Fuente de datos.
   Mientras el sitio vive en GitHub Pages, ORIGEN_VIVO queda vacío y todo
   se lee de los archivos de /data. Cuando el Worker de Cloudflare esté
   publicado, poner acá su URL base (por ejemplo '/api') y el sitio pasa a
   datos en vivo sin más cambios. */
const ORIGEN_VIVO = '';

const RAIZ = document.documentElement.dataset.base || '';
const IDIOMA = document.documentElement.lang.startsWith('en') ? 'en' : 'es';

const RUTAS = {
  tabla:    ORIGEN_VIVO ? ORIGEN_VIVO + '/tabla'    : RAIZ + 'data/tabla.json',
  partidos: ORIGEN_VIVO ? ORIGEN_VIVO + '/partidos' : RAIZ + 'data/partidos.json',
  plantel:  RAIZ + 'data/plantel.json',
  noticias: ORIGEN_VIVO ? ORIGEN_VIVO + '/noticias' : RAIZ + 'data/noticias.json'
};

const T = {
  es: {
    meses: ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'],
    dias: ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'],
    ultimoPartido: 'Último partido',
    proximosPartidos: 'Próximos partidos',
    deLocal: 'De local',
    deVisitante: 'De visitante',
    en: 'en',
    columnas: ['#', 'Equipo', 'PJ', 'G', 'E', 'P', 'GF', 'GC', 'DG', 'Pts', 'Últimos 5'],
    columnasCortas: ['#', 'Equipo', 'PJ', 'DG', 'Pts'],
    posicionesDe: 'Posiciones del',
    fecha: 'fecha',
    rotuloFecha: 'Fecha',
    actualizado: 'Actualizado el',
    sinHora: 'horario a confirmar',
    sede: 'sede a confirmar',
    verCalendario: 'Calendario completo',
    datosDe: 'Datos de la',
    gano: 'Ganó', empato: 'Empató', perdio: 'Perdió',
    puestos: { Arqueros: 'Arqueros', Defensores: 'Defensores', Mediocampistas: 'Mediocampistas', Delanteros: 'Delanteros' },
    sinTabla: 'La tabla no se pudo cargar. Recargá la página en un momento.',
    sinPartidos: 'Los datos de partidos no están disponibles.',
    sinPlantel: 'El plantel 2026 se publica acá apenas esté confirmado.',
    sinCuerpo: 'El cuerpo técnico se publica acá apenas esté confirmado.',
    sinNoticias: 'Todavía no hay noticias publicadas.',
    numero: 'Nº'
  },
  en: {
    meses: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    dias: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    ultimoPartido: 'Last match',
    proximosPartidos: 'Upcoming matches',
    deLocal: 'Home',
    deVisitante: 'Away',
    en: 'at',
    columnas: ['#', 'Team', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts', 'Last 5'],
    columnasCortas: ['#', 'Team', 'P', 'GD', 'Pts'],
    posicionesDe: 'Standings for the',
    fecha: 'matchday',
    rotuloFecha: 'Matchday',
    actualizado: 'Updated',
    sinHora: 'kick-off to be confirmed',
    sede: 'venue to be confirmed',
    verCalendario: 'Full calendar',
    datosDe: 'Data from the',
    gano: 'Won', empato: 'Drew', perdio: 'Lost',
    puestos: { Arqueros: 'Goalkeepers', Defensores: 'Defenders', Mediocampistas: 'Midfielders', Delanteros: 'Forwards' },
    sinTabla: 'The table could not be loaded. Please reload in a moment.',
    sinPartidos: 'Match data is not available.',
    sinPlantel: 'The 2026 squad will be published here as soon as it is confirmed.',
    sinCuerpo: 'The coaching staff will be published here as soon as it is confirmed.',
    sinNoticias: 'No news published yet.',
    numero: 'No.'
  }
}[document.documentElement.lang.startsWith('en') ? 'en' : 'es'];

function texto(valor) {
  /* Acepta un string suelto o un objeto {es, en} y devuelve el idioma activo. */
  if (valor && typeof valor === 'object') return valor[IDIOMA] || valor.es || '';
  return valor || '';
}

function filaPartido(p) {
  const f = leerFecha(p.fecha);
  const rival = p.condicion === 'local' ? p.visitante : p.local;
  const otro = p.condicion === 'local' ? p.local : p.visitante;
  const quien = rival && rival !== 'Rubio Ñu' ? rival : otro;

  /* Sin condición definida no se afirma dónde se juega. */
  const donde = p.condicion
    ? `${p.condicion === 'local' ? T.deLocal : T.deVisitante}${p.estadio ? ' ' + T.en + ' ' + p.estadio : ''}`
    : T.sede;

  const detalle = [donde, competencia(p)].filter(Boolean).join(' · ');
  const nota = p.nota ? `<div class="proximo-nota">${texto(p.nota)}</div>` : '';
  const hora = p.hora ? `${T.dias[f.getDay()]} ${p.hora}` : `${T.dias[f.getDay()]} · ${T.sinHora}`;

  return `<div class="proximo-fila">
      <div class="proximo-dia">${f.getDate()}<span>${T.meses[f.getMonth()]}</span></div>
      <div>
        <div class="proximo-rival">${quien}</div>
        <div class="proximo-detalle">${detalle}</div>
        ${nota}
      </div>
      <div class="proximo-hora">${hora}</div>
    </div>`;
}

function competencia(m) {
  return m.ronda ? `${m.torneo} · ${T.rotuloFecha} ${m.ronda}` : m.torneo || '';
}

function leerFecha(iso) {
  const [a, m, d] = iso.split('-').map(Number);
  return new Date(a, m - 1, d);
}

function diaMes(f) {
  return IDIOMA === 'en'
    ? `${T.meses[f.getMonth()]} ${f.getDate()}`
    : `${f.getDate()} de ${T.meses[f.getMonth()]}`;
}

async function traer(ruta) {
  const r = await fetch(ruta, { cache: 'no-store' });
  if (!r.ok) throw new Error('No se pudo leer ' + ruta);
  return r.json();
}

/* ---------- Menú ---------- */
function menu() {
  const boton = document.querySelector('.menu-boton');
  const lista = document.querySelector('.menu');
  if (!boton || !lista) return;
  boton.addEventListener('click', () => {
    const abierto = lista.classList.toggle('abierto');
    boton.setAttribute('aria-expanded', String(abierto));
  });
}

/* ---------- Tabla de posiciones ---------- */
function filaTabla(e, resumida) {
  const clases = e.esNosotros ? 'fila-nuestra' : '';
  const titulos = { G: T.gano, E: T.empato, P: T.perdio };
  const forma = (e.forma || [])
    .map(r => `<i class="${r}" title="${titulos[r] || ''}">${r}</i>`)
    .join('');

  const columnasLargas = resumida ? '' : `
      <td>${e.g}</td><td>${e.e}</td><td>${e.p}</td>
      <td>${e.gf}</td><td>${e.gc}</td>`;

  return `<tr class="${clases}">
      <td>${e.pos}</td>
      <td>${e.equipo}</td>
      <td>${e.pj}</td>${columnasLargas}
      <td>${e.dg > 0 ? '+' : ''}${e.dg}</td>
      <td class="pts">${e.pts}</td>
      ${resumida ? '' : `<td><span class="forma">${forma}</span></td>`}
    </tr>`;
}

async function tabla() {
  const destino = document.querySelector('[data-tabla]');
  if (!destino) return;
  const resumida = destino.dataset.tabla === 'resumida';

  try {
    const d = await traer(RUTAS.tabla);
    const encabezados = resumida ? T.columnasCortas : T.columnas;

    destino.innerHTML = `
      <div class="tabla-envoltorio">
        <table class="posiciones${resumida ? ' resumida' : ''}">
          <caption class="sr-only">${T.posicionesDe} ${texto(d.torneo)}</caption>
          <thead><tr>${encabezados.map(h => `<th scope="col">${h}</th>`).join('')}</tr></thead>
          <tbody>${d.equipos.map(e => filaTabla(e, resumida)).join('')}</tbody>
        </table>
      </div>
      <div class="leyenda-tabla">
        <span>${texto(d.torneo)}, ${T.fecha} ${d.fecha_jugada}</span>
        <span>${T.datosDe} ${texto(d.fuente)}</span>
        ${d.actualizado ? `<span>${T.actualizado} ${diaMes(leerFecha(d.actualizado))}</span>` : ''}
      </div>`;
  } catch (err) {
    destino.innerHTML = `<p class="vacio">${T.sinTabla}</p>`;
  }
}

/* ---------- Partidos ---------- */
async function partidos() {
  const cajaUltimo = document.querySelector('[data-ultimo]');
  const cajaProximos = document.querySelector('[data-proximos]');
  if (!cajaUltimo && !cajaProximos) return;

  try {
    const d = await traer(RUTAS.partidos);

    /* Sin datos cargados, la franja entera se oculta: es preferible no
       mostrarla a mostrarla vacía o con información sin confirmar. */
    if (!d.ultimo && !(d.proximos || []).length) {
      const franja = document.querySelector('.franja-partido');
      if (franja) franja.style.display = 'none';
      return;
    }

    if (cajaUltimo && d.ultimo) {
      const u = d.ultimo;
      cajaUltimo.innerHTML = `
        <p class="partido-rotulo">${T.ultimoPartido}</p>
        <div class="marcador">
          <span class="marcador-equipos">${u.local}<br>${u.visitante}</span>
          <span class="marcador-cifras">${u.golesLocal}–${u.golesVisitante}</span>
        </div>
        <p class="partido-pie">${competencia(u)} · ${diaMes(leerFecha(u.fecha))} · ${u.estadio}</p>`;
    }

    if (cajaProximos && d.proximos) {
      /* En la franja solo entran los tres más cercanos; el resto vive en el calendario. */
      const filas = d.proximos.slice(0, 3).map(filaPartido).join('');
      cajaProximos.innerHTML = `<p class="partido-rotulo">${T.proximosPartidos}</p>
        <div class="proximo-lista">${filas}</div>`;
    }
  } catch (err) {
    if (cajaUltimo) cajaUltimo.innerHTML = `<p class="partido-pie">${T.sinPartidos}</p>`;
    if (cajaProximos) cajaProximos.innerHTML = '';
  }
}

/* ---------- Calendario completo ---------- */
async function calendario() {
  const destino = document.querySelector('[data-calendario]');
  if (!destino) return;
  try {
    const d = await traer(RUTAS.partidos);
    const lista = d.proximos || [];
    destino.innerHTML = lista.length
      ? `<div class="proximo-lista calendario">${lista.map(filaPartido).join('')}</div>`
      : `<p class="vacio">${T.sinPartidos}</p>`;
  } catch (err) {
    destino.innerHTML = `<p class="vacio">${T.sinPartidos}</p>`;
  }
}

/* ---------- Plantel y cuerpo técnico ---------- */
async function plantel() {
  const destino = document.querySelector('[data-plantel]');
  const cuerpo = document.querySelector('[data-cuerpo-tecnico]');
  if (!destino && !cuerpo) return;

  let d;
  try {
    d = await traer(RUTAS.plantel);
  } catch (err) {
    if (destino) destino.innerHTML = `<p class="vacio">${T.sinPlantel}</p>`;
    if (cuerpo) cuerpo.innerHTML = `<p class="vacio">${T.sinCuerpo}</p>`;
    return;
  }

  if (destino) {
    const conNombre = (d.jugadores || []).filter(j => j.nombre);
    if (!conNombre.length) {
      destino.innerHTML = `<p class="vacio">${T.sinPlantel}</p>`;
    } else {
      const orden = ['Arqueros', 'Defensores', 'Mediocampistas', 'Delanteros'];
      destino.innerHTML = orden.map(puesto => {
        const grupo = conNombre.filter(j => j.puesto === puesto);
        if (!grupo.length) return '';
        const fichas = grupo.map(j => `
          <article class="jugador">
            <div class="jugador-foto">
              ${j.foto ? `<img src="${RAIZ}${j.foto}" alt="${j.nombre}" loading="lazy">`
                       : `<span class="jugador-numero">${j.numero || ''}</span>`}
            </div>
            <div class="jugador-info">
              <strong>${j.nombre}</strong>
              <span>${j.numero ? T.numero + ' ' + j.numero : ''}</span>
            </div>
          </article>`).join('');
        return `<section class="plantel-grupo"><h3>${T.puestos[puesto]}</h3>
          <div class="plantel-grilla">${fichas}</div></section>`;
      }).join('');
    }
  }

  if (cuerpo) {
    const staff = (d.cuerpoTecnico || []).filter(m => m.nombre);
    cuerpo.innerHTML = staff.length
      ? `<dl class="datos-grilla">${staff.map(m =>
          `<div class="dato"><dt>${texto(m.rol)}</dt><dd>${m.nombre}</dd></div>`).join('')}</dl>`
      : `<p class="vacio">${T.sinCuerpo}</p>`;
  }
}

/* ---------- Noticias ---------- */
async function noticias() {
  const destino = document.querySelector('[data-noticias]');
  if (!destino) return;
  const limite = parseInt(destino.dataset.limite || '0', 10);

  try {
    const d = await traer(RUTAS.noticias);
    let entradas = d.entradas || [];
    if (limite) entradas = entradas.slice(0, limite);

    if (!entradas.length) {
      destino.innerHTML = `<p class="vacio">${T.sinNoticias}</p>`;
      return;
    }

    destino.innerHTML = `<div class="noticias-grilla">${entradas.map(n => {
      const f = leerFecha(n.fecha);
      const fecha = IDIOMA === 'en' ? `${diaMes(f)}, ${f.getFullYear()}` : `${diaMes(f)} de ${f.getFullYear()}`;
      const medio = n.medio ? `<span class="noticia-medio">${n.medio}</span>` : '';
      return `<a class="noticia" href="${n.enlace || '#'}"${n.enlace ? ' target="_blank" rel="noopener"' : ''}>
        <time datetime="${n.fecha}">${fecha}</time>
        <h3>${texto(n.titulo)}</h3>
        <p>${texto(n.bajada)}</p>
        ${medio}
      </a>`;
    }).join('')}</div>`;
  } catch (err) {
    destino.innerHTML = `<p class="vacio">${T.sinNoticias}</p>`;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  menu();
  tabla();
  partidos();
  calendario();
  plantel();
  noticias();
});
