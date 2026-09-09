# Sitio oficial — Club Rubio Ñu

Sitio estático. Sin build, sin dependencias. Se publica tal cual desde GitHub Pages
y más adelante migra a Cloudflare Workers.

## Estructura

```
index.html          Portada
club.html           Historia, estadio, comisión directiva
plantel.html        Plantel y cuerpo técnico
fixture.html        Fixture, resultados y tabla de posiciones
noticias.html       Listado de noticias
socios.html         Categorías de socio y formulario de alta
contacto.html       Datos de contacto y formulario

assets/css/main.css Hoja de estilos única
assets/js/main.js   Menú, tabla, partidos y plantel
assets/img/         Escudo y fotografías
data/*.json         Datos editables
worker/api.js       Worker de Cloudflare (todavía sin usar)
build.py            Regenera las páginas desde plantillas compartidas
```

Las siete páginas comparten cabecera y pie. Para cambiar el menú, el pie o los
metadatos hay que editar `build.py` y correr `python3 build.py`, no los HTML
sueltos, porque el script los sobreescribe.

## Actualizar datos

- **Tabla de posiciones**: `data/tabla.json`
- **Último resultado y próximos partidos**: `data/partidos.json`
- **Plantel**: `data/plantel.json` — los jugadores sin `nombre` no se muestran

## Actualización semanal de la tabla

La tabla se carga a mano. Cada semana, después de la fecha:

1. Abrir `data/tabla.json`
2. Actualizar los doce equipos con los datos de la APF
3. Cambiar `fecha_jugada` y `actualizado` (formato AAAA-MM-DD)

La fecha de actualización se muestra debajo de la tabla en el sitio, así que
si queda vieja se nota. `forma` son los últimos cinco partidos, del más viejo
al más nuevo, con G de ganó, E de empató y P de perdió. La marca
`"esNosotros": true` es la que pinta de verde la fila de Rubio Ñu.

Para el último resultado y los próximos partidos, `data/partidos.json`. Si
`ultimo` es `null` y `proximos` está vacío, la franja de partidos se oculta
sola: es preferible no mostrarla a mostrar datos sin confirmar.

## Datos en vivo (pendiente)

`worker/index.js` trae la tabla y los partidos desde API-Football, pero NO está
en uso: el plan gratuito no da acceso a la temporada 2026 y devuelve
`"Free plans do not have access to this season, try from 2022 to 2024."`.
Requiere plan pago. Para activarlo: agregar `"main": "worker/index.js"` y el
binding `ASSETS` en `wrangler.jsonc`, cargar el secret `API_FOOTBALL_KEY` y
poner `ORIGEN_VIVO = '/api'` en `assets/js/main.js`.

## Antes de publicar

Todas las páginas llevan `noindex` mientras el contenido esté sin aprobar. Hay que
sacarlo de `build.py` y regenerar cuando el club dé el visto bueno.
