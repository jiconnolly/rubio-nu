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

## Pasar a datos en vivo

Hoy la tabla y los partidos se leen de los JSON estáticos. Para automatizarlos:

1. Crear cuenta gratuita en `dashboard.api-football.com`
2. Publicar `worker/api.js` en Cloudflare con la key como secret
3. En `assets/js/main.js`, poner `ORIGEN_VIVO = '/api'`

No usar los widgets de copiar y pegar de API-Football: obligan a dejar la key
visible en el HTML.

## Antes de publicar

Todas las páginas llevan `noindex` mientras el contenido esté sin aprobar. Hay que
sacarlo de `build.py` y regenerar cuando el club dé el visto bueno.
