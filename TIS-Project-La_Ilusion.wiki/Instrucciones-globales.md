# Instrucciones globales:

- El sistema debe ser un proyecto web con Django y base de datos SQLite3.

- Deberán implementar todas las clases de su proyecto.

- Deberán utilizar el sistema “migrations” de Django para llevar el registro de cambios del SQL.

- Vaya creando datos ficticios, y cuando tenga un buen grupo de datos ficticios exporte el SQL (correspondiente a las filas) y suba ese SQL al repositorio (normalmente jamás se subiría un SQL a un proyecto público, pero para facilidad de la entrega así lo haremos).

- Recuerde que cada línea (asociación) en el diagrama de clases se convierte en dos funciones (dinámicamente propiedades) en las dos clases que se relacionan.

- Cree un archivo README.md en la raíz del repositorio donde explique cómo ejecutar el programa, cuál es la ruta principal que se debe invocar, entre otros.

- La aplicación debe tener 2 secciones principales. Sección del usuario final, y sección del administrador. Por lo tanto, se debe utilizar un sistema de Login.

- Tópicos especiales en ingeniería de softwareUtilice el **Tutorial LOGIN Django (Ver Tutorial Sesiones)** para agregar un sistema de login totalmente funcional a su proyecto.
  - **Sección usuario final**, por ejemplo “/*”. Es la aplicación que ve el usuario final, ve los productos, los compra, etc. Pero no puede borrarlos, ni modificarlos, ni crearlos.
  - **Nota:** ojo que las vistas de la sección de administrador no deberían ser las mismas (o compartirse) con las vistas del usuario final. Los paneles de admin se ven muy diferentes a las vistas de usuario final, ejemplo de panel de admin:

- La aplicación deberá contener por lo menos “4 funcionalidades interesantes” diferentes a las tradicionales: crear, editar, borrar y leer. Ejemplos: (i) búsqueda de productos por nombre, (ii) ver top 3 productos más vendidos, (iii) generar en pdf la factura de venta, (iv) ver top 4 productos más
comentados.

- Añada 2 páginas al wiki y enlácelas en la página principal.
  - **Funcionalidades interesantes:** en esta página describa cuales son las 4 funcionalidades interesantes, y en qué archivos están implementadas (especifique la línea exacta desde donde arranca la implementación).
  - **Pantallazos:** Tome un pantallazo de las 3 secciones más importantes de la aplicación y colóquelas en esta página.

- Todos los textos del proyecto deben ir resources/lang/* - si le da tiempo, implemente el proyecto en 2 idiomas.

- Aplique principios DRY y ETC. Sugerencia: ver libro “Pragmatic programmer” topic 8 y 9 (son 4 páginas).

- Aplique los principios, tips, y sugerencias que se han brindado durante todo el curso. Muchos de ellos no aparecen en las presentaciones ya que se discutieron en clase.

- Ojo al reutilizar el código de los talleres, aunque es una muy buena base para iniciar, hay varios cambios y mejoras que se deben realizar que se discutieron durante las clases.

- Coloque la información del autor del código de cada archivo en la parte de arriba de cada archivo (como un comentario).

# Instrucciones de entrega para el arquitecto:
- Comparta el link del repositorio con el docente (en un .txt en la carpeta de Teams) antes de la fecha de finalización de entrega.