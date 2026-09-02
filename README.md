# Currículum — Fernando Fariña

Currículum en formato de página web, publicado con GitHub Pages.

**https://damianfsrc-jpg.github.io/cv/**

## Archivos

| Archivo | Para qué sirve |
| --- | --- |
| `source.html` | La fuente. Acá se editan textos, colores y estructura. |
| `index.html` | **Generado.** Es lo que sirve GitHub Pages. No editarlo a mano. |
| `build.py` | Genera `index.html` a partir de `source.html`. |

`source.html` está escrito para el envoltorio de Claude Artifacts, así que no
lleva `<!doctype>`, `<head>` ni `<body>`. `build.py` agrega ese esqueleto junto
con el `viewport`, las metaetiquetas de Open Graph y el `noindex`.

## Cómo hacer un cambio

```bash
python build.py
git commit -am "Actualizo el CV"
git push
```

Editar `source.html`, correr `build.py`, y hacer commit de los dos archivos.
GitHub Pages tarda un minuto o dos en reflejar el cambio.

## Notas

- Para republicar la versión de Claude Artifacts hay que publicar `source.html`,
  nunca `index.html`: el envoltorio de Artifacts agrega su propio `<head>` y el
  archivo generado quedaría con el esqueleto duplicado.

- La página lleva `noindex, nofollow`: el link funciona para quien lo tenga,
  pero no aparece en los buscadores. Se saca desde `build.py` si en algún
  momento se quiere lo contrario.
- Se adapta al tema claro u oscuro del dispositivo de quien la abre.
- Imprimir desde el navegador genera un PDF con formato propio.
