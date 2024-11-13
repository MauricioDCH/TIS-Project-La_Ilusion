# Guía de estilo de programación.

En nuestro proyecto vamos a utilizar varias guías de estilo, como utilizaremos python, css y html vamos a utilizar para cada uno de los lenguajes de programación su documentación de guía de estilo.

## Python.

La guía de programación con la que vamos a trabajar en python es:

- Documentación: [PEP8](https://peps.python.org/pep-0008/)
- Para el formateo automático vamos a utilizar la librería ```autopep8```.
- Para su instalación usamos.

```bash
pip install autopep8
```

- Para la ejecución desde la carpeta principal del proyecto:
```bash
autopep8 --in-place --aggressive --aggressive --recursive .
```

Desglose del Comando
- ```--in-place```: Modifica los archivos en su lugar.
- ```--aggressive```: Realiza más cambios, incluso cambios más agresivos. Puedes añadirlo varias veces para aumentar el nivel de agresividad.
- ```--recursive```: Aplica el formateo recursivamente en todos los subdirectorios.
- ```.```: Indica que se debe aplicar en el directorio actual.

## HTML y CSS.
La guía de programación con la que vamos a trabajar en html y css es:

- Documentación: [Documentación para html y css](https://www.mclibre.org/consultar/htmlcss/css/css-guia-estilo.html)
- Instalación de Node.js:[Link de Node.js](https://nodejs.org/)

  Seguimos la información de instalación para cada uno de los sistemas operativos.
- Instalamos npm

```bash
npm install
```
- Instalamos npm prettier.

```bash
npm install --global prettier
```

- Para la ejecución desde la carpeta principal del proyecto:
```bash
prettier --write "**/*.html" "**/*.css"
```

Con estas ejecuciones vamos a tene un proyecto bien formateado para los tres lenguajes de programación que vamos a usar.