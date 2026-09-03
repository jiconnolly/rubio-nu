/* ============================================================
   Club Rubio Ñu — comportamiento del sitio
   ============================================================ */

/* Fuente de datos.
   Mientras el sitio vive en GitHub Pages, ORIGEN_VIVO queda vacío y todo
   se lee de los JSON estáticos de /data.
   Cuando el Worker de Cloudflare esté publicado, poner acá su URL base
   (por ejemplo '/api') y el sitio pasa a datos en vivo sin más cambios. */
const ORIGEN_VIVO = '';

const RUTAS = {
  tabla:    ORIGEN_VIVO ? ORIGEN_VIVO + '/tabla'    : 'data/tabla.json',
  partidos: ORIGEN_VIVO ? ORIGEN_VIVO + '/partidos' : 'data/partidos.json',
  plantel:  'data/plantel.json'
};

const MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'];
const DIAS = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'];

function leerFecha(iso) {
  const [a, m, d] = iso.split('-').map(Number);
  return new Date(a, m - 1, d);
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

  const forma = (e.forma || [])
    .map(r => `<i class="${r}" title="${r === 'G' ? 'Ganó' : r === 'E' ? 'Empató' : 'Perdió'}">${r}</i>`)
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
    const encabezados = resumida
      ? ['#', 'Equipo', 'PJ', 'DG', 'Pts']
      : ['#', 'Equipo', 'PJ', 'G', 'E', 'P', 'GF', 'GC', 'DG', 'Pts', 'Últimos 5'];

    destino.innerHTML = `
      <div class="tabla-envoltorio">
        <table class="posiciones${resumida ? ' resumida' : ''}">
          <caption class="sr-only">Posiciones del ${d.torneo}</caption>
          <thead><tr>${encabezados.map(h => `<th scope="col">${h}</th>`).join('')}</tr></thead>
          <tbody>${d.equipos.map(e => filaTabla(e, resumida)).join('')}</tbody>
        </table>
      </div>
      <div class="leyenda-tabla">
        <span>${d.torneo}, fecha ${d.fecha_jugada}</span>
        <span>Datos de la ${d.fuente}</span>
      </div>`;
  } catch (err) {
    destino.innerHTML = '<p class="vacio">La tabla no se pudo cargar. Recargá la página en un momento.</p>';
  }
}

/* ---------- Partidos ---------- */
async function partidos() {
  const cajaUltimo = document.querySelector('[data-ultimo]');
  const cajaProximos = document.querySelector('[data-proximos]');
  if (!cajaUltimo && !cajaProximos) return;

  try {
    const d = await traer(RUTAS.partidos);

    if (cajaUltimo && d.ultimo) {
      const u = d.ultimo;
      const f = leerFecha(u.fecha);
      cajaUltimo.innerHTML = `
        <p class="partido-rotulo">Último partido</p>
        <div class="marcador">
          <span class="marcador-equipos">${u.local}<br>${u.visitante}</span>
          <span class="marcador-cifras">${u.golesLocal}–${u.golesVisitante}</span>
        </div>
        <p class="partido-pie">${u.competencia} · ${f.getDate()} de ${MESES[f.getMonth()]} · ${u.estadio}</p>`;
    }

    if (cajaProximos && d.proximos) {
      const filas = d.proximos.map(p => {
        const f = leerFecha(p.fecha);
        const rival = p.condicion === 'local' ? p.visitante : p.local;
        return `<div class="proximo-fila">
            <div class="proximo-dia">${f.getDate()}<span>${MESES[f.getMonth()]}</span></div>
            <div>
              <div class="proximo-rival">${rival}</div>
              <div class="proximo-detalle">${p.condicion === 'local' ? 'De local' : 'De visitante'} en ${p.estadio} · ${p.competencia}</div>
            </div>
            <div class="proximo-hora">${DIAS[f.getDay()]} ${p.hora}</div>
          </div>`;
      }).join('');
      cajaProximos.innerHTML = `<p class="partido-rotulo">Próximos partidos</p>
        <div class="proximo-lista">${filas}</div>`;
    }
  } catch (err) {
    if (cajaUltimo) cajaUltimo.innerHTML = '<p class="partido-pie">Los datos de partidos no están disponibles.</p>';
    if (cajaProximos) cajaProximos.innerHTML = '';
  }
}

/* ---------- Plantel ---------- */
async function plantel() {
  const destino = document.querySelector('[data-plantel]');
  if (!destino) return;

  try {
    const d = await traer(RUTAS.plantel);
    const conNombre = (d.jugadores || []).filter(j => j.nombre);

    if (!conNombre.length) {
      destino.innerHTML = '<p class="vacio">El plantel 2026 se publica acá apenas esté confirmado.</p>';
      return;
    }

    const orden = ['Arqueros', 'Defensores', 'Mediocampistas', 'Delanteros'];
    destino.innerHTML = orden.map(puesto => {
      const grupo = conNombre.filter(j => j.puesto === puesto);
      if (!grupo.length) return '';
      const fichas = grupo.map(j => `
        <article class="jugador">
          <div class="jugador-foto">
            ${j.foto ? `<img src="${j.foto}" alt="${j.nombre}" loading="lazy">`
                     : `<span class="jugador-numero">${j.numero || ''}</span>`}
          </div>
          <div class="jugador-info">
            <strong>${j.nombre}</strong>
            <span>${j.numero ? 'Nº ' + j.numero : ''}</span>
          </div>
        </article>`).join('');
      return `<section class="plantel-grupo"><h3>${puesto}</h3>
        <div class="plantel-grilla">${fichas}</div></section>`;
    }).join('');
  } catch (err) {
    destino.innerHTML = '<p class="vacio">El plantel no se pudo cargar.</p>';
  }
}

document.addEventListener('DOMContentLoaded', () => {
  menu();
  tabla();
  partidos();
  plantel();
});
