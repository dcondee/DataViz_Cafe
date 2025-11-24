import dash
from dash import html, dcc

dash.register_page(__name__, path="/objetivos", name="Objetivos y Justificación", order=5)

# La imagen del banner que se solicita
DATA_SCIENCE_BANNER = html.Img(
    src='/assets/objetivos.jpg', # Asegúrate de usar el nombre de archivo correcto
    alt='Banner de Data Science, IA y Visualización de Datos',
    style={
        'width': '100vw',           # Ocupa todo el ancho de la ventana
        'height': '200px',          # Altura fija para el banner
        'objectFit': 'cover',       # Asegura que la imagen cubra el área sin distorsionarse
        'margin': '-40px 0 30px 0', # Elimina el padding superior del div padre y añade margen inferior
        'display': 'block',         # Asegura que ocupe todo el ancho
        'boxShadow': '0 4px 8px rgba(0,0,0,0.2)' # Sombra sutil para destacarlo
    }
)

layout = html.Div(
    # Estilo del contenedor principal: limita el ancho del texto, pero no del banner
    style={"padding": "40px"},
    children=[
        
        # 1. EL BANNER VA PRIMERO
        DATA_SCIENCE_BANNER,
        
        # Contenedor para el resto del contenido (texto) con ancho limitado y centrado
        html.Div(
            style={"maxWidth": "850px", "margin": "0 auto", "textAlign": "justify"},
            children=[
                
                html.H1("Objetivos y Justificación del Proyecto", className="display-5", style={'textAlign': 'center', 'marginBottom': '30px', 'marginTop': '-10px'}),
                html.Hr(),
                
                # 2. Objetivo General
                html.H3("Objetivo General"),
                dcc.Markdown("""
                    Construir un **dashboard interactivo** que permita visualizar el consumo mundial 
                    de café y analizar su relación con indicadores de salud y bienestar a través de técnicas de **Análisis de Datos y Machine Learning**.
                """, className="lead"),

                html.Br(),

                # 3. Objetivos Específicos
                html.H3("Objetivos Específicos"),
                html.Ul(
                    style={'listStyleType': 'none', 'paddingLeft': '20px'}, # Lista sin bullet points predeterminados
                    children=[
                        # Usamos emojis y negrita para destacar cada punto
                        html.Li(dcc.Markdown(" ** Limpieza y Preparación:** Integrar, limpiar y transformar los datos provenientes de diversas fuentes para su análisis.")),
                        html.Li(dcc.Markdown(" ** Visualización Descriptiva:** Elaborar visualizaciones descriptivas del consumo de café, las distribuciones de variables clave y sus relaciones.")),
                        html.Li(dcc.Markdown(" ** Análisis Geográfico:** Construir un mapa georreferenciado (coroplético) para representar patrones globales de consumo.")),
                        html.Li(dcc.Markdown(" ** Modelado Predictivo:** Desarrollar una herramienta predictiva basada en técnicas de **Machine Learning (Random Forest)** para predecir si una persona podría estar en riesgo de sufrir problemas de salud.")),
                        html.Li(dcc.Markdown(" ** Comunicación de Resultados:** Presentar los hallazgos y el modelo en un Dashboard interactivo y funcional.")),
                    ]
                ),
                
                html.Br(),

                # 4. Justificación
                html.H3("Justificación del Estudio"),
                dcc.Markdown("""
                    > Comprender patrones globales de consumo de café permite generar hipótesis sólidas sobre prácticas culturales, estilos de vida y condiciones de salud. **El componente predictivo (IA)** del proyecto facilita la identificación temprana de factores de riesgo.
                    
                    En última instancia, el dashboard es una herramienta que facilita la **toma de decisiones informada** en contextos de salud pública y economía global, traduciendo datos complejos en conocimiento accionable.
                """, className="blockquote"), # Usamos blockquote para destacar la justificación
                
                html.Hr(style={'marginTop': '40px'})
            ]
        )
    ]
)