from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now

# Modelo de Categoría
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True, verbose_name="ID de la categoría")
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Categoría", null=False, blank=False)

    def __str__(self):
        return self.nombre

# Modelo de Subcategoría
class Subcategoria(models.Model):
    id_subcategoria = models.AutoField(primary_key=True, verbose_name="ID de la subcategoría")
    nombre = models.CharField(max_length=100, verbose_name="Subcategoría", null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='subcategorias', verbose_name="Categoría", null=False, blank=False)

    def __str__(self):
        return f"{self.categoria.nombre} - {self.nombre}"

# Clase base con campos comunes para todas las categorías de productos
class ProductoBase(models.Model):
    # Relación con Categoría y Subcategoría
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='productos', verbose_name="Categoría", null=False, blank=False)
    subcategoria = models.ForeignKey('Subcategoria', on_delete=models.CASCADE, related_name='productos', verbose_name="Subcategoría", null=False, blank=False)
    
    # Campo para el usuario que registró el producto
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='productos', verbose_name="Usuario", null=True, blank=False)
    
    # Campos base obligatorios
    id_producto = models.AutoField(primary_key=True, verbose_name="ID del producto", null=False, blank=False)
    nombre = models.CharField(max_length=255, verbose_name="Nombre del producto", null=False, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio", validators=[MinValueValidator(0)], null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción del producto", null=False, blank=False)
    uso = models.TextField(verbose_name="Uso del producto", null=False, blank=False)
    marca = models.CharField(max_length=100, verbose_name="Marca", null=False, blank=False)
    garantia = models.IntegerField(verbose_name="Garantía (meses)", null=False, blank=False)
    
    # Fecha de creación, modificación, estado activo y eliminación
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=False, blank=False)
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de última modificación", null=False, blank=False)
    esta_activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_eliminacion = models.DateTimeField(verbose_name="Fecha de eliminación", null=True, blank=True)

    class Meta:
        abstract = True  # Esto indica que esta clase es abstracta y no se creará una tabla para ella

    def __str__(self):
        return self.nombre

    # Método clean para validaciones adicionales
    def clean(self):
        # Llama a la validación de los campos en el modelo padre (si es necesario)
        super().clean()

        # Validación de fechas: Si el producto está marcado como activo, no debe tener fecha de eliminación
        if self.esta_activo and self.fecha_eliminacion is not None:
            raise ValidationError("Un producto activo no puede tener una fecha de eliminación.")

        # Si el producto no está activo, debe tener una fecha de eliminación
        if not self.esta_activo and self.fecha_eliminacion is None:
            raise ValidationError("Un producto inactivo debe tener una fecha de eliminación.")

        # Validación de la fecha de eliminación: No puede ser en el futuro
        if self.fecha_eliminacion and self.fecha_eliminacion > now():
            raise ValidationError("La fecha de eliminación no puede ser en el futuro.")

        # Validación del precio: Ya se asegura con el validador, pero podrías incluir otra regla si es necesario
        if self.precio < 0:
            raise ValidationError("El precio no puede ser negativo.")

# Modelo de Imagen
class Imagen(models.Model):
    id_imagen = models.AutoField(primary_key=True, verbose_name="ID de la imagen")
    # Cambia el related_name aquí
    productos = models.ManyToManyField('Producto', related_name='imagenes_inversas', blank=True)  # Cambiado a 'imagenes_inversas'
    url = models.ImageField(upload_to='imagenes_de_productos/', verbose_name="Imagen", null=False, blank=False)
    descripcion = models.CharField(max_length=255, blank=True, verbose_name="Descripción")

    def __str__(self):
        return self.descripcion if self.descripcion else f"Imagen {self.id_imagen}"


# Modelo de Producto que hereda de ProductoBase
class Producto(ProductoBase):
    # Imágenes es un campo obligatorio con una relación ManyToMany
    imagenes = models.ManyToManyField(Imagen, blank=True, verbose_name="Imágenes", related_name='productos_inversos')

    # Relación con comentarios
    #comentarios = models.ManyToManyField('Comentario', blank=True, verbose_name="Comentarios")

    # Campos específicos para la categoría de productos, pueden o no estar vacíos.
    acabado = models.CharField(max_length=255, blank=True, null=True, verbose_name="Acabado")
    adherencia = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adherencia")
    alto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Alto (cm)")
    altura_griferia = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Altura de la grifería (cm)")
    ancho = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Ancho (cm)")
    areas_uso = models.TextField(blank=True, null=True,verbose_name="Áreas de uso")
    calidad = models.CharField(max_length=255, blank=True, null=True, verbose_name="Calidad")
    capacidad_descarga = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True, verbose_name="Capacidad de descarga (L)")
    componentes = models.TextField(blank=True, null=True,verbose_name="Componentes incluidos")
    consumo_agua = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True, verbose_name="Consumo de agua (L/min)")
    contenido_producto = models.TextField(blank=True, null=True,verbose_name="Contenido del producto")
    diametro_desague = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True, verbose_name="Diámetro del desagüe (cm)")
    dimensiones = models.CharField(max_length=255, blank=True, null=True,verbose_name="Dimensiones")
    dilucion = models.CharField(max_length=255, blank=True, null=True,verbose_name="Dilución")
    espesor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Espesor (cm)")
    forma = models.CharField(max_length=255, blank=True, null=True,verbose_name="Forma")
    formato = models.CharField(max_length=255, blank=True, null=True,verbose_name="Formato")
    garantia = models.TextField(blank=True, null=True,verbose_name="Garantía")
    incluye = models.TextField(blank=True, null=True,verbose_name="Incluye")
    largo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Largo (cm)")
    lavabilidad = models.CharField(max_length=255, blank=True, null=True, verbose_name="Lavabilidad")
    longitud_brazo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Longitud del brazo (cm)")
    materiales = models.TextField(blank=True, null=True,verbose_name="Materiales")
    metro_por_caja = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, verbose_name="Metro por caja")
    no_incluye = models.TextField(blank=True, null=True,verbose_name="No incluye")
    perfil_tasa = models.CharField(max_length=255, blank=True, null=True,verbose_name="Perfil de tasa")
    piezas_por_caja = models.PositiveIntegerField(blank=True, null=True, verbose_name="Piezas por caja")
    presentacion = models.CharField(max_length=255, blank=True, null=True,verbose_name="Presentación")
    productos_compatibles = models.TextField(blank=True, null=True,verbose_name="Productos compatibles")
    profundidad_pozo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Profundidad del pozo (cm)")
    rendimiento = models.TextField(blank=True, null=True, verbose_name="Rendimiento")
    sistema_accionamiento = models.CharField(max_length=255, blank=True, null=True,verbose_name="Sistema de accionamiento")
    sistema_descarga = models.CharField(max_length=255, blank=True, null=True,verbose_name="Sistema de descarga")
    tiempo_abierto = models.DecimalField(max_digits=2, decimal_places=1,blank=True, null=True, verbose_name="Tiempo abierto (min)")
    tiempo_secado = models.DecimalField(max_digits=2, decimal_places=1,blank=True, null=True, verbose_name="Tiempo de secado (min)")
    tiempo_emboquillar = models.DecimalField(max_digits=2, decimal_places=1,blank=True, null=True, verbose_name="Tiempo para emboquillar (min)")
    tipo_asiento = models.CharField(max_length=255, blank=True, null=True,verbose_name="Tipo de asiento")
    tipo_chorro = models.CharField(max_length=255, blank=True, null=True,verbose_name="Tipo de chorro")
    tipo_cierre = models.CharField(max_length=255, blank=True, null=True,verbose_name="Tipo de cierre")
    tipo_griferia = models.CharField(max_length=255, blank=True, null=True,verbose_name="Tipo de grifería")
    tipo_herrajes = models.CharField(max_length=255, blank=True, null=True,verbose_name="Tipo de herrajes")
    tipo_instalacion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tipo de instalación")
    tipo_lavamanos = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tipo de lavamanos")
    tipo_manija = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tipo de manija")
    tipo_mezclador = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tipo de mezclador")
    tipo_pintura = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tipo de pintura")
    tipo_regadera = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tipo de regadera")
    tipo_sifon = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tipo de sifón")
    tipo_tanque = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tipo de tanque")
    trafico = models.DecimalField(max_digits=2, decimal_places=0, max_length=255, blank=True, null=True, verbose_name="Tráfico")

    # Calificaciones individuales se gestionan dentro del modelo Comentario, no como ManyToMany.

    def promedio_calificaciones(self):
        # Calcular el promedio de las calificaciones de los comentarios asociados al producto
        comentarios_con_calificacion = self.comentarios.filter(calificacion__isnull=False)
        if comentarios_con_calificacion.exists():
            total_calificaciones = sum([comentario.calificacion for comentario in comentarios_con_calificacion])
            return total_calificaciones / comentarios_con_calificacion.count()
        return None  # O 0 si prefieres retornar un valor numérico en lugar de None.

    def __str__(self):
        return self.nombre


    def __str__(self):
        return self.nombre
        
    def clean(self):
        super().clean()
        # Asegúrate de que los campos no sean None antes de hacer comparaciones
        # Aquí puedes manejar el caso en que precio o stock sean None
        if self.precio is None:
            raise ValidationError("El precio no puede ser vacío.")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Guarda el objeto primero


# Modelo de Comentario con calificación
class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True, verbose_name="ID del comentario")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='comentarios', verbose_name="Producto", null=True, blank=True)
    texto = models.TextField(verbose_name="Comentario", null=False, blank=False)
    fecha_comentario = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del comentario")
    calificacion = models.PositiveSmallIntegerField(verbose_name="Calificación", validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios', verbose_name="Usuario", null=False, blank=False)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        # Utilizamos el email en lugar de username
        return f"Comentario de {self.usuario.email} el {self.fecha_comentario.strftime('%Y-%m-%d')}, Calificación: {self.calificacion if self.calificacion else 'Sin calificación'}"
