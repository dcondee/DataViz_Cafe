import dash
from dash import html

layout = html.Div(
    style={
        "padding": "40px",
        "maxWidth": "900px",
        "margin": "0 auto",
        "fontFamily": "Arial, sans-serif",
        "lineHeight": "1.6",
    },
    children=[
        html.H1("Contexto", style={"textAlign": "center", "marginBottom": "30px"}),

        html.P(
            """
            Para el desarrollo de este proyecto se empleó el dataset “Global Coffee Health Dataset”,
            disponible públicamente en la plataforma Kaggle. Este conjunto de datos reúne 10.000
            registros provenientes de 20 países, con información detallada relacionada con patrones
            de consumo de café, indicadores de salud y hábitos de vida.
            """
        ),

        html.P(
            """
            El dataset incluye variables demográficas, niveles diarios de ingesta de café y cafeína,
            duración y calidad del sueño, índice de masa corporal (BMI), frecuencia cardíaca, niveles
            de estrés, actividad física, condiciones de salud, ocupación, hábitos de tabaquismo y
            consumo de alcohol, entre otras.
            """
        ),

        html.P(
            """
            Además, captura relaciones ampliamente documentadas en la literatura científica, como
            los efectos del consumo de cafeína sobre el sueño, el estrés y otros indicadores
            fisiológicos. Gracias a esta estructura rica y multidimensional, el dataset resulta
            adecuado para realizar análisis estadísticos, exploración de correlaciones, visualización
            de datos y estudios sobre bienestar, estilos de vida y salud poblacional.
            """
        ),
    ]
)
