# product/generators/pdf_generator.py

from fpdf import FPDF
from product.interfaces import ReporteGenerator

class PDFReporteGenerator(ReporteGenerator):
    """Generador de reportes en formato PDF."""

    def generar_reporte(self, productos):
        pdf = FPDF()
        
        # Establecer márgenes de 3 cm en cada lado
        margen = 30  # 3 cm = 30 mm
        pdf.set_left_margin(margen)
        pdf.set_right_margin(margen)
        pdf.set_top_margin(margen)
        
        # Añadir una página y configurar fuente
        pdf.add_page()
        pdf.set_font("Times", "B", 14)  # Times New Roman en negrita para el título

        # Título del reporte
        pdf.cell(0, 10, txt="Reporte de Productos", ln=True, align="C")
        
        # Ajustar fuente para el contenido del reporte
        pdf.set_font("Times", size=12)  # Times New Roman regular para el contenido

        for producto in productos:
            # Título en negrita y luego contenido normal
            pdf.set_font("Times", "B", 12)
            pdf.cell(0, 10, txt="Producto: ", ln=True)
            pdf.set_font("Times", size=12)
            pdf.cell(0, 10, txt=f"{producto.nombre}", ln=True)
            
            pdf.set_font("Times", "B", 12)
            pdf.cell(0, 10, txt="Precio: ", ln=True)
            pdf.set_font("Times", size=12)
            pdf.cell(0, 10, txt=f"${producto.precio}", ln=True)
            
            pdf.set_font("Times", "B", 12)
            pdf.cell(0, 10, txt="Marca: ", ln=True)
            pdf.set_font("Times", size=12)
            pdf.cell(0, 10, txt=f"{producto.marca}", ln=True)
            
            pdf.set_font("Times", "B", 12)
            pdf.cell(0, 10, txt="Descripción: ", ln=True)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(0, 10, txt=producto.descripcion)
            
            # Espacio en blanco entre productos
            pdf.cell(0, 10, txt="", ln=True)

        # Guardar el PDF
        pdf.output("reporte_productos.pdf")
        print("Reporte en PDF generado exitosamente.")
