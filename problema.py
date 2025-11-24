import dash
from dash import html, dcc

dash.register_page(__name__, path="/problema", name="Planteamiento del Problema", order=4)

layout = html.Div(
    style={"padding": "40px"},
    children=[
        html.H1("🎯 Planteamiento del Problema", style={"fontWeight": "bold"}),

        html.P(
            """
El consumo de café es un hábito ampliamente extendido a nivel global y su impacto
en la salud ha sido objeto de numerosos estudios. Sin embargo, comprender cómo se
comporta este consumo en distintos países y de qué manera se relaciona con indicadores
como la calidad del sueño, el índice de masa corporal (BMI), los niveles de estrés o la
actividad física, requiere herramientas que permitan explorar los datos de manera clara
y comparativa.
            """,
            style={"textAlign": "justify"},
        ),

        html.P(
            """
En este proyecto buscamos desarrollar una herramienta interactiva que permita
visualizar la distribución del consumo de café en los diferentes países incluidos en el
Global Coffee Health Dataset, así como analizar su relación con otros indicadores
relevantes presentes en la base de datos. A través de visualizaciones dinámicas y
análisis exploratorios, se pretende ofrecer una comprensión más profunda de los patrones
de comportamiento asociados al consumo de cafeína y su posible influencia en el estilo
de vida y la salud.
            """,
            style={"textAlign": "justify"},
        ),

        html.P(
            """
Además de la exploración visual, se propone aplicar técnicas de Ciencia de Datos y
Machine Learning para construir un modelo predictivo capaz de estimar si una persona,
con base en sus características y hábitos registrados, tiene mayor probabilidad de
presentar problemas de salud. Con ello, se busca no solo describir patrones, sino también
ofrecer una aproximación analítica que contribuya a la identificación temprana de riesgos.
            """,
            style={"textAlign": "justify"},
        ),

        html.Br(),
        html.Hr(),

        html.P(
            "Esta página forma parte del Dashboard del proyecto de Visualización de Datos.",
            style={"fontStyle": "italic", "color": "gray"},
        ),
    ]
)
