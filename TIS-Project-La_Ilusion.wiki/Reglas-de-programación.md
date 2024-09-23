# Reglas de programación.

Claro, aquí tienes un conjunto de reglas de programación para un proyecto Django, organizadas por categorías:

### Reglas de Programación para el Proyecto Django

#### 1. **Reglas para Controladores (Views)**

- **Extensión de Template Base**: Todas las vistas deben extender de `base.html` para mantener una estructura común en la interfaz de usuario.
  
  ```python
  class MiVista(TemplateView):
      template_name = "mi_app/base.html"
  ```

- **Funcionalidad de Vista**: Cada vista debe tener una funcionalidad clara y única. Evitar la lógica compleja dentro de las vistas; en su lugar, delegar a servicios o modelos.

- **Uso de Decoradores**: Utilizar decoradores de autenticación (`@login_required`, `@permission_required`) donde sea necesario para asegurar el acceso a las vistas.

#### 2. **Reglas para Modelos**

- **Nombres de Clases**: Los nombres de los modelos deben ser sustantivos en singular y utilizar la convención de nombres en CamelCase.

  ```python
  class Producto(models.Model):
      nombre = models.CharField(max_length=100)
  ```

- **Uso de Métodos**: Definir métodos relevantes dentro del modelo para encapsular la lógica relacionada con el modelo en lugar de exponerlo directamente en las vistas.

- **Estructura de Datos**: Utilizar los tipos de campo adecuados y establecer validaciones donde sea necesario para garantizar la integridad de los datos.

#### 3. **Reglas para Templates**

- **Formato de Archivos**: Todos los templates deben ser archivos HTML y deben estar organizados en carpetas correspondientes a cada aplicación.

- **Uso de Bloques**: Utilizar bloques en los templates para facilitar la herencia y la sobreescritura en sub-templates.

  ```html
  {% block content %}
  {% endblock %}
  ```

- **Evitar Lógica Compleja**: Mantener la lógica en los templates al mínimo; las decisiones deben hacerse en las vistas o modelos.

#### 4. **Reglas para Rutas (URLs)**

- **Asociación con Vistas**: Cada ruta debe estar asociada a una vista específica para mantener un mapeo claro entre URLs y lógica de negocio.

- **Nombres de Rutas**: Utilizar nombres descriptivos y legibles para las rutas en el archivo `urls.py`.

  ```python
  path('productos/', MiVista.as_view(), name='lista_productos')
  ```

- **Uso de Namespaces**: Cuando sea necesario, utilizar namespaces para agrupar URLs relacionadas.

#### 5. **Reglas para Pruebas**

- **Cobertura de Pruebas**: Asegurarse de que todas las vistas, modelos y funciones críticas estén cubiertas por pruebas automatizadas.

- **Ejecución de Pruebas**: Ejecutar pruebas unitarias regularmente para garantizar que los cambios no rompan funcionalidades existentes.

#### 6. **Reglas de Documentación**

- **Comentarios**: Utilizar comentarios claros y concisos para explicar la lógica compleja en el código.

- **Documentación de Código**: Cada función y clase debe tener una docstring que explique su propósito y uso.