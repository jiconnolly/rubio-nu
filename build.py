# -*- coding: utf-8 -*-
"""Genera las páginas del sitio de Club Rubio Ñu a partir de plantillas compartidas."""
import os, textwrap

SITIO = "Club Rubio Ñu"
BASE = os.path.dirname(os.path.abspath(__file__))

PAGINAS_MENU = [
    ("index.html", "Inicio"),
    ("club.html", "El club"),
    ("plantel.html", "Plantel"),
    ("fixture.html", "Fixture y tabla"),
    ("noticias.html", "Noticias"),
    ("socios.html", "Hacete socio"),
    ("contacto.html", "Contacto"),
]


def cabecera(actual, titulo, descripcion):
    enlaces = "\n".join(
        '        <a href="{h}"{a}>{t}</a>'.format(
            h=h, t=t, a=' aria-current="page"' if h == actual else ""
        )
        for h, t in PAGINAS_MENU
    )
    return f"""<!DOCTYPE html>
<html lang="es-PY">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · {SITIO}</title>
<meta name="description" content="{descripcion}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{titulo} · {SITIO}">
<meta property="og:description" content="{descripcion}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/escudo.png">
<meta name="theme-color" content="#10201A">
<link rel="icon" href="assets/img/escudo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Karla:ital,wght@0,400;0,500;0,700;1,400&family=Oswald:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
<a class="saltar" href="#contenido">Ir al contenido</a>

<header class="cabecera">
  <div class="marco cabecera-fila">
    <a class="marca" href="index.html">
      <img src="assets/img/escudo.png" alt="">
      <span class="marca-texto">Rubio Ñu
        <small>ASUNCIÓN 1913</small>
      </span>
    </a>
    <button class="menu-boton" aria-expanded="false" aria-controls="menu-principal">Menú</button>
    <nav class="menu" id="menu-principal" aria-label="Principal">
{enlaces}
    </nav>
  </div>
</header>
<div class="filete bastones"></div>

<main id="contenido">
"""


SPONSORS = [
    ("kia.png", "Kia", ""),
    ("ueno-bank.png", "ueno bank", ""),
    ("garcis.png", "Garcis", "alto"),
    ("bambi.png", "Bambi", "alto"),
    ("lacteos-trebol.png", "Lácteos Trébol", "alto"),
]


def banda_sponsors():
    logos = "\n".join(
        '        <img src="assets/img/sponsors/{a}" alt="{n}" class="{c}" loading="lazy">'.format(
            a=a, n=n, c=c
        )
        for a, n, c in SPONSORS
    )
    return f"""<section class="banda-sponsors">
  <div class="marco">
    <p class="rotulo-sponsors">SPONSORS</p>
    <div class="grilla-sponsors">
{logos}
    </div>
  </div>
</section>

"""


def pie():
    return banda_sponsors() + f"""</main>

<footer class="pie">
  <div class="marco">
    <div class="instituciones">
      <div class="instituciones-escudos">
        <span><img src="assets/img/instituciones/apf.png" alt="Asociación Paraguaya de Fútbol"></span>
        <span><img src="assets/img/instituciones/conmebol.png" alt="CONMEBOL"></span>
      </div>
      <p>Rubio Ñu está afiliado a la Asociación Paraguaya de Fútbol, miembro de la CONMEBOL.</p>
    </div>
    <div class="pie-grilla">
      <div class="pie-escudo">
        <img src="assets/img/escudo.png" alt="">
        <div>
          <strong style="color:var(--hueso)">Club Rubio Ñu</strong><br>
          Barrio Santísima Trinidad, Asunción, Paraguay.<br>
          Fundado el 24 de agosto de 1913.
        </div>
      </div>
      <div>
        <h4>EL CLUB</h4>
        <ul>
          <li><a href="club.html">Historia</a></li>
          <li><a href="club.html#estadio">La Arboleda</a></li>
          <li><a href="plantel.html">Plantel</a></li>
        </ul>
      </div>
      <div>
        <h4>COMPETENCIA</h4>
        <ul>
          <li><a href="fixture.html">Fixture</a></li>
          <li><a href="fixture.html#tabla">Tabla de posiciones</a></li>
          <li><a href="noticias.html">Noticias</a></li>
        </ul>
      </div>
      <div>
        <h4>PARTICIPAR</h4>
        <ul>
          <li><a href="socios.html">Hacete socio</a></li>
          <li><a href="contacto.html">Contacto</a></li>
          <li><a href="contacto.html#prensa">Prensa</a></li>
        </ul>
      </div>
    </div>
    <div class="pie-legal">
      <span>© 2026 Club Rubio Ñu. Todos los derechos reservados.</span>
      <span>Asociación Paraguaya de Fútbol · División de Honor</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
"""


def escribir(nombre, titulo, descripcion, cuerpo):
    with open(os.path.join(BASE, nombre), "w", encoding="utf-8") as f:
        f.write(cabecera(nombre, titulo, descripcion) + cuerpo + pie())


# ---------------------------------------------------------------- INICIO
INICIO = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="assets/img/escudo.png" alt="Escudo del Club Rubio Ñu">
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
    <div class="noticias-grilla">
      <a class="noticia" href="noticias.html">
        <time datetime="2026-09-01">1 de septiembre de 2026</time>
        <h3>Título de la nota</h3>
        <p>Bajada breve de la noticia. Esta sección se carga con el material que envíe el
        departamento de prensa del club.</p>
      </a>
      <a class="noticia" href="noticias.html">
        <time datetime="2026-08-28">28 de agosto de 2026</time>
        <h3>Título de la nota</h3>
        <p>Bajada breve de la noticia.</p>
      </a>
      <a class="noticia" href="noticias.html">
        <time datetime="2026-08-24">24 de agosto de 2026</time>
        <h3>Título de la nota</h3>
        <p>Bajada breve de la noticia.</p>
      </a>
    </div>
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

# ---------------------------------------------------------------- CLUB
CLUB = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="assets/img/escudo.png" alt="">
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

# ---------------------------------------------------------------- PLANTEL
PLANTEL = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="assets/img/escudo.png" alt="">
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
    <div class="vacio">Pendiente de carga.</div>
  </div>
</section>
"""

# ---------------------------------------------------------------- FIXTURE
FIXTURE = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="assets/img/escudo.png" alt="">
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
    <p class="entrada">Las 22 fechas del torneo, con horarios y sedes.</p>
    <div class="vacio">Pendiente de carga.</div>
  </div>
</section>
"""

# ---------------------------------------------------------------- NOTICIAS
NOTICIAS = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="assets/img/escudo.png" alt="">
    <div>
      <h1>Noticias</h1>
      <p class="portada-bajada">Novedades del primer equipo, las inferiores y la institución.</p>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <div class="noticias-grilla">
      <a class="noticia" href="#">
        <time datetime="2026-09-01">1 de septiembre de 2026</time>
        <h3>Título de la nota</h3>
        <p>Bajada breve. Reemplazar por el contenido real del departamento de prensa.</p>
      </a>
      <a class="noticia" href="#">
        <time datetime="2026-08-28">28 de agosto de 2026</time>
        <h3>Título de la nota</h3>
        <p>Bajada breve.</p>
      </a>
      <a class="noticia" href="#">
        <time datetime="2026-08-24">24 de agosto de 2026</time>
        <h3>Título de la nota</h3>
        <p>Bajada breve.</p>
      </a>
      <a class="noticia" href="#">
        <time datetime="2026-08-18">18 de agosto de 2026</time>
        <h3>Título de la nota</h3>
        <p>Bajada breve.</p>
      </a>
      <a class="noticia" href="#">
        <time datetime="2026-08-11">11 de agosto de 2026</time>
        <h3>Título de la nota</h3>
        <p>Bajada breve.</p>
      </a>
      <a class="noticia" href="#">
        <time datetime="2026-08-04">4 de agosto de 2026</time>
        <h3>Título de la nota</h3>
        <p>Bajada breve.</p>
      </a>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- SOCIOS
SOCIOS = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="assets/img/escudo.png" alt="">
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

# ---------------------------------------------------------------- CONTACTO
CONTACTO = """
<section class="portada">
  <div class="marco portada-contenido">
    <img class="portada-escudo" src="assets/img/escudo.png" alt="">
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

escribir("index.html", "Sitio oficial",
         "Sitio oficial del Club Rubio Ñu, de Santísima Trinidad, Asunción. Fundado en 1913.", INICIO)
escribir("club.html", "El club",
         "Historia, estadio y datos institucionales del Club Rubio Ñu.", CLUB)
escribir("plantel.html", "Plantel",
         "Plantel y cuerpo técnico del Club Rubio Ñu, temporada 2026.", PLANTEL)
escribir("fixture.html", "Fixture y tabla",
         "Fixture, resultados y tabla de posiciones del Club Rubio Ñu.", FIXTURE)
escribir("noticias.html", "Noticias",
         "Novedades del Club Rubio Ñu.", NOTICIAS)
escribir("socios.html", "Hacete socio",
         "Categorías de socio y alta en el Club Rubio Ñu.", SOCIOS)
escribir("contacto.html", "Contacto",
         "Datos de contacto del Club Rubio Ñu.", CONTACTO)

print("Páginas generadas:", ", ".join(p for p, _ in PAGINAS_MENU))
