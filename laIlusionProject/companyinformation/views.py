# companyinformation/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Inicio - La Ilusión Pisos y Enchapes",
            "Bienvenida":"Bienvenidos a la aplicación de la empresa la Ilusión Pisos y Enchapes.",
            "Contenido_slogan":"\"Donde los sueños de su hogar se hacen realidad\"",
        })

        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Sobre Nosotros - La Ilusión Pisos y Enchapes",
            "Subtitle": "Conoce más sobre nuestra empresa",
            
            "Slogan": "SLOGAN:",
            "Contenido_slogan":"\"Donde los sueños de su hogar se hacen realidad\"",
            
            "Historia": "HISTORIA:",
            "Contenido_historia": "La Ilusión Pisos y Enchapes es una empresa familiar fundada en el año 2008, en la ciudad de Medellín. Desde nuestros inicios, nos hemos dedicado a la venta de pisos y enchapes de la más alta calidad, con el objetivo de brindar a nuestros clientes soluciones para la construcción y remodelación de sus espacios. Con más de 16 años de experiencia en el mercado, nos hemos consolidado como una empresa líder en la región, gracias a la excelencia de nuestros productos y servicios.",
            
            "Mision": "MISIÓN:",
            "Contenido_Mision": "Somos una Empresa Privada, dedicada a la compra, venta y distribución de Materiales de obra blanca para la construcción a la población de la ciudad de Medellín y el departamento de Antioquia, gerenciada con ética empresarial, responsabilidad social y profesionalidad; contamos con personal calificado; comercializamos productos de alta calidad; hacemos énfasis en el respeto de los clientes, basados en los principios de responsabilidad, honestidad, confianza y seguridad.",
            
            "Vision": "VISIÓN:",
            "Contenido_Vision": "En el 2025 ser reconocidos en el medio del comercio de materiales de obra blanca para la construcción, como un almacén que atiende las necesidades que tiene la población de la ciudad de Medellín y el departamento de Antioquia en el ramo, con calidad, calidez, respeto y honestidad, logrando ampliar los servicios al 50% de los municipios del Área Metropolitana del Valle de Aburra y del Departamento de Antioquia.",
            
            "Valores": "NUESTROS VALORES:",
            "Contenido_Valores": "En La Ilusión Pisos y Enchapes, nos regimos por los siguientes valores:",
            "Valor_1": "RESPETO:",
            "Contenido_valor_1":"El buen trato, la equidad y el reconocimiento de los derechos de nuestros usuarios.",
            "Valor_2": "RESPONSABILIDAD AMBIENTAL:",
            "Contenido_valor_2":"Buscamos la sostenibilidad de nuestra actividad institucional y de nuestros servicios, a partir de la reducción del impacto sobre el medio ambiente y la generación de un mayor bienestar de nuestras comunidades vecinas, clientes y proveedores. Es permanente nuestro compromiso y participación en el mejoramiento de la sociedad en la cual vivimos y trabajamos.",
            "Valor_3": "COMPROMISO:",
            "Contenido_valor_3":"Con nuestros usuarios, entrega, dedicación y convencimiento, siempre presente en nuestras acciones.",
            "Valor_4": "COMPETITIVIDAD:",
            "Contenido_valor_4":"Nos esforzamos diariamente para agregar valor y lograr la excelencia. Lo hacemos siendo ágiles, flexibles y proactivos, constantemente.",
            "Valor_5": "HONESTIDAD:",
            "Contenido_valor_5":"Comportamiento y expresión coherente y sincera de acuerdo con los valores de verdad y justicia.",
            "Politica_de_calidad":"POLÍTICA DE CALIDAD",
            "Contenido_politica_de_calidad":"En el Almacén LA ILUSION PISOS Y ENCHAPES, estamos comprometidos con la calidad de los procedimientos propios de la institución; la calidad de vida de los clientes, con la conservación y cuidado del medio ambiente y con la calidad de vida de las personas que laboran en la organización.",
            "Actividad_economica":"ACTIVIDAD ECONÓMICA",
            "Contenido_actividad_economica":"El Almacén LA ILUSION PISOS Y ENCHAPES es una Entidad Privada, dedicada a la compra, venta y distribución de Materiales para la construcción y en especial para obra blanca como pisos, enchapes, sanitarios y accesorios, pinturas y cocinas prefabricadas; brindando atenciones, servicios y productos de alta calidad, a través de la adquisición de estos productos a los mejores proveedores y con la atención por personal capacitado y con amplia experiencia. ",
        })

        return context

class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contáctenos - La Ilusión Pisos y Enchapes",
            "Subtitle": "Contáctenos para más información",
            "Telefono_fijo": "Teléfono fijo",
            "Contenido_telefono_fijo": "(604) 251-6450",
            "Telefono_celular": "Teléfono celular",
            "Contenido_telefono_celular": "(314) 881-7721",
            "Correo_electronico": "Correo electrónico de contacto",
            "Contenido_correo_electronico": "mario.perez.moralez@hotmail.com",
            "Direccion": "Dirección",
            "Contenido_direccion_1": "Carrera 55 N° 58A - 18",
            "Contenido_direccion_2": "Glorieta de la minorista (Diagonal a EASY)",
            "Contenido_direccion_3": "Medellín, Antioquia",
        })
        
        return context
    