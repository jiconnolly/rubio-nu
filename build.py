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
            ("EL CLUB", [("club", "Historia"), ("club#estadio", "La Arboleda"), ("plantel", "Plantel")]),
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
            ("THE CLUB", [("club", "History"), ("club#estadio", "La Arboleda"), ("plantel", "Squad")]),
            ("COMPETITION", [("fixture", "Fixtures"), ("fixture#tabla", "League table"), ("noticias", "News")]),
            ("GET INVOLVED", [("socios", "Membership"), ("contacto", "Contact"), ("contacto#prensa", "Press")]),
        ],
        "pie_legal": "© 2026 Club Rubio Ñu. All rights reserved.",
        "pie_liga": "Paraguayan Football Association · First Division",
    },
}

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
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="Escudo del Club Rubio Ñu">
    <div>
      <h1>Rubio Ñu</h1>
      <p class="portada-bajada">Blanco por la pureza, verde por la esperanza. El albiverde de
      Santísima Trinidad juega otra vez en la División de Honor del fútbol paraguayo.</p>
    </div>
  </div>
  <div class="marco portada-datos">
    <span>Fundado el <b>24 de agosto de 1913</b></span>
    <span>Estadio <b>La Arboleda</b></span>
    <span>Asunción, <b>Paraguay</b></span>
  </div>
</section>

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
          <p>Un grupo de amigos funda el club el 24 de agosto y elige el blanco y el verde:
          blanco por la pureza, verde por la esperanza. De ahí viene el apodo albiverde.</p>
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
          <p>Un grupo de amigos funda el club el 24 de agosto en Santísima Trinidad y elige el
          blanco y el verde como colores.</p>
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
    de local todas las fechas del torneo.</p>
    <dl class="datos-grilla">
      <div class="dato"><dt>Ubicación</dt><dd>Santísima Trinidad</dd></div>
      <div class="dato"><dt>Capacidad</dt><dd>Por confirmar</dd></div>
      <div class="dato"><dt>Superficie</dt><dd>Césped natural</dd></div>
      <div class="dato"><dt>Inauguración</dt><dd>Por confirmar</dd></div>
    </dl>
  </div>
</section>

<section class="seccion seccion-gris" id="comision">
  <div class="marco">
    <h2 class="titulo-seccion">Comisión directiva</h2>
    <p class="entrada">La nómina completa de la comisión directiva se publica en esta página.</p>
    <div class="vacio">Pendiente de carga.</div>
  </div>
</section>
"""

ES["plantel"] = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="">
    <div>
      <h1>Plantel 2026</h1>
      <p class="portada-bajada">Los jugadores y el cuerpo técnico de la temporada.</p>
    </div>
  </div>
</section>

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
"""

ES["fixture"] = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="">
    <div>
      <h1>Fixture y tabla</h1>
      <p class="portada-bajada">Resultados, próximos partidos y posiciones de la División de Honor.</p>
    </div>
  </div>
</section>

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
    <p class="entrada">Las fechas del torneo, con horarios y sedes.</p>
    <div class="vacio">Pendiente de carga.</div>
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
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="">
    <div>
      <h1>Hacete socio</h1>
      <p class="portada-bajada">Sostené al club todo el año y entrá a La Arboleda cada fecha.</p>
    </div>
  </div>
</section>

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
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="Club Rubio Ñu crest">
    <div>
      <h1>Rubio Ñu</h1>
      <p class="portada-bajada">White for purity, green for hope. The albiverde of Santísima
      Trinidad is back in the top flight of Paraguayan football.</p>
    </div>
  </div>
  <div class="marco portada-datos">
    <span>Founded on <b>24 August 1913</b></span>
    <span>Stadium <b>La Arboleda</b></span>
    <span>Asunción, <b>Paraguay</b></span>
  </div>
</section>

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
          <p>A group of friends founds the club on 24 August and chooses white and green: white for
          purity, green for hope. That is where the albiverde nickname comes from.</p>
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
          <p>A group of friends founds the club on 24 August in Santísima Trinidad and chooses
          white and green as its colours.</p>
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
    plays every home match here.</p>
    <dl class="datos-grilla">
      <div class="dato"><dt>Location</dt><dd>Santísima Trinidad</dd></div>
      <div class="dato"><dt>Capacity</dt><dd>To be confirmed</dd></div>
      <div class="dato"><dt>Surface</dt><dd>Natural grass</dd></div>
      <div class="dato"><dt>Opened</dt><dd>To be confirmed</dd></div>
    </dl>
  </div>
</section>

<section class="seccion seccion-gris" id="comision">
  <div class="marco">
    <h2 class="titulo-seccion">Board of directors</h2>
    <p class="entrada">The full board is published on this page.</p>
    <div class="vacio">To be added.</div>
  </div>
</section>
"""

EN["plantel"] = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="">
    <div>
      <h1>2026 squad</h1>
      <p class="portada-bajada">The players and coaching staff for the season.</p>
    </div>
  </div>
</section>

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
"""

EN["fixture"] = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="">
    <div>
      <h1>Fixtures and table</h1>
      <p class="portada-bajada">Results, upcoming matches and First Division standings.</p>
    </div>
  </div>
</section>

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
    <p class="entrada">Every matchday of the tournament, with kick-off times and venues.</p>
    <div class="vacio">To be added.</div>
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
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="{base}assets/img/escudo.png" alt="">
    <div>
      <h1>Become a member</h1>
      <p class="portada-bajada">Support the club all year and get into La Arboleda every matchday.</p>
    </div>
  </div>
</section>

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
            html = cabecera(idioma, pagina) + cuerpo + pie(idioma)
            with open(ruta_salida(idioma, pagina), "w", encoding="utf-8") as f:
                f.write(html)
        print(idioma, "→", len(PAGINAS), "páginas")


if __name__ == "__main__":
    construir()
