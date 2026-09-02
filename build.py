"""Genera index.html (página completa, para GitHub Pages) a partir de source.html.

source.html está escrito para el envoltorio de Claude Artifacts: arranca directo
con <title>/<link>/<style> y sigue con el markup, sin <!doctype>, <html>, <head>
ni <body>. Este script agrega ese esqueleto más las metaetiquetas que una página
servida por su cuenta necesita: viewport, description, Open Graph y noindex.

Uso:  python build.py
"""

from pathlib import Path
from urllib.parse import quote

RAIZ = Path(__file__).parent
FUENTE = RAIZ / "source.html"
SALIDA = RAIZ / "index.html"

URL = "https://damianfsrc-jpg.github.io/cv/"
TITULO = "Fernando Fariña"
DESCRIPCION = (
    "Gestión de propiedades, atención al cliente y producción de contenido "
    "audiovisual. Santa Teresita."
)

# El markup del body empieza acá; todo lo anterior es contenido de <head>.
CORTE = '<header class="bar"'

FAVICON = "data:image/svg+xml," + quote(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
    '<text y=".9em" font-size="90">🧭</text></svg>'
)


def construir() -> str:
    fuente = FUENTE.read_text(encoding="utf-8")
    if CORTE not in fuente:
        raise SystemExit(f"No encontré {CORTE!r} en source.html: no sé dónde termina el head.")
    cabeza, cuerpo = fuente.split(CORTE, 1)
    cuerpo = CORTE + cuerpo

    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Pedido a los buscadores de no listar esta página. El link sigue funcionando
     para quien lo tenga; simplemente no aparece en resultados de búsqueda. -->
<meta name="robots" content="noindex, nofollow">

<meta name="description" content="{DESCRIPCION}">
<meta name="author" content="{TITULO}">

<meta property="og:type" content="profile">
<meta property="og:title" content="{TITULO}">
<meta property="og:description" content="{DESCRIPCION}">
<meta property="og:url" content="{URL}">
<meta property="og:locale" content="es_AR">
<meta name="twitter:card" content="summary">

<meta name="theme-color" content="#ECEEF2" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#101317" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{FAVICON}">

<style>
  :root {{ color-scheme: light dark; }}
  img {{ max-width: 100%; }}
  [hidden] {{ display: none !important; }}
</style>

{cabeza.rstrip()}
</head>
<body>
{cuerpo.rstrip()}
</body>
</html>
"""


if __name__ == "__main__":
    SALIDA.write_text(construir(), encoding="utf-8")
    print(f"index.html generado ({SALIDA.stat().st_size:,} bytes)")
