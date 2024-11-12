# product/interfaces.py

from abc import ABC, abstractmethod

class ReporteGenerator(ABC):
    """Interfaz para los generadores de reportes."""
    
    @abstractmethod
    def generar_reporte(self, productos):
        """Genera un reporte a partir de una lista de productos."""
        pass
