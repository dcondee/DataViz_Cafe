import dash
from dash import html, dcc

def layout():
    return html.Div(
        style={"padding": "40px"},
        children=[
            html.H1("Metodología del Proyecto", style={"textAlign": "center"}),

            html.H2("1. Recolección de Datos"),
            dcc.Markdown("""
El proyecto parte del dataset **Global Coffee Health Dataset**, el cual contiene información detallada sobre consumo de café, indicadores de salud, hábitos de sueño, actividad física y datos demográficos de múltiples países.

Este conjunto de datos permite analizar patrones reales de consumo, explorar su relación con la salud y desarrollar soluciones basadas en técnicas de análisis estadístico y aprendizaje automático.
            """),

            html.H2("2. Análisis Exploratorio de Datos (EDA)"),
            dcc.Markdown("""
Se realizó un análisis exploratorio inicial para comprender la estructura del dataset y detectar patrones relacionados con:

- Distribución del consumo de café por país.
- Relación entre consumo de café y horas de sueño.
- Asociación entre *Coffee Intake* y variables fisiológicas como **BMI** y **heart rate**.
- Evaluación de correlaciones entre los indicadores de salud.

Este análisis permitió orientar la construcción de las visualizaciones y el enfoque del modelo predictivo.
            """),

            html.H2("3. Limpieza y Preparación de Datos"),
            dcc.Markdown("""
La fase de preparación incluyó:

- Manejo de valores faltantes mediante imputación.
- Homogeneización y estandarización de nombres de países para permitir uniones geográficas.
- Conversión de variables categóricas mediante *One Hot Encoding*.
- Normalización y revisión de valores atípicos cuando fue necesario.

Estas transformaciones aseguran una base sólida para la visualización y el modelado.
            """),

            html.H2("4. Feature Engineering"),
            dcc.Markdown("""
Con el propósito de desarrollar un modelo predictivo útil y alineado con los objetivos del proyecto, se construyó una **variable objetivo** basada en indicadores de salud presentes en la base de datos.

La nueva variable binaria **Health Risk** permite clasificar a una persona como:

- **1** → si presenta o está en riesgo de presentar problemas de salud de acuerdo con las condiciones registradas.
- **0** → en caso contrario.

Este proceso de *feature engineering* fue clave para transformar los registros originales en un problema de clasificación supervisada.
            """),

            html.H2("5. Modelado Predictivo"),
            dcc.Markdown("""
Para predecir si una persona podría presentar problemas de salud relacionados con los hábitos y características registradas, se desarrolló un modelo basado en la arquitectura de **Random Forest**.

Las razones para elegir este modelo incluyen:

- Maneja bien variables categóricas y numéricas.
- Es robusto ante ruido y valores atípicos.
- Captura interacciones no lineales entre variables.
- Ofrece interpretabilidad mediante la importancia de características (*feature importance*).

El proceso incluyó:

1. División en *train/test*.  
2. Codificación de variables categóricas mediante `ColumnTransformer`.  
3. Entrenamiento del modelo *RandomForestClassifier*.  
4. Evaluación mediante métricas como accuracy, precision, recall y F1-score.

El modelo será integrado dentro del dashboard para permitir análisis interactivos y predicciones basadas en los datos ingresados.
            """),

            html.Br(),
            html.Hr(),

            html.P("Esta sección describe el flujo metodológico aplicado para la construcción del proyecto, desde el análisis inicial hasta el desarrollo del modelo predictivo."),
        ]
    )

def get_layout():
    return layout()
