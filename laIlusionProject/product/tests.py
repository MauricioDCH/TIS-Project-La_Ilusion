from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from .models import Categoria, Subcategoria, Producto, Imagen
from django.contrib.auth import get_user_model

User = get_user_model()
class ProductoModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.categoria = Categoria.objects.create(nombre="Herramientas")
        cls.subcategoria = Subcategoria.objects.create(nombre="Espátula", categoria=cls.categoria)
        
        # Crear un usuario de prueba
        cls.usuario = User.objects.create_user(email="testuser@example.com", password="Mauricio123!!")

        # Crear una imagen de prueba
        cls.imagen = Imagen.objects.create(
            url="imagenes_de_productos/espatula-5-pulgadas.jpg",
            descripcion="Imagen de prueba"
        )

    def test_crear_producto_valido(self):
        producto = Producto.objects.create(
            categoria=self.categoria,
            subcategoria=self.subcategoria,
            usuario=self.usuario,
            nombre="Espátula de 5 pulgadas",
            precio=5000.00,
            descripcion="Espátula de acero inoxidable",
            uso="Uso doméstico",
            marca="Goya",
            garantia=0,
            esta_activo=True
        )
        producto.imagenes.add(self.imagen)
        producto.clean()
        self.assertEqual(str(producto), "Espátula de 5 pulgadas")
        self.assertTrue(producto.esta_activo)

    def test_producto_inactivo_debe_tener_fecha_eliminacion(self):
        producto = Producto(
            categoria=self.categoria,
            subcategoria=self.subcategoria,
            usuario=self.usuario,
            nombre="Espátula de 3 pulgadas",
            precio=4500.00,
            descripcion="Espátula de acero inoxidable",
            uso="Uso doméstico",
            marca="Goya",
            garantia=0,
            esta_activo=False,
            fecha_eliminacion=now()
        )
        try:
            producto.clean()
            producto.save()
        except ValidationError:
            self.fail("Producto inactivo debería permitir una fecha de eliminación.")

    def test_producto_activo_no_debe_tener_fecha_eliminacion(self):
        producto = Producto(
            categoria=self.categoria,
            subcategoria=self.subcategoria,
            usuario=self.usuario,
            nombre="Espátula de 2 pulgadas",
            precio=4000.00,
            descripcion="Espátula de acero inoxidable",
            uso="Uso doméstico",
            marca="Goya",
            garantia=0,
            esta_activo=True,
            fecha_eliminacion=now()
        )
        # Esto debería causar un ValidationError, intento de validación que debería fallar
        with self.assertRaises(ValidationError):
            producto.clean()

    def test_precio_negativo_debe_lanzar_error(self):
        producto = Producto(
            categoria=self.categoria,
            subcategoria=self.subcategoria,
            usuario=self.usuario,
            nombre="Espátula de 1 pulgada",
            precio=-3000.00,  # Precio inválido
            descripcion="Espátula de acero inoxidable",
            uso="Uso doméstico",
            marca="Goya",
            garantia=0,
            esta_activo=True
        )
        # Intento de validación que debería fallar
        with self.assertRaises(ValidationError):
            producto.clean()

    def test_asociacion_imagenes_producto(self):
        producto = Producto.objects.create(
            categoria=self.categoria,
            subcategoria=self.subcategoria,
            usuario=self.usuario,
            nombre="Aspiradora Dyson",
            precio=200.00,
            descripcion="Aspiradora sin bolsa",
            uso="Uso doméstico",
            marca="Dyson",
            garantia=24,
            esta_activo=True
        )
        producto.imagenes.add(self.imagen)
        self.assertEqual(producto.imagenes.count(), 1)
        self.assertEqual(producto.imagenes.first(), self.imagen)
