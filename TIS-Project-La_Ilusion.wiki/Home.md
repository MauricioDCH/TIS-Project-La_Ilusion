# Integrantes.
- Camilo Ortegón Saugter.
- Mauricio David Correa Hernandez.

# Materia.
Tópicos Especiales de Ingeniería de Software.

# Universidad.
Universidad EAFIT

# Logo del Equipo.
[Link de la imagen del grupo.](https://drive.google.com/file/d/161TfPQmfmGOaQ3KfajI_EwKtsdkMRUBb/view?usp=drive_link)

# Modelo Verbal Definitivo.

Este proyecto viene desde hace algunos semestres atrás, la idea es desarrollar el E-Commerce de la empresa La Ilusión Pisos y Enchapes, la cual es una empresa fundada por familiares en el año 2008. La plataforma que se está desarrollando tiene el fin de  permitir a los clientes de esta empresa navegar por productos relacionados con pisos y enchapes, pinturas entre otros. Realizar pedidos y consultar información detallada sobre los productos, creando su usuario en la página, revisando la información empresarial de dicha entidad, hacer pagos y agregando productos al carrito. Adicionalmente, por el lado del administrador, podrá revisar el inventario, crear, eliminar, actualizar los productos que se venden allí.

A continuación, se describe el flujo y la interacción entre los principales componentes de la arquitectura del sistema.

1. **Navegador ↔ URLs: Solicitudes y Respuestas HTTP.**
El cliente, desde su navegador, inicia la interacción con la plataforma enviando una solicitud HTTP (HTTP Request), generalmente en forma de una URL, como. Esta solicitud llega al sistema de enrutamiento (URLs). El sistema analiza la URL solicitada y decide qué vista debe manejar dicha solicitud.
Después de que el enrutador selecciona la vista adecuada, la vista procesa la solicitud y genera una respuesta HTTP (HTTP Response) que se envía de vuelta al navegador del cliente. Esta respuesta puede incluir páginas web HTML, CSS, Bootstrap 5 o incluso datos JSON si es una API.

1. **URLs ↔ Views: Enrutamiento y Despacho.**
El sistema de URLs se encarga de enrutar las solicitudes del navegador a la vista correspondiente. Por ejemplo, una solicitud a /product puede dirigirse a la vista ProductListView, que es responsable de listar los productos disponibles. El proceso de enrutamiento implica la definición de rutas y controladores en el archivo urls.py, donde cada ruta URL es mapeada a una vista específica.
No hay un flujo inverso directo de las vistas hacia las URLs, pero las vistas pueden enviar redirecciones a otras URLs, como en el caso de una operación exitosa o cuando un usuario necesita ser llevado a otra página.

1. **Views ↔ Models: Lógica de Negocio y Consultas a la Base de Datos.**
Una vez que la vista es activada a través de las URLs, la vista puede comunicarse con los modelos. Los modelos representan los datos del negocio (en este caso, productos, pedidos, usuarios, etc.) y gestionan la interacción con la base de datos mediante un ORM (Object Relational Mapper).
La vista puede consultar a un modelo para obtener la lista de productos disponibles (Product.objects.all()), o puede crear, actualizar o eliminar registros en la base de datos, dependiendo de la lógica de negocio. Esta interacción permite a las vistas mostrar datos dinámicos y gestionar las operaciones CRUD (crear, leer, actualizar y eliminar).
En este flujo, la vista realiza consultas o actualizaciones y el modelo devuelve los resultados o confirma la operación.

1. **Views ↔ Templates: Data Binding y Renderización.**
Las vistas preparan la información que se enviará al cliente y la pasan a los templates. Los templates son archivos HTML que están diseñados para renderizar datos dinámicos utilizando el contexto proporcionado por las vistas. Por ejemplo, la vista ProductListView puede pasar una lista de productos a un template llamado productos.html, que luego renderiza esa lista como una tabla o galería en una página web.
El flujo desde la vista hacia el template implica la inyección de datos dinámicos para la renderización. El flujo inverso consiste en que el template devuelto contiene la información lista para ser visualizada por el usuario en el navegador.

1. **Models ↔ Base de Datos: ORM y Consultas SQL.**
Los modelos interactúan directamente con la base de datos, generalmente utilizando un ORM (Object Relational Mapper). En el caso de Django, el ORM facilita la generación automática de consultas SQL para interactuar con la base de datos de forma eficiente. Por ejemplo, si la vista solicita a un modelo que obtenga todos los productos disponibles, el ORM genera una consulta SQL como SELECT * FROM productos y devuelve los resultados como objetos que pueden ser utilizados por las vistas.
El flujo inverso implica que los cambios realizados en los modelos, como la creación de nuevos productos o la actualización de precios, se reflejan en la base de datos mediante consultas de inserción o actualización.


# Diagrama de Clases.
Ya que no se ve bien las imágenes por gran detalle, ver mejor el diagrama de clases, dirigirse al link.

[Diagrama de clases proyecto La Ilusión](https://drive.google.com/file/d/1BfMW766jc2zTV_3rsJBsVzgNfwQH2qrU/view?usp=sharing)

# Diagrama de Arquitectura.
Ya que no se ve bien las imágenes por gran detalle, ver mejor el diagrama de arquitectura, dirigirse al link.

[Diseño Arquitectónico - MVT](https://drive.google.com/file/d/1UAZ0f0lXIDoxjIDW1XDn5GK1h-tePdYf/view?usp=sharing)

# Implementación en Django.
Repositorio de implementación.

[TIS-Project-La_Ilusion.git](https://github.com/MauricioDCH/TIS-Project-La_Ilusion.git)