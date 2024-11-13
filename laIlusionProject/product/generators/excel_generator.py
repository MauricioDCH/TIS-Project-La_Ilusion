# product/generated/excel_generator.py

from openpyxl import Workbook
from openpyxl.styles import Alignment
from product.interfaces import ReporteGenerator

class ExcelReporteGenerator(ReporteGenerator):
    """Generador de reportes en formato Excel."""

    def generar_reporte(self, productos):
        wb = Workbook()
        ws = wb.active
        ws.title = "Reporte de Productos"

        # Agregar encabezados
        ws.append(["Nombre", "Precio $", "Marca", "Descripción"])

        # Agregar los productos
        for producto in productos:
            ws.append([producto.nombre, producto.precio, producto.marca, producto.descripcion])

        # Ajustar el texto para la columna de descripción
        descripcion_columna = ws["D"]  # Columna D contiene la Descripción
        for cell in descripcion_columna:
            cell.alignment = Alignment(wrap_text=True)  # Permite el ajuste de texto en varias líneas

        # Ajuste automático del ancho de columna para mejor visualización
        for column_cells in ws.columns:
            max_length = 0
            column = column_cells[0].column_letter  # Obtener la letra de la columna
            for cell in column_cells:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            adjusted_width = (max_length + 2)
            ws.column_dimensions[column].width = adjusted_width

        # Guardar el archivo Excel
        wb.save("reporte_productos.xlsx")
        print("Reporte en Excel generado exitosamente.")
