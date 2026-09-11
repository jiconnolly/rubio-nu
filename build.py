# -*- coding: utf-8 -*-
"""Genera el sitio de Club Rubio Ñu en español (raíz) e inglés (/en/).

Editar este archivo y correr `python3 build.py`. Nunca editar los HTML sueltos:
el script los sobreescribe.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
IDIOMAS = ("es", "en")

PAGINAS = ["index", "club", "plantel", "fixture", "noticias", "socios", "contacto"]

NAV = {
    "es": [("index", "Inicio"), ("club", "El club"), ("plantel", "Plantel"),
           ("fixture", "Fixture y tabla"), ("noticias", "Noticias"),
           ("socios", "Hacete socio"), ("contacto", "Contacto")],
    "en": [("index", "Home"), ("club", "The club"), ("plantel", "Squad"),
           ("fixture", "Fixtures"), ("noticias", "News"),
           ("socios", "Membership"), ("contacto", "Contact")],
}

META = {
    "es": {
        "index": ("Sitio oficial", "Sitio oficial del Club Rubio Ñu, de Santísima Trinidad, Asunción. Fundado en 1913."),
        "club": ("El club", "Historia, estadio y datos institucionales del Club Rubio Ñu."),
        "plantel": ("Plantel", "Plantel y cuerpo técnico del Club Rubio Ñu, temporada 2026."),
        "fixture": ("Fixture y tabla", "Fixture, resultados y tabla de posiciones del Club Rubio Ñu."),
        "noticias": ("Noticias", "Novedades del Club Rubio Ñu."),
        "socios": ("Hacete socio", "Categorías de socio y alta en el Club Rubio Ñu."),
        "contacto": ("Contacto", "Datos de contacto del Club Rubio Ñu."),
    },
    "en": {
        "index": ("Official site", "Official site of Club Rubio Ñu, from Santísima Trinidad, Asunción. Founded in 1913."),
        "club": ("The club", "History, stadium and institutional facts about Club Rubio Ñu."),
        "plantel": ("Squad", "Club Rubio Ñu first-team squad and coaching staff, 2026 season."),
        "fixture": ("Fixtures", "Club Rubio Ñu fixtures, results and league table."),
        "noticias": ("News", "Latest from Club Rubio Ñu."),
        "socios": ("Membership", "Membership categories and sign-up at Club Rubio Ñu."),
        "contacto": ("Contact", "Contact details for Club Rubio Ñu."),
    },
}

CHROME = {
    "es": {
        "saltar": "Ir al contenido",
        "menu": "Menú",
        "kicker": "ASUNCIÓN 1913",
        "otro_idioma": "English",
        "sponsors": "SPONSORS",
        "instituciones": "Rubio Ñu está afiliado a la Asociación Paraguaya de Fútbol, miembro de la CONMEBOL.",
        "pie_direccion": "Barrio Santísima Trinidad, Asunción, Paraguay.<br>Fundado el 24 de agosto de 1913.",
        "pie_columnas": [
            ("EL CLUB", [("club", "Historia"), ("club#nombre", "El nombre"), ("club#estadio", "La Arboleda"), ("club#inferiores", "Inferiores"), ("plantel", "Plantel")]),
            ("COMPETENCIA", [("fixture", "Fixture"), ("fixture#tabla", "Tabla de posiciones"), ("noticias", "Noticias")]),
            ("PARTICIPAR", [("socios", "Hacete socio"), ("contacto", "Contacto"), ("contacto#prensa", "Prensa")]),
        ],
        "pie_legal": "© 2026 Club Rubio Ñu. Todos los derechos reservados.",
        "pie_liga": "Asociación Paraguaya de Fútbol · División de Honor",
    },
    "en": {
        "saltar": "Skip to content",
        "menu": "Menu",
        "kicker": "ASUNCIÓN 1913",
        "otro_idioma": "Español",
        "sponsors": "SPONSORS",
        "instituciones": "Rubio Ñu is affiliated to the Paraguayan Football Association, a member of CONMEBOL.",
        "pie_direccion": "Santísima Trinidad, Asunción, Paraguay.<br>Founded on 24 August 1913.",
        "pie_columnas": [
            ("THE CLUB", [("club", "History"), ("club#nombre", "The name"), ("club#estadio", "La Arboleda"), ("club#inferiores", "Academy"), ("plantel", "Squad")]),
            ("COMPETITION", [("fixture", "Fixtures"), ("fixture#tabla", "League table"), ("noticias", "News")]),
            ("GET INVOLVED", [("socios", "Membership"), ("contacto", "Contact"), ("contacto#prensa", "Press")]),
        ],
        "pie_legal": "© 2026 Club Rubio Ñu. All rights reserved.",
        "pie_liga": "Paraguayan Football Association · First Division",
    },
}

IG = ('https://www.instagram.com/rubionu.1913/', 'Instagram',
      '<path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.2.05 1.8.25 2.2.42.6.22 1 .48 1.4.9.43.42.7.83.9 1.4.18.4.38 1 .43 2.2.06 1.3.07 1.7.07 4.9s0 3.6-.07 4.9c-.05 1.2-.25 1.8-.42 2.2-.22.6-.48 1-.9 1.4-.42.43-.83.7-1.4.9-.4.18-1 .38-2.2.43-1.3.06-1.7.07-4.9.07s-3.6 0-4.9-.07c-1.2-.05-1.8-.25-2.2-.42-.6-.22-1-.48-1.4-.9-.43-.42-.7-.83-.9-1.4-.18-.4-.38-1-.43-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.07-4.9c.05-1.2.25-1.8.42-2.2.22-.6.48-1 .9-1.4.42-.43.83-.7 1.4-.9.4-.18 1-.38 2.2-.43C8.4 2.2 8.8 2.2 12 2.2zm0 1.8c-3.1 0-3.5 0-4.7.07-1.1.05-1.7.24-2.1.4-.5.2-.9.44-1.3.83-.4.4-.63.8-.83 1.3-.16.4-.35 1-.4 2.1C2.6 9.9 2.6 10.3 2.6 12s0 2.1.07 3.3c.05 1.1.24 1.7.4 2.1.2.5.44.9.83 1.3.4.4.8.63 1.3.83.4.16 1 .35 2.1.4 1.2.07 1.6.07 4.7.07s3.5 0 4.7-.07c1.1-.05 1.7-.24 2.1-.4.5-.2.9-.44 1.3-.83.4-.4.63-.8.83-1.3.16-.4.35-1 .4-2.1.07-1.2.07-1.6.07-3.3s0-2.1-.07-3.3c-.05-1.1-.24-1.7-.4-2.1-.2-.5-.44-.9-.83-1.3-.4-.4-.8-.63-1.3-.83-.4-.16-1-.35-2.1-.4C15.5 4 15.1 4 12 4zm0 3.1a4.9 4.9 0 110 9.8 4.9 4.9 0 010-9.8zm0 8.1a3.2 3.2 0 100-6.4 3.2 3.2 0 000 6.4zm6.2-8.3a1.15 1.15 0 11-2.3 0 1.15 1.15 0 012.3 0z"/>')

FB = ('https://www.facebook.com/clubrubionu', 'Facebook',
      '<path d="M22 12a10 10 0 10-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7A10 10 0 0022 12z"/>')

REDES = [IG, FB]


def bloque_redes(clase=""):
    enlaces = "\n".join(
        '        <a href="{u}" target="_blank" rel="noopener" aria-label="{n}">'
        '<svg viewBox="0 0 24 24" aria-hidden="true">{p}</svg></a>'.format(u=u, n=n, p=path)
        for u, n, path in REDES
    )
    return '      <div class="redes {c}">\n{e}\n      </div>'.format(c=clase, e=enlaces)


SPONSORS = [
    ("kia.png", "Kia", ""),
    ("ueno-bank.png", "ueno bank", ""),
    ("garcis.png", "Garcis", "alto"),
    ("bambi.png", "Bambi", "alto"),
    ("lacteos-trebol.png", "Lácteos Trébol", "alto"),
]


def ruta_salida(idioma, pagina):
    if idioma == "es":
        return os.path.join(BASE, pagina + ".html")
    return os.path.join(BASE, "en", pagina + ".html")


def prefijo(idioma):
    """Prefijo relativo hacia la raíz del sitio para assets y datos."""
    return "" if idioma == "es" else "../"


def enlace_otro_idioma(idioma, pagina):
    return ("en/" + pagina + ".html") if idioma == "es" else ("../" + pagina + ".html")


def cabecera(idioma, pagina):
    t = CHROME[idioma]
    base = prefijo(idioma)
    titulo, descripcion = META[idioma][pagina]
    lang = "es-PY" if idioma == "es" else "en"

    enlaces = "\n".join(
        '        <a href="{h}.html"{a}>{t}</a>'.format(
            h=h, t=txt, a=' aria-current="page"' if h == pagina else ""
        )
        for h, txt in NAV[idioma]
    )

    alterno_es = ("" if idioma == "es" else "../") + pagina + ".html"
    alterno_en = ("en/" if idioma == "es" else "") + pagina + ".html"

    return f"""<!DOCTYPE html>
<html lang="{lang}" data-base="{base}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · Club Rubio Ñu</title>
<meta name="description" content="{descripcion}">
<meta name="robots" content="noindex, nofollow">
<link rel="alternate" hreflang="es" href="{alterno_es}">
<link rel="alternate" hreflang="en" href="{alterno_en}">
<meta property="og:title" content="{titulo} · Club Rubio Ñu">
<meta property="og:description" content="{descripcion}">
<meta property="og:type" content="website">
<meta property="og:image" content="{base}assets/img/escudo.png">
<meta name="theme-color" content="#10201A">
<link rel="icon" href="{base}assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Karla:ital,wght@0,400;0,500;0,700;1,400&family=Oswald:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/main.css">
</head>
<body>
<a class="saltar" href="#contenido">{t['saltar']}</a>

<header class="cabecera">
  <div class="marco cabecera-fila">
    <a class="marca" href="index.html">
      <img src="{base}assets/img/escudo.png" alt="">
      <span class="marca-texto">Rubio Ñu
        <small>{t['kicker']}</small>
      </span>
    </a>
    <div class="cabecera-derecha">
      <a class="idioma" href="{enlace_otro_idioma(idioma, pagina)}">{t['otro_idioma']}</a>
      <button class="menu-boton" aria-expanded="false" aria-controls="menu-principal">{t['menu']}</button>
    </div>
    <nav class="menu" id="menu-principal" aria-label="{t['menu']}">
{enlaces}
    </nav>
  </div>
</header>
<div class="filete bastones"></div>

<main id="contenido">
"""


def banda_sponsors(idioma):
    base = prefijo(idioma)
    logos = "\n".join(
        '        <img src="{b}assets/img/sponsors/{a}" alt="{n}" class="{c}" loading="lazy">'.format(
            b=base, a=a, n=n, c=c
        )
        for a, n, c in SPONSORS
    )
    return f"""<section class="banda-sponsors">
  <div class="marco">
    <p class="rotulo-sponsors">{CHROME[idioma]['sponsors']}</p>
    <div class="grilla-sponsors">
{logos}
    </div>
  </div>
</section>

"""


def pie(idioma):
    t = CHROME[idioma]
    base = prefijo(idioma)
    def href(destino):
        if "#" in destino:
            pagina, ancla = destino.split("#", 1)
            return f"{pagina}.html#{ancla}"
        return f"{destino}.html"

    columnas = "\n".join(
        """      <div>
        <h4>{titulo}</h4>
        <ul>
{items}
        </ul>
      </div>""".format(
            titulo=titulo,
            items="\n".join(
                f'          <li><a href="{href(h)}">{txt}</a></li>' for h, txt in items
            ),
        )
        for titulo, items in t["pie_columnas"]
    )

    return banda_sponsors(idioma) + f"""</main>

<footer class="pie">
  <div class="marco">
    <div class="instituciones">
      <div class="instituciones-escudos">
        <span><img src="{base}assets/img/instituciones/apf.png" alt="Asociación Paraguaya de Fútbol"></span>
        <span><img src="{base}assets/img/instituciones/conmebol.png" alt="CONMEBOL"></span>
      </div>
      <p>{t['instituciones']}</p>
    </div>
    <div class="pie-grilla">
      <div class="pie-escudo">
        <img src="{base}assets/img/escudo.png" alt="">
        <div>
          <strong style="color:var(--blanco)">Club Rubio Ñu</strong><br>
          {t['pie_direccion']}
{bloque_redes()}
        </div>
      </div>
{columnas}
    </div>
    <div class="pie-legal">
      <span>{t['pie_legal']}</span>
      <span>{t['pie_liga']}</span>
    </div>
  </div>
</footer>

<script src="{base}assets/js/main.js"></script>
</body>
</html>
"""


# ================================================================ CONTENIDO ES
ES = {}

ES["index"] = """
<section class="portada-foto">
  <div class="fondo" style="background-image:url('{base}assets/img/portada-arboleda.webp')"></div>
  <div class="velo"></div>
  <div class="marco">
    <div class="placa">
      <img src="{base}assets/img/escudo.png" alt="Escudo del Club Rubio Ñu">
      <div>
        <p class="placa-kicker">Santísima Trinidad · Asunción</p>
        <h1>Rubio Ñu</h1>
        <p class="lema">Ciento trece años en la misma manzana. Blanco por la pureza, verde por la
        esperanza: el albiverde volvió a la División de Honor.</p>
      </div>
    </div>
    <div class="pie-foto">
      <span>Estadio <b>La Arboleda</b>, el barrio donde el club se fundó en <b>1913</b></span>
      <span class="sello">Albiverde · Ñuenses · Laureado</span>
    </div>
  </div>
</section>
<div class="filete bastones"></div>

<section class="franja-partido">
  <div class="marco partido-grilla">
    <div data-ultimo><p class="cargando">Cargando resultado…</p></div>
    <div class="divisoria" aria-hidden="true"></div>
    <div data-proximos><p class="cargando">Cargando calendario…</p></div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <div class="cabezal-seccion">
      <div>
        <h2 class="titulo-seccion">Cómo va el Clausura</h2>
        <p class="entrada">Posiciones de la División de Honor, actualizadas fecha a fecha.</p>
      </div>
      <a class="enlace-mas" href="fixture.html#tabla">Tabla completa y fixture</a>
    </div>
    <div data-tabla="resumida"><p class="cargando">Cargando tabla…</p></div>
  </div>
</section>

<section class="banda-foto">
  <div class="fondo" style="background-image:url('{base}assets/img/barrio-trinidad.webp')"></div>
  <div class="velo"></div>
  <div class="marco">
    <p class="banda-cita">El club nunca se mudó del barrio
      <span>Santísima Trinidad, Asunción, desde 1913.</span>
    </p>
  </div>
</section>

<section class="seccion seccion-tinta textura-diagonal">
  <div class="marco">
    <h2 class="titulo-seccion">El club siempre vuelve</h2>
    <p class="entrada">Rubio Ñu nació en 1913 en Santísima Trinidad y nunca se movió del barrio.
    La resiliencia es lo que define su historia.</p>
    <div class="hitos">
      <article class="hito">
        <div class="hito-anio">1913</div>
        <div>
          <h3>La fundación</h3>
          <p>Un grupo de muchachos, todos menores de dieciocho años, funda el club el 24 de agosto
          y lo llama como el campo donde se creía que habían peleado los niños de Acosta Ñu.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">1936</div>
        <div>
          <h3>La refundación</h3>
          <p>Tras veintitrés años de historia, Itá Ybaté y Flor de Mayo, dos clubes del mismo
          barrio, se fusionan con Rubio Ñu para mantenerlo con vida.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">2025</div>
        <div>
          <h3>Campeón de la Intermedia</h3>
          <p>El equipo gana la segunda categoría y sella el ascenso a la División de Honor.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">2026</div>
        <div>
          <h3>De vuelta en Primera</h3>
          <p>Rubio Ñu compite otra vez contra los clubes más grandes del país, con La Arboleda
          como sede de sus partidos de local.</p>
        </div>
      </article>
    </div>
    <p style="margin-top:2rem"><a class="enlace-mas" href="club.html">Toda la historia del club</a></p>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <div class="cabezal-seccion">
      <h2 class="titulo-seccion">Noticias</h2>
      <a class="enlace-mas" href="noticias.html">Ver todas</a>
    </div>
    <div data-noticias data-limite="3"><p class="cargando">Cargando noticias…</p></div>
  </div>
</section>

<section class="banda-foto">
  <div class="fondo" style="background-image:url('{base}assets/img/tribuna-arboleda.webp')"></div>
  <div class="velo"></div>
  <div class="marco">
    <p class="banda-cita">Cada quince días, esta tribuna se llena
      <span>La Arboleda, Santísima Trinidad.</span>
    </p>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <div class="accion">
      <div>
        <h2>Hacete socio</h2>
        <p>El socio sostiene al club todo el año: entra a La Arboleda, elige su butaca y decide en
        la asamblea.</p>
      </div>
      <div class="botonera">
        <a class="boton" href="socios.html">Ver las categorías</a>
        <a class="boton boton-borde" href="contacto.html">Escribirnos</a>
      </div>
    </div>
  </div>
</section>
"""

ES["club"] = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="">
    <div>
      <h1>El club</h1>
      <p class="portada-bajada">Un club de barrio con más de un siglo de historia.</p>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="marco dos-columnas">
    <div>
      <h2 class="titulo-seccion">Un club de barrio con más de un siglo de historia</h2>
      <p>Rubio Ñu nació el 24 de agosto de 1913 en el barrio de Santísima Trinidad, Asunción, de la
      mano de un grupo de amigos que eligió el blanco y el verde como colores del club: blanco por
      la pureza, verde por la esperanza. Esa combinación le dio al club su apodo, albiverde.</p>
      <p>En 1936, tras veintitrés años de historia, dos clubes del mismo barrio, Itá Ybaté y Flor de
      Mayo, se fusionaron con Rubio Ñu para mantenerlo con vida. Esa refundación marcó al club:
      volver siempre, incluso después de las bajas.</p>
      <p>El club juega sus partidos como local en el Estadio La Arboleda, y sostiene su rivalidad
      histórica con Sportivo Trinidense en el Clásico de Trinidad. A sus jugadores e hinchas se los
      conoce como ñuenses.</p>
    </div>
    <div>
      <h3 style="font-size:1.1rem;color:var(--verde-hondo);margin-bottom:1rem">Valores</h3>
      <ul class="lista-marca">
        <li>Resiliencia: el club siempre vuelve.</li>
        <li>Identidad de barrio, en Santísima Trinidad.</li>
        <li>Formación de talento joven.</li>
        <li>Proyección sudamericana.</li>
      </ul>
    </div>
  </div>
</section>

<section class="seccion seccion-tinta" id="nombre">
  <div class="marco dos-columnas">
    <div>
      <h2 class="titulo-seccion">De dónde viene el nombre</h2>
      <p style="color:rgba(255,255,255,0.78)">El 16 de agosto de 1869, en la Guerra de la Triple
      Alianza, un ejército paraguayo compuesto en buena parte por niños resistió en Barrero Grande,
      la actual ciudad de Eusebio Ayala. Se la recuerda como la batalla de los niños.</p>
      <p style="color:rgba(255,255,255,0.78)">Durante décadas ese combate se llamó Rubio Ñu. El
      error venía de un poema del sacerdote Juan B. Tournedou y se repitió hasta 1948, cuando el
      historiador Andrés Aguirre consiguió por decreto que se lo llamara Acosta Ñu, el nombre de
      los campos donde efectivamente ocurrió, y que el 16 de agosto fuera el Día del Niño.</p>
      <p style="color:rgba(255,255,255,0.78)">El club se fundó en 1913, treinta y cinco años antes
      de esa corrección. Un grupo de muchachos de Santísima Trinidad, todos menores de dieciocho
      años, le puso a su club el nombre con el que entonces se conocía la batalla, y eligió el
      blanco y el verde como homenaje a esos chicos. <em>Ñu</em> es campo en guaraní.</p>
    </div>
    <div>
      <p class="cita-mision" style="color:var(--verde);max-width:20ch">Chicos que le pusieron a su
      club el nombre de otros chicos</p>
      <p style="color:rgba(255,255,255,0.6);font-size:0.88rem;margin-top:1.25rem">Esta sección
      espera la validación del archivo histórico del club.</p>
    </div>
  </div>
  <div class="marco">
    <figure class="figura-estadio figura-ancha">
      <img src="{base}assets/img/ninos-martires.webp"
           alt="Monumento a los Niños Mártires de Acosta Ñu, con la bandera paraguaya recortada en chapa y las siluetas de un soldado y un niño"
           loading="lazy" width="1600" height="1066">
      <figcaption>
        <span>Monumento a los Niños Mártires, en Eusebio Ayala, donde ocurrió la batalla.</span>
        <span><b>16 de agosto</b>, Día del Niño en Paraguay</span>
      </figcaption>
    </figure>
  </div>
</section>

<section class="seccion seccion-verde">
  <div class="marco dos-columnas">
    <p class="cita-mision">Un club histórico de barrio que honra su resiliencia de más de cien
    años y que busca consolidarse como miembro permanente de la Primera División.</p>
    <p class="entrada" style="margin:0">La misión del club es formar y exportar talento paraguayo y
    sudamericano, sosteniendo el crecimiento deportivo e institucional sin perder la identidad de
    Santísima Trinidad.</p>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <h2 class="titulo-seccion">Datos institucionales</h2>
    <dl class="datos-grilla">
      <div class="dato"><dt>Fundación</dt><dd>24 de agosto de 1913</dd></div>
      <div class="dato"><dt>Barrio</dt><dd>Santísima Trinidad</dd></div>
      <div class="dato"><dt>Ciudad</dt><dd>Asunción, Paraguay</dd></div>
      <div class="dato"><dt>Estadio</dt><dd>La Arboleda</dd></div>
      <div class="dato"><dt>Apodos</dt><dd>Albiverde, Ñuenses, Laureado</dd></div>
      <div class="dato"><dt>Clásico</dt><dd>Sportivo Trinidense</dd></div>
      <div class="dato"><dt>Categoría 2026</dt><dd>División de Honor</dd></div>
      <div class="dato"><dt>Asociación</dt><dd>APF</dd></div>
    </dl>
  </div>
</section>

<section class="seccion seccion-tinta textura-diagonal">
  <div class="marco">
    <h2 class="titulo-seccion">Línea de tiempo</h2>
    <div class="hitos">
      <article class="hito">
        <div class="hito-anio">1913</div>
        <div>
          <h3>La fundación</h3>
          <p>Un grupo de muchachos menores de dieciocho años funda el club el 24 de agosto en
          Santísima Trinidad, en homenaje a los niños de Acosta Ñu, y elige el blanco y el verde.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">1926</div>
        <div>
          <h3>Primer título</h3>
          <p>Rubio Ñu se corona campeón de la División Intermedia por primera vez y sube a la
          categoría principal.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">1927</div>
        <div>
          <h3>Debut en Primera</h3>
          <p>El club juega su primera temporada en la máxima categoría del fútbol paraguayo.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">1932</div>
        <div>
          <h3>La Guerra del Chaco</h3>
          <p>La institución suspende sus actividades: dirigentes y deportistas pasan a integrar el
          ejército en campaña. El club retoma su curso al terminar la contienda.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">1936</div>
        <div>
          <h3>La refundación</h3>
          <p>Itá Ybaté y Flor de Mayo, dos clubes del mismo barrio, se fusionan con Rubio Ñu para
          mantenerlo con vida.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">1963</div>
        <div>
          <h3>Campeón invicto</h3>
          <p>Gana la segunda división sin perder un partido y supera la promoción para volver a
          Primera.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">2009</div>
        <div>
          <h3>El regreso y el mejor puesto</h3>
          <p>Vuelve a la División de Honor tras veintiocho años de ausencia y firma su mejor
          campaña histórica en la máxima categoría.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">2025</div>
        <div>
          <h3>Campeón de la División Intermedia</h3>
          <p>El club gana la segunda categoría del fútbol paraguayo y asciende a la División de Honor.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">2026</div>
        <div>
          <h3>Temporada en Primera</h3>
          <p>Rubio Ñu disputa el Apertura y el Clausura de la División de Honor.</p>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="seccion" id="estadio">
  <div class="marco">
    <h2 class="titulo-seccion">La Arboleda</h2>
    <p class="entrada">La cancha del club, en el mismo barrio donde se fundó. Acá juega Rubio Ñu
    de local todas las fechas del torneo. La visera lleva el nombre de Rubén Martin Ruiz Díaz
    Romero, presidente de la institución.</p>
    <figure class="figura-estadio">
      <img src="{base}assets/img/la-arboleda.webp"
           alt="Vista aérea del Estadio La Arboleda rodeado por las casas de Santísima Trinidad"
           loading="lazy" width="1500" height="843">
      <figcaption>
        <span>El estadio, encajado entre las calles del barrio.</span>
        <span><b>Santísima Trinidad</b>, Asunción</span>
      </figcaption>
    </figure>
    <dl class="datos-grilla">
      <div class="dato"><dt>Ubicación</dt><dd>Santísima Trinidad</dd></div>
      <div class="dato"><dt>Capacidad</dt><dd>8.000 personas</dd></div>
      <div class="dato"><dt>Superficie</dt><dd>Césped natural</dd></div>
      <div class="dato"><dt>Inauguración</dt><dd>Por confirmar</dd></div>
    </dl>
    <div class="tira-fotos">
      <figure>
        <img src="{base}assets/img/estadio-visera.webp" alt="Visera Rubén Martín Ruiz Díaz, en el estadio La Arboleda" loading="lazy" width="900" height="600">
        <figcaption>La visera Rubén Martín Ruiz Díaz, por el presidente del club.</figcaption>
      </figure>
      <figure>
        <img src="{base}assets/img/estadio-corner.webp" alt="Banderín de córner y césped del estadio La Arboleda" loading="lazy" width="900" height="600">
        <figcaption>El córner, antes de que llegue la gente.</figcaption>
      </figure>
      <figure>
        <img src="{base}assets/img/estadio-linea.webp" alt="Línea de cal hacia la tribuna albiverde de La Arboleda" loading="lazy" width="900" height="600">
        <figcaption>La tribuna, pintada de blanco y verde.</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="seccion seccion-gris" id="inferiores">
  <div class="marco">
    <h2 class="titulo-seccion">Las inferiores</h2>
    <p class="entrada">La Arboleda es donde el club juega los domingos. Las inferiores trabajan en
    otro lado: en el CARDIF, el Centro de Alto Rendimiento de las Divisiones Formativas de la Asociación
    Paraguaya de Fútbol, donde se forman bajo la metodología de la APF.</p>
    <figure class="figura-estadio">
      <img src="{base}assets/img/cardif.webp"
           alt="Vista aérea del CARDIF, Centro de Alto Rendimiento de las Divisiones Formativas de la APF"
           loading="lazy" width="1600" height="1067">
      <figcaption>
        <span>El CARDIF, Centro de Alto Rendimiento de las Divisiones Formativas.</span>
        <span><b>Asociación Paraguaya de Fútbol</b></span>
      </figcaption>
    </figure>
  </div>
</section>

<section class="seccion" id="palmares">
  <div class="marco dos-columnas">
    <div>
      <h2 class="titulo-seccion">Palmarés</h2>
      <p class="entrada">La historia de Rubio Ñu no es una vitrina de títulos grandes: es la de un
      club que se cayó muchas veces y siempre volvió a subir.</p>
      <ul class="lista-marca">
        <li>Campeón de la División Intermedia en 1926, 1941, 1954, 1961, 1963, 1972, 2008 y 2025.</li>
        <li>Mejor campaña en la máxima categoría: cuarto puesto en el Clausura 2009.</li>
        <li>Premio Guaraní al mejor equipo del año, 2009.</li>
      </ul>
    </div>
    <div>
      <h3 style="font-size:1.1rem;color:var(--verde-hondo);margin-bottom:1rem">Actividades del club</h3>
      <ul class="lista-marca">
        <li>Fútbol profesional</li>
        <li>Fútbol senior y amateur</li>
        <li>Escuela de fútbol</li>
        <li>Futsal</li>
        <li>Fútbol de playa</li>
        <li>Pádel</li>
      </ul>
    </div>
  </div>
</section>

<section class="seccion seccion-gris" id="comision">
  <div class="marco">
    <h2 class="titulo-seccion">Comisión directiva</h2>
    <p class="entrada">Los dirigentes que conducen la institución.</p>
    <figure class="figura-estadio">
      <img src="{base}assets/img/comision-directiva.webp"
           alt="La comisión directiva del Club Rubio Ñu, reunida en el estadio La Arboleda"
           loading="lazy" width="1600" height="1004">
      <figcaption>
        <span>La comisión directiva, en La Arboleda.</span>
        <span>Bajo la <b>visera Rubén Martín Ruiz Díaz</b></span>
      </figcaption>
    </figure>
    <p class="entrada" style="margin-top:1.5rem">Comisión directiva del período <b>2024 / 2026</b>.</p>
    <dl class="nomina">
      <div><dt>Presidente</dt><dd>Rubén Martin Ruiz Díaz Romero</dd></div>
      <div><dt>Vicepresidente 1º</dt><dd>Víctor Fredi Riveros López</dd></div>
      <div><dt>Vicepresidente 2º</dt><dd>Juan Ramón Fleitas González</dd></div>
      <div><dt>Secretario</dt><dd>Guido Jovino Mendoza Garcete</dd></div>
      <div><dt>Tesorero</dt><dd>Jorge Del Pilar Cubilla González</dd></div>
    </dl>
    <div class="nomina-columnas">
      <div>
        <h3>Miembros titulares</h3>
        <ol>
          <li>Néstor Rubén Jara Pintos</li>
          <li>Henry Dennis Ruiz Díaz Cáceres</li>
          <li>Rodney David Apodaca Paredes</li>
          <li>Rodrigo Augusto Talia Apodaca</li>
          <li>Darío Alberto Ocampos Almirón</li>
          <li>Gustavo Adolfo Rivarola Paredes</li>
          <li>Carlos Alberto Gamarra Pavón</li>
        </ol>
      </div>
      <div>
        <h3>Miembros suplentes</h3>
        <ol>
          <li>Ariel Eduardo Álvarez Acosta</li>
          <li>Santiago Joel Retaíno Buisines</li>
          <li>José Julián Burgos Valinoti</li>
        </ol>
      </div>
    </div>
    <div class="nomina-columnas">
      <div>
        <h3>Síndico titular</h3>
        <ol>
          <li>Carlos Gerardo Dávalos Insfrán</li>
        </ol>
      </div>
      <div>
        <h3>Síndico suplente</h3>
        <ol>
          <li>José Dolores Ríos Rodríguez</li>
        </ol>
      </div>
    </div>
    <div class="nomina-columnas">
      <div>
        <h3>TEI · Titulares</h3>
        <ol>
          <li>Víctor Hugo Bejarano Almirón</li>
          <li>Nery Francisco Villalba Solís</li>
          <li>Darío Quiñonez Martínez</li>
        </ol>
      </div>
      <div>
        <h3>TEI · Suplentes</h3>
        <ol>
          <li>Justo Pastor Apodaca Paredes</li>
          <li>Carlos Alberto Ruiz Díaz Romero</li>
          <li>Nelson Andrés Hastedt Ruiz Díaz</li>
        </ol>
      </div>
    </div>
  </div>
</section>
"""

ES["plantel"] = """
<section class="portada-foto portada-interior">
  <div class="fondo" style="background-image:url('{base}assets/img/plantel-2026.webp')"></div>
  <div class="velo"></div>
  <div class="marco">
    <div class="placa">
      <img src="{base}assets/img/escudo.png" alt="">
      <div>
        <p class="placa-kicker">Temporada 2026</p>
        <h1>Plantel</h1>
        <p class="lema">Los jugadores y el cuerpo técnico de la temporada.</p>
      </div>
    </div>
    <div class="pie-foto">
      <span>El plantel completo, con el cuerpo técnico</span>
      <span class="sello">División de Honor</span>
    </div>
  </div>
</section>
<div class="filete bastones"></div>

<section class="seccion">
  <div class="marco">
    <div data-plantel><p class="cargando">Cargando plantel…</p></div>
  </div>
</section>

<section class="seccion seccion-gris">
  <div class="marco">
    <h2 class="titulo-seccion">Cuerpo técnico</h2>
    <div data-cuerpo-tecnico><p class="cargando">Cargando…</p></div>
  </div>
</section>

<section class="seccion seccion-tinta textura-diagonal">
  <div class="marco">
    <h2 class="titulo-seccion">El equipo en cancha</h2>
    <p class="entrada">Imágenes de la temporada en la División de Honor.</p>
    <div class="galeria-accion">
      <img src="{base}assets/img/accion-remate.webp" alt="Jugador de Rubio Ñu por rematar al arco" loading="lazy" width="760" height="950">
      <img src="{base}assets/img/accion-festejo.webp" alt="Jugadores de Rubio Ñu abrazados festejando un gol" loading="lazy" width="760" height="950">
      <img src="{base}assets/img/accion-grito.webp" alt="Jugador de Rubio Ñu celebrando y señalando hacia la tribuna" loading="lazy" width="760" height="950">
      <img src="{base}assets/img/accion-cabezazo.webp" alt="Disputa aérea dentro del área en La Arboleda" loading="lazy" width="760" height="950">
      <img src="{base}assets/img/accion-duelo.webp" alt="Duelo por la pelota, en blanco y negro" loading="lazy" width="760" height="950">
      <img src="{base}assets/img/accion-conduccion.webp" alt="Jugador de Rubio Ñu conduciendo la pelota" loading="lazy" width="760" height="950">
    </div>
  </div>
</section>
"""

ES["fixture"] = """
<section class="portada-foto portada-interior">
  <div class="fondo" style="background-image:url('{base}assets/img/once-arboleda.webp')"></div>
  <div class="velo"></div>
  <div class="marco">
    <div class="placa">
      <img src="{base}assets/img/escudo.png" alt="">
      <div>
        <p class="placa-kicker">Clausura 2026</p>
        <h1>Fixture y tabla</h1>
        <p class="lema">Resultados, próximos partidos y posiciones de la División de Honor.</p>
      </div>
    </div>
    <div class="pie-foto">
      <span>Los once, antes de empezar, en <b>La Arboleda</b></span>
      <span class="sello">Copa de Primera</span>
    </div>
  </div>
</section>
<div class="filete bastones"></div>

<section class="franja-partido">
  <div class="marco partido-grilla">
    <div data-ultimo><p class="cargando">Cargando resultado…</p></div>
    <div class="divisoria" aria-hidden="true"></div>
    <div data-proximos><p class="cargando">Cargando calendario…</p></div>
  </div>
</section>

<section class="seccion" id="tabla">
  <div class="marco">
    <h2 class="titulo-seccion">Tabla de posiciones</h2>
    <p class="entrada">División de Honor, Torneo Clausura 2026.</p>
    <div data-tabla="completa"><p class="cargando">Cargando tabla…</p></div>
  </div>
</section>

<section class="seccion seccion-gris">
  <div class="marco">
    <h2 class="titulo-seccion">Calendario completo</h2>
    <p class="entrada">Los próximos partidos del albiverde, en el Clausura y en la Copa Paraguay.</p>
    <div data-calendario><p class="cargando">Cargando calendario…</p></div>
  </div>
</section>
"""

ES["noticias"] = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="">
    <div>
      <h1>Noticias</h1>
      <p class="portada-bajada">Novedades del primer equipo, las inferiores y la institución.</p>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <div data-noticias><p class="cargando">Cargando noticias…</p></div>
  </div>
</section>
"""

ES["socios"] = """
<section class="portada-foto portada-interior">
  <div class="fondo" style="background-image:url('{base}assets/img/equipo-visitante.webp')"></div>
  <div class="velo"></div>
  <div class="marco">
    <div class="placa">
      <img src="{base}assets/img/escudo.png" alt="">
      <div>
        <p class="placa-kicker">Sé parte del club</p>
        <h1>Hacete socio</h1>
        <p class="lema">Sostené al club todo el año y entrá a La Arboleda cada fecha.</p>
      </div>
    </div>
    <div class="pie-foto">
      <span>El albiverde, de visitante</span>
      <span class="sello">Desde 1913</span>
    </div>
  </div>
</section>
<div class="filete bastones"></div>

<section class="seccion">
  <div class="marco">
    <h2 class="titulo-seccion">Categorías</h2>
    <p class="entrada">Las cuotas, los beneficios y la forma de pago se confirman con la
    administración del club antes de publicar esta página.</p>
    <dl class="datos-grilla">
      <div class="dato"><dt>Socio activo</dt><dd>Cuota a confirmar</dd></div>
      <div class="dato"><dt>Socio menor</dt><dd>Cuota a confirmar</dd></div>
      <div class="dato"><dt>Socio adherente</dt><dd>Cuota a confirmar</dd></div>
      <div class="dato"><dt>Socio vitalicio</dt><dd>Cuota a confirmar</dd></div>
    </dl>
  </div>
</section>

<section class="seccion seccion-gris">
  <div class="marco">
    <h2 class="titulo-seccion">Asociate</h2>
    <p class="entrada">Dejá tus datos y la administración se comunica para completar el alta.</p>
    <form class="formulario" method="post" action="#">
      <div class="campo">
        <label for="s-nombre">Nombre y apellido</label>
        <input id="s-nombre" name="nombre" type="text" required>
      </div>
      <div class="campo">
        <label for="s-ci">Cédula de identidad</label>
        <input id="s-ci" name="ci" type="text" required>
      </div>
      <div class="campo">
        <label for="s-mail">Correo electrónico</label>
        <input id="s-mail" name="email" type="email" required>
      </div>
      <div class="campo">
        <label for="s-tel">Teléfono</label>
        <input id="s-tel" name="telefono" type="tel">
      </div>
      <div class="campo">
        <label for="s-cat">Categoría</label>
        <select id="s-cat" name="categoria">
          <option>Socio activo</option>
          <option>Socio menor</option>
          <option>Socio adherente</option>
          <option>Socio vitalicio</option>
        </select>
      </div>
      <div><button class="boton" type="submit">Enviar solicitud</button></div>
    </form>
  </div>
</section>
"""

ES["contacto"] = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="">
    <div>
      <h1>Contacto</h1>
      <p class="portada-bajada">Sede, prensa, sponsors y administración.</p>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <h2 class="titulo-seccion">Dónde encontrarnos</h2>
    <dl class="datos-grilla">
      <div class="dato"><dt>Sede</dt><dd>Santísima Trinidad, Asunción</dd></div>
      <div class="dato"><dt>Teléfono</dt><dd>Por confirmar</dd></div>
      <div class="dato"><dt>Correo</dt><dd>Por confirmar</dd></div>
      <div class="dato"><dt>Horarios</dt><dd>Por confirmar</dd></div>
    </dl>
    <div style="margin-top:2rem">
      <h3 style="font-size:1.1rem;color:var(--verde-hondo);margin-bottom:0.75rem">Seguinos</h3>
      <p class="entrada" style="margin-bottom:1rem">Las novedades del día a día salen primero por
      las redes del club.</p>
{bloque_redes("redes-claro")}
    </div>
  </div>
</section>

<section class="seccion seccion-gris" id="prensa">
  <div class="marco">
    <h2 class="titulo-seccion">Escribinos</h2>
    <form class="formulario" method="post" action="#">
      <div class="campo">
        <label for="c-nombre">Nombre</label>
        <input id="c-nombre" name="nombre" type="text" required>
      </div>
      <div class="campo">
        <label for="c-mail">Correo electrónico</label>
        <input id="c-mail" name="email" type="email" required>
      </div>
      <div class="campo">
        <label for="c-motivo">Motivo</label>
        <select id="c-motivo" name="motivo">
          <option>Consulta general</option>
          <option>Prensa</option>
          <option>Sponsors y comercial</option>
          <option>Inferiores y captación</option>
        </select>
      </div>
      <div class="campo">
        <label for="c-mensaje">Mensaje</label>
        <textarea id="c-mensaje" name="mensaje" required></textarea>
      </div>
      <div><button class="boton" type="submit">Enviar mensaje</button></div>
    </form>
  </div>
</section>
"""

# ================================================================ CONTENIDO EN
EN = {}

EN["index"] = """
<section class="portada-foto">
  <div class="fondo" style="background-image:url('{base}assets/img/portada-arboleda.webp')"></div>
  <div class="velo"></div>
  <div class="marco">
    <div class="placa">
      <img src="{base}assets/img/escudo.png" alt="Club Rubio Ñu crest">
      <div>
        <p class="placa-kicker">Santísima Trinidad · Asunción</p>
        <h1>Rubio Ñu</h1>
        <p class="lema">A hundred and thirteen years on the same block. White for purity, green for
        hope: the albiverde is back in the top flight.</p>
      </div>
    </div>
    <div class="pie-foto">
      <span>Estadio <b>La Arboleda</b>, in the barrio where the club was founded in <b>1913</b></span>
      <span class="sello">Albiverde · Ñuenses · Laureado</span>
    </div>
  </div>
</section>
<div class="filete bastones"></div>

<section class="franja-partido">
  <div class="marco partido-grilla">
    <div data-ultimo><p class="cargando">Loading result…</p></div>
    <div class="divisoria" aria-hidden="true"></div>
    <div data-proximos><p class="cargando">Loading fixtures…</p></div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <div class="cabezal-seccion">
      <div>
        <h2 class="titulo-seccion">How the Clausura stands</h2>
        <p class="entrada">First Division standings, updated matchday by matchday.</p>
      </div>
      <a class="enlace-mas" href="fixture.html#tabla">Full table and fixtures</a>
    </div>
    <div data-tabla="resumida"><p class="cargando">Loading table…</p></div>
  </div>
</section>

<section class="banda-foto">
  <div class="fondo" style="background-image:url('{base}assets/img/barrio-trinidad.webp')"></div>
  <div class="velo"></div>
  <div class="marco">
    <p class="banda-cita">The club never left the neighbourhood
      <span>Santísima Trinidad, Asunción, since 1913.</span>
    </p>
  </div>
</section>

<section class="seccion seccion-tinta textura-diagonal">
  <div class="marco">
    <h2 class="titulo-seccion">The club always comes back</h2>
    <p class="entrada">Rubio Ñu was born in 1913 in Santísima Trinidad and never left the
    neighbourhood. Resilience is what defines its history.</p>
    <div class="hitos">
      <article class="hito">
        <div class="hito-anio">1913</div>
        <div>
          <h3>The founding</h3>
          <p>A group of boys, all under eighteen, founds the club on 24 August and names it after
          the field where the children of Acosta Ñu were believed to have fought.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">1936</div>
        <div>
          <h3>The refounding</h3>
          <p>After twenty-three years, Itá Ybaté and Flor de Mayo, two clubs from the same
          neighbourhood, merge with Rubio Ñu to keep it alive.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">2025</div>
        <div>
          <h3>Second division champions</h3>
          <p>The team wins the División Intermedia and seals promotion to the top flight.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">2026</div>
        <div>
          <h3>Back in the top flight</h3>
          <p>Rubio Ñu competes again against the biggest clubs in the country, with La Arboleda as
          its home ground.</p>
        </div>
      </article>
    </div>
    <p style="margin-top:2rem"><a class="enlace-mas" href="club.html">The full history</a></p>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <div class="cabezal-seccion">
      <h2 class="titulo-seccion">News</h2>
      <a class="enlace-mas" href="noticias.html">See all</a>
    </div>
    <div data-noticias data-limite="3"><p class="cargando">Loading news…</p></div>
  </div>
</section>

<section class="banda-foto">
  <div class="fondo" style="background-image:url('{base}assets/img/tribuna-arboleda.webp')"></div>
  <div class="velo"></div>
  <div class="marco">
    <p class="banda-cita">Every other week, this stand fills up
      <span>La Arboleda, Santísima Trinidad.</span>
    </p>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <div class="accion">
      <div>
        <h2>Become a member</h2>
        <p>Members keep the club going all year: they get into La Arboleda, pick their seat and
        vote at the general assembly.</p>
      </div>
      <div class="botonera">
        <a class="boton" href="socios.html">See the categories</a>
        <a class="boton boton-borde" href="contacto.html">Get in touch</a>
      </div>
    </div>
  </div>
</section>
"""

EN["club"] = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="">
    <div>
      <h1>The club</h1>
      <p class="portada-bajada">A neighbourhood club with more than a century of history.</p>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="marco dos-columnas">
    <div>
      <h2 class="titulo-seccion">A neighbourhood club with more than a century of history</h2>
      <p>Rubio Ñu was born on 24 August 1913 in the neighbourhood of Santísima Trinidad, Asunción,
      founded by a group of friends who chose white and green as the club colours: white for
      purity, green for hope. That combination gave the club its nickname, albiverde.</p>
      <p>In 1936, after twenty-three years, two clubs from the same neighbourhood, Itá Ybaté and
      Flor de Mayo, merged with Rubio Ñu to keep it alive. That refounding marked the club: always
      coming back, even after the losses.</p>
      <p>The club plays its home matches at Estadio La Arboleda, and holds a historic rivalry with
      Sportivo Trinidense in the Clásico de Trinidad. Its players and supporters are known as
      ñuenses.</p>
    </div>
    <div>
      <h3 style="font-size:1.1rem;color:var(--verde-hondo);margin-bottom:1rem">Values</h3>
      <ul class="lista-marca">
        <li>Resilience: the club always comes back.</li>
        <li>Neighbourhood identity, in Santísima Trinidad.</li>
        <li>Developing young talent.</li>
        <li>South American reach.</li>
      </ul>
    </div>
  </div>
</section>

<section class="seccion seccion-tinta" id="nombre">
  <div class="marco dos-columnas">
    <div>
      <h2 class="titulo-seccion">Where the name comes from</h2>
      <p style="color:rgba(255,255,255,0.78)">On 16 August 1869, during the War of the Triple
      Alliance, a Paraguayan army largely made up of children held out at Barrero Grande, today the
      city of Eusebio Ayala. It is remembered as the battle of the children.</p>
      <p style="color:rgba(255,255,255,0.78)">For decades that battle was called Rubio Ñu. The
      mistake came from a poem by the priest Juan B. Tournedou and was repeated until 1948, when
      the historian Andrés Aguirre secured a decree renaming it Acosta Ñu, after the fields where
      it actually took place, and making 16 August Children's Day.</p>
      <p style="color:rgba(255,255,255,0.78)">The club was founded in 1913, thirty-five years
      before that correction. A group of boys from Santísima Trinidad, all under eighteen, named
      their club after the battle as it was known at the time, and chose white and green in tribute
      to those children. <em>Ñu</em> means field in Guaraní.</p>
    </div>
    <div>
      <p class="cita-mision" style="color:var(--verde);max-width:22ch">Boys who named their club
      after other boys</p>
      <p style="color:rgba(255,255,255,0.6);font-size:0.88rem;margin-top:1.25rem">This section is
      pending validation by the club's historical archive.</p>
    </div>
  </div>
  <div class="marco">
    <figure class="figura-estadio figura-ancha">
      <img src="{base}assets/img/ninos-martires.webp"
           alt="Monument to the Child Martyrs of Acosta Ñu, with the Paraguayan flag cut in sheet metal and the silhouettes of a soldier and a child"
           loading="lazy" width="1600" height="1066">
      <figcaption>
        <span>Monument to the Child Martyrs, in Eusebio Ayala, where the battle took place.</span>
        <span><b>16 August</b>, Children's Day in Paraguay</span>
      </figcaption>
    </figure>
  </div>
</section>

<section class="seccion seccion-verde">
  <div class="marco dos-columnas">
    <p class="cita-mision">A historic neighbourhood club that honours more than a hundred years of
    resilience and aims to establish itself in the top flight.</p>
    <p class="entrada" style="margin:0">The club's mission is to develop and export Paraguayan and
    South American talent, sustaining sporting and institutional growth without losing the identity
    of Santísima Trinidad.</p>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <h2 class="titulo-seccion">Club facts</h2>
    <dl class="datos-grilla">
      <div class="dato"><dt>Founded</dt><dd>24 August 1913</dd></div>
      <div class="dato"><dt>Neighbourhood</dt><dd>Santísima Trinidad</dd></div>
      <div class="dato"><dt>City</dt><dd>Asunción, Paraguay</dd></div>
      <div class="dato"><dt>Stadium</dt><dd>La Arboleda</dd></div>
      <div class="dato"><dt>Nicknames</dt><dd>Albiverde, Ñuenses, Laureado</dd></div>
      <div class="dato"><dt>Derby</dt><dd>Sportivo Trinidense</dd></div>
      <div class="dato"><dt>2026 division</dt><dd>First Division</dd></div>
      <div class="dato"><dt>Association</dt><dd>APF</dd></div>
    </dl>
  </div>
</section>

<section class="seccion seccion-tinta textura-diagonal">
  <div class="marco">
    <h2 class="titulo-seccion">Timeline</h2>
    <div class="hitos">
      <article class="hito">
        <div class="hito-anio">1913</div>
        <div>
          <h3>The founding</h3>
          <p>A group of boys under eighteen founds the club on 24 August in Santísima Trinidad, in
          tribute to the children of Acosta Ñu, and chooses white and green.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">1926</div>
        <div>
          <h3>First title</h3>
          <p>Rubio Ñu wins the División Intermedia for the first time and moves up to the top
          division.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">1927</div>
        <div>
          <h3>Top-flight debut</h3>
          <p>The club plays its first season in the highest division of Paraguayan football.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">1932</div>
        <div>
          <h3>The Chaco War</h3>
          <p>The club suspends its activities: officials and athletes join the army in the field.
          It resumes once the war is over.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">1936</div>
        <div>
          <h3>The refounding</h3>
          <p>Itá Ybaté and Flor de Mayo, two clubs from the same neighbourhood, merge with Rubio Ñu
          to keep it alive.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">1963</div>
        <div>
          <h3>Unbeaten champions</h3>
          <p>The club wins the second division without losing a match and comes through the
          play-off to return to the top flight.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">2009</div>
        <div>
          <h3>The return, and the best finish</h3>
          <p>Rubio Ñu returns to the top flight after twenty-eight years away and records its best
          ever campaign in the first division.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">2025</div>
        <div>
          <h3>División Intermedia champions</h3>
          <p>The club wins the Paraguayan second division and earns promotion to the top flight.</p>
        </div>
      </article>
      <article class="hito">
        <div class="hito-anio">2026</div>
        <div>
          <h3>Top-flight season</h3>
          <p>Rubio Ñu plays the Apertura and Clausura tournaments of the First Division.</p>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="seccion" id="estadio">
  <div class="marco">
    <h2 class="titulo-seccion">La Arboleda</h2>
    <p class="entrada">The club's ground, in the same neighbourhood where it was founded. Rubio Ñu
    plays every home match here. The main stand roof carries the name of Rubén Martin Ruiz Díaz
    Romero, the club's president.</p>
    <figure class="figura-estadio">
      <img src="{base}assets/img/la-arboleda.webp"
           alt="Aerial view of Estadio La Arboleda surrounded by the houses of Santísima Trinidad"
           loading="lazy" width="1500" height="843">
      <figcaption>
        <span>The ground, wedged between the streets of the barrio.</span>
        <span><b>Santísima Trinidad</b>, Asunción</span>
      </figcaption>
    </figure>
    <dl class="datos-grilla">
      <div class="dato"><dt>Location</dt><dd>Santísima Trinidad</dd></div>
      <div class="dato"><dt>Capacity</dt><dd>8,000</dd></div>
      <div class="dato"><dt>Surface</dt><dd>Natural grass</dd></div>
      <div class="dato"><dt>Opened</dt><dd>To be confirmed</dd></div>
    </dl>
    <div class="tira-fotos">
      <figure>
        <img src="{base}assets/img/estadio-visera.webp" alt="The Rubén Martín Ruiz Díaz stand roof at La Arboleda" loading="lazy" width="900" height="600">
        <figcaption>The Rubén Martín Ruiz Díaz stand roof, named after the club president.</figcaption>
      </figure>
      <figure>
        <img src="{base}assets/img/estadio-corner.webp" alt="Corner flag and pitch at La Arboleda" loading="lazy" width="900" height="600">
        <figcaption>The corner, before the crowd arrives.</figcaption>
      </figure>
      <figure>
        <img src="{base}assets/img/estadio-linea.webp" alt="Touchline leading to the green and white stand at La Arboleda" loading="lazy" width="900" height="600">
        <figcaption>The stand, painted white and green.</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="seccion seccion-gris" id="inferiores">
  <div class="marco">
    <h2 class="titulo-seccion">The academy</h2>
    <p class="entrada">La Arboleda is where the club plays on Sundays. The youth teams work
    somewhere else: at the CARDIF, the Paraguayan Football Association's high-performance centre for
    youth development, where they train under the APF methodology.</p>
    <figure class="figura-estadio">
      <img src="{base}assets/img/cardif.webp"
           alt="Aerial view of the CARDIF, the Paraguayan Football Association training complex"
           loading="lazy" width="1600" height="1067">
      <figcaption>
        <span>The CARDIF, the APF high-performance centre for youth football.</span>
        <span><b>Paraguayan Football Association</b></span>
      </figcaption>
    </figure>
  </div>
</section>

<section class="seccion" id="palmares">
  <div class="marco dos-columnas">
    <div>
      <h2 class="titulo-seccion">Honours</h2>
      <p class="entrada">Rubio Ñu's history is not a cabinet full of major trophies: it is the
      story of a club that fell many times and always climbed back.</p>
      <ul class="lista-marca">
        <li>División Intermedia champions in 1926, 1941, 1954, 1961, 1963, 1972, 2008 and 2025.</li>
        <li>Best top-flight campaign: fourth place in the 2009 Clausura.</li>
        <li>Premio Guaraní, team of the year, 2009.</li>
      </ul>
    </div>
    <div>
      <h3 style="font-size:1.1rem;color:var(--verde-hondo);margin-bottom:1rem">Club activities</h3>
      <ul class="lista-marca">
        <li>Professional football</li>
        <li>Senior and amateur football</li>
        <li>Football school</li>
        <li>Futsal</li>
        <li>Beach football</li>
        <li>Padel</li>
      </ul>
    </div>
  </div>
</section>

<section class="seccion seccion-gris" id="comision">
  <div class="marco">
    <h2 class="titulo-seccion">Board of directors</h2>
    <p class="entrada">The officials who run the club.</p>
    <figure class="figura-estadio">
      <img src="{base}assets/img/comision-directiva.webp"
           alt="The board of directors of Club Rubio Ñu, gathered at La Arboleda"
           loading="lazy" width="1600" height="1004">
      <figcaption>
        <span>The board of directors, at La Arboleda.</span>
        <span>Under the <b>Rubén Martín Ruiz Díaz stand</b></span>
      </figcaption>
    </figure>
    <p class="entrada" style="margin-top:1.5rem">Board of directors for the <b>2024 / 2026</b> term.</p>
    <dl class="nomina">
      <div><dt>President</dt><dd>Rubén Martin Ruiz Díaz Romero</dd></div>
      <div><dt>First vice-president</dt><dd>Víctor Fredi Riveros López</dd></div>
      <div><dt>Second vice-president</dt><dd>Juan Ramón Fleitas González</dd></div>
      <div><dt>Secretary</dt><dd>Guido Jovino Mendoza Garcete</dd></div>
      <div><dt>Treasurer</dt><dd>Jorge Del Pilar Cubilla González</dd></div>
    </dl>
    <div class="nomina-columnas">
      <div>
        <h3>Full members</h3>
        <ol>
          <li>Néstor Rubén Jara Pintos</li>
          <li>Henry Dennis Ruiz Díaz Cáceres</li>
          <li>Rodney David Apodaca Paredes</li>
          <li>Rodrigo Augusto Talia Apodaca</li>
          <li>Darío Alberto Ocampos Almirón</li>
          <li>Gustavo Adolfo Rivarola Paredes</li>
          <li>Carlos Alberto Gamarra Pavón</li>
        </ol>
      </div>
      <div>
        <h3>Alternate members</h3>
        <ol>
          <li>Ariel Eduardo Álvarez Acosta</li>
          <li>Santiago Joel Retaíno Buisines</li>
          <li>José Julián Burgos Valinoti</li>
        </ol>
      </div>
    </div>
    <div class="nomina-columnas">
      <div>
        <h3>Auditor</h3>
        <ol>
          <li>Carlos Gerardo Dávalos Insfrán</li>
        </ol>
      </div>
      <div>
        <h3>Alternate auditor</h3>
        <ol>
          <li>José Dolores Ríos Rodríguez</li>
        </ol>
      </div>
    </div>
    <div class="nomina-columnas">
      <div>
        <h3>TEI · Titulares</h3>
        <ol>
          <li>Víctor Hugo Bejarano Almirón</li>
          <li>Nery Francisco Villalba Solís</li>
          <li>Darío Quiñonez Martínez</li>
        </ol>
      </div>
      <div>
        <h3>TEI · Suplentes</h3>
        <ol>
          <li>Justo Pastor Apodaca Paredes</li>
          <li>Carlos Alberto Ruiz Díaz Romero</li>
          <li>Nelson Andrés Hastedt Ruiz Díaz</li>
        </ol>
      </div>
    </div>
  </div>
</section>
"""

EN["plantel"] = """
<section class="portada-foto portada-interior">
  <div class="fondo" style="background-image:url('{base}assets/img/plantel-2026.webp')"></div>
  <div class="velo"></div>
  <div class="marco">
    <div class="placa">
      <img src="{base}assets/img/escudo.png" alt="">
      <div>
        <p class="placa-kicker">2026 season</p>
        <h1>Squad</h1>
        <p class="lema">The players and coaching staff for the season.</p>
      </div>
    </div>
    <div class="pie-foto">
      <span>The full squad, with the coaching staff</span>
      <span class="sello">First Division</span>
    </div>
  </div>
</section>
<div class="filete bastones"></div>

<section class="seccion">
  <div class="marco">
    <div data-plantel><p class="cargando">Loading squad…</p></div>
  </div>
</section>

<section class="seccion seccion-gris">
  <div class="marco">
    <h2 class="titulo-seccion">Coaching staff</h2>
    <div data-cuerpo-tecnico><p class="cargando">Loading…</p></div>
  </div>
</section>

<section class="seccion seccion-tinta textura-diagonal">
  <div class="marco">
    <h2 class="titulo-seccion">The team on the pitch</h2>
    <p class="entrada">Images from the season in the First Division.</p>
    <div class="galeria-accion">
      <img src="{base}assets/img/accion-remate.webp" alt="Rubio Ñu player about to shoot" loading="lazy" width="760" height="950">
      <img src="{base}assets/img/accion-festejo.webp" alt="Rubio Ñu players celebrating a goal together" loading="lazy" width="760" height="950">
      <img src="{base}assets/img/accion-grito.webp" alt="Rubio Ñu player celebrating and pointing to the stand" loading="lazy" width="760" height="950">
      <img src="{base}assets/img/accion-cabezazo.webp" alt="Aerial duel inside the box at La Arboleda" loading="lazy" width="760" height="950">
      <img src="{base}assets/img/accion-duelo.webp" alt="Battle for the ball, in black and white" loading="lazy" width="760" height="950">
      <img src="{base}assets/img/accion-conduccion.webp" alt="Rubio Ñu player running with the ball" loading="lazy" width="760" height="950">
    </div>
  </div>
</section>
"""

EN["fixture"] = """
<section class="portada-foto portada-interior">
  <div class="fondo" style="background-image:url('{base}assets/img/once-arboleda.webp')"></div>
  <div class="velo"></div>
  <div class="marco">
    <div class="placa">
      <img src="{base}assets/img/escudo.png" alt="">
      <div>
        <p class="placa-kicker">Clausura 2026</p>
        <h1>Fixtures</h1>
        <p class="lema">Results, upcoming matches and First Division standings.</p>
      </div>
    </div>
    <div class="pie-foto">
      <span>The starting eleven at <b>La Arboleda</b></span>
      <span class="sello">Copa de Primera</span>
    </div>
  </div>
</section>
<div class="filete bastones"></div>

<section class="franja-partido">
  <div class="marco partido-grilla">
    <div data-ultimo><p class="cargando">Loading result…</p></div>
    <div class="divisoria" aria-hidden="true"></div>
    <div data-proximos><p class="cargando">Loading fixtures…</p></div>
  </div>
</section>

<section class="seccion" id="tabla">
  <div class="marco">
    <h2 class="titulo-seccion">League table</h2>
    <p class="entrada">First Division, Clausura 2026.</p>
    <div data-tabla="completa"><p class="cargando">Loading table…</p></div>
  </div>
</section>

<section class="seccion seccion-gris">
  <div class="marco">
    <h2 class="titulo-seccion">Full calendar</h2>
    <p class="entrada">Rubio Ñu's upcoming fixtures, in the Clausura and the Copa Paraguay.</p>
    <div data-calendario><p class="cargando">Loading calendar…</p></div>
  </div>
</section>
"""

EN["noticias"] = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="">
    <div>
      <h1>News</h1>
      <p class="portada-bajada">Updates from the first team, the academy and the club.</p>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <div data-noticias><p class="cargando">Loading news…</p></div>
  </div>
</section>
"""

EN["socios"] = """
<section class="portada-foto portada-interior">
  <div class="fondo" style="background-image:url('{base}assets/img/equipo-visitante.webp')"></div>
  <div class="velo"></div>
  <div class="marco">
    <div class="placa">
      <img src="{base}assets/img/escudo.png" alt="">
      <div>
        <p class="placa-kicker">Be part of the club</p>
        <h1>Membership</h1>
        <p class="lema">Support the club all year and get into La Arboleda every matchday.</p>
      </div>
    </div>
    <div class="pie-foto">
      <span>The albiverde, away from home</span>
      <span class="sello">Since 1913</span>
    </div>
  </div>
</section>
<div class="filete bastones"></div>

<section class="seccion">
  <div class="marco">
    <h2 class="titulo-seccion">Categories</h2>
    <p class="entrada">Fees, benefits and payment methods are confirmed with the club
    administration before this page is published.</p>
    <dl class="datos-grilla">
      <div class="dato"><dt>Full member</dt><dd>Fee to be confirmed</dd></div>
      <div class="dato"><dt>Junior member</dt><dd>Fee to be confirmed</dd></div>
      <div class="dato"><dt>Associate member</dt><dd>Fee to be confirmed</dd></div>
      <div class="dato"><dt>Life member</dt><dd>Fee to be confirmed</dd></div>
    </dl>
  </div>
</section>

<section class="seccion seccion-gris">
  <div class="marco">
    <h2 class="titulo-seccion">Sign up</h2>
    <p class="entrada">Leave your details and the club administration will get in touch to
    complete your membership.</p>
    <form class="formulario" method="post" action="#">
      <div class="campo">
        <label for="s-nombre">Full name</label>
        <input id="s-nombre" name="nombre" type="text" required>
      </div>
      <div class="campo">
        <label for="s-ci">ID number</label>
        <input id="s-ci" name="ci" type="text" required>
      </div>
      <div class="campo">
        <label for="s-mail">Email</label>
        <input id="s-mail" name="email" type="email" required>
      </div>
      <div class="campo">
        <label for="s-tel">Phone</label>
        <input id="s-tel" name="telefono" type="tel">
      </div>
      <div class="campo">
        <label for="s-cat">Category</label>
        <select id="s-cat" name="categoria">
          <option>Full member</option>
          <option>Junior member</option>
          <option>Associate member</option>
          <option>Life member</option>
        </select>
      </div>
      <div><button class="boton" type="submit">Send request</button></div>
    </form>
  </div>
</section>
"""

EN["contacto"] = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="">
    <div>
      <h1>Contact</h1>
      <p class="portada-bajada">Club offices, press, sponsors and administration.</p>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <h2 class="titulo-seccion">Where to find us</h2>
    <dl class="datos-grilla">
      <div class="dato"><dt>Offices</dt><dd>Santísima Trinidad, Asunción</dd></div>
      <div class="dato"><dt>Phone</dt><dd>To be confirmed</dd></div>
      <div class="dato"><dt>Email</dt><dd>To be confirmed</dd></div>
      <div class="dato"><dt>Opening hours</dt><dd>To be confirmed</dd></div>
    </dl>
    <div style="margin-top:2rem">
      <h3 style="font-size:1.1rem;color:var(--verde-hondo);margin-bottom:0.75rem">Follow us</h3>
      <p class="entrada" style="margin-bottom:1rem">Day-to-day news goes out on the club's social
      channels first.</p>
{bloque_redes("redes-claro")}
    </div>
  </div>
</section>

<section class="seccion seccion-gris" id="prensa">
  <div class="marco">
    <h2 class="titulo-seccion">Write to us</h2>
    <form class="formulario" method="post" action="#">
      <div class="campo">
        <label for="c-nombre">Name</label>
        <input id="c-nombre" name="nombre" type="text" required>
      </div>
      <div class="campo">
        <label for="c-mail">Email</label>
        <input id="c-mail" name="email" type="email" required>
      </div>
      <div class="campo">
        <label for="c-motivo">Subject</label>
        <select id="c-motivo" name="motivo">
          <option>General enquiry</option>
          <option>Press</option>
          <option>Sponsorship and commercial</option>
          <option>Academy and scouting</option>
        </select>
      </div>
      <div class="campo">
        <label for="c-mensaje">Message</label>
        <textarea id="c-mensaje" name="mensaje" required></textarea>
      </div>
      <div><button class="boton" type="submit">Send message</button></div>
    </form>
  </div>
</section>
"""

CONTENIDO = {"es": ES, "en": EN}


def construir():
    os.makedirs(os.path.join(BASE, "en"), exist_ok=True)
    for idioma in IDIOMAS:
        base = prefijo(idioma)
        for pagina in PAGINAS:
            cuerpo = CONTENIDO[idioma][pagina].replace("{base}", base)
            cuerpo = cuerpo.replace('{bloque_redes("redes-claro")}', bloque_redes("redes-claro"))
            html = cabecera(idioma, pagina) + cuerpo + pie(idioma)
            with open(ruta_salida(idioma, pagina), "w", encoding="utf-8") as f:
                f.write(html)
        print(idioma, "→", len(PAGINAS), "páginas")


if __name__ == "__main__":
    construir()
