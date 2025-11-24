import dash
from dash import html, dcc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import (
    kstest, norm, chi2_contingency, shapiro, 
    ks_2samp, ttest_ind, mannwhitneyu
)
from sklearn.impute import SimpleImputer, KNNImputer
import geopandas as gpd
import folium
from folium import Choropleth, Marker, Popup
from shapely.geometry import Point
import warnings

# --- Nuevas librerías necesarias para Plotly y el Modelo Predictivo ---
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# --------------------------------------------------------------------

warnings.filterwarnings("ignore")

dash.register_page(__name__, path="/resultados", name="Resultados y Análisis", order=6) # Nombre claro para la navegación

# --- LECTURA Y PREPARACIÓN DE DATOS ---
df = pd.read_csv("data/synthetic_coffee_health_10000.csv")

# Función para crear la columna Health_Risk, replicando la lógica de tu notebook.
def compute_health_risk(row):
    """Calcula el riesgo de salud (1=Alto, 0=Bajo) basado en un sistema de puntos."""
    score = 0
    # Asignación de puntos según la lógica identificada en el notebook
    if row['Coffee_Intake'] > 4: score += 2
    if row['Sleep_Hours'] < 6: score += 2
    if row['BMI'] > 25: score += 1
    if row['Heart_Rate'] > 80: score += 1
    if row['Stress_Level'] == 'Medium': score += 1
    if row['Stress_Level'] == 'High': score += 2
    if row['Smoking'] == 1: score += 2
    if row['Alcohol_Consumption'] == 1: score += 1
    if row['Sleep_Quality'] == 'Poor': score += 2
    if row['Sleep_Quality'] == 'Fair': score += 1
    return 1 if score >= 6 else 0

df_tratado = df.copy()
df_tratado["Health_Risk"] = df_tratado.apply(compute_health_risk, axis=1)
# Mapear la variable objetivo a etiquetas de texto para mejor visualización
df_tratado['Health_Risk_Label'] = df_tratado['Health_Risk'].map({0: 'Low Risk', 1: 'High Risk'})

# --- FUNCIONES DE GENERACIÓN DE GRÁFICOS CON PLOTLY (Mantenidas) ---
# ... Las funciones get_univariate_plots, get_bivariate_plots, get_geographic_plot, get_model_analysis
#     se mantienen IGUAL, ya que devuelven los bloques de html.Div con los gráficos.
# (Por brevedad, omito el código de estas funciones en la respuesta, asumiendo que ya lo tienes.)

# --- FUNCIONES DE GENERACIÓN DE GRÁFICOS CON PLOTLY ---
def get_univariate_plots(df):
    """Genera gráficos de análisis univariado."""
    # 1. Coffee Intake (Histograma con boxplot marginal)
    fig_coffee = px.histogram(
        df, x='Coffee_Intake', marginal='box',
        title='Distribución de Consumo de Café (Tazas)',
        labels={'Coffee_Intake': 'Consumo de Café (Tazas)', 'count': 'Frecuencia'},
        color_discrete_sequence=['#4c78a8']
    )
    fig_coffee.update_layout(bargap=0.05)

    # 2. Sleep Hours (Histograma)
    fig_sleep = px.histogram(
        df, x='Sleep_Hours', marginal='box',
        title='Distribución de Horas de Sueño',
        labels={'Sleep_Hours': 'Horas de Sueño', 'count': 'Frecuencia'},
        color_discrete_sequence=['#f58518']
    )
    fig_sleep.update_layout(bargap=0.05)
    
    # 3. Stress Level (Gráfico de barras)
    stress_order = ['Low', 'Medium', 'High']
    stress_counts = df['Stress_Level'].value_counts().reindex(stress_order)
    
    fig_stress = px.bar(
        stress_counts, x=stress_counts.index, y=stress_counts.values,
        title='Distribución de Nivel de Estrés',
        labels={'x': 'Nivel de Estrés', 'y': 'Frecuencia'},
        color=stress_counts.index,
        color_discrete_map={'Low': '#54a24b', 'Medium': '#f58518', 'High': '#e45756'}
    )
    fig_stress.update_xaxes(categoryorder='array', categoryarray=stress_order)
    
    # 4. Heart Rate (Histograma)
    fig_hr = px.histogram(
        df, x='Heart_Rate', marginal='box',
        title='Distribución de Frecuencia Cardíaca (BPM)',
        labels={'Heart_Rate': 'Frecuencia Cardíaca (BPM)', 'count': 'Frecuencia'},
        color_discrete_sequence=['#72b7b2']
    )
    fig_hr.update_layout(bargap=0.05)
    
    # 5. BMI (Histograma)
    fig_bmi = px.histogram(
        df, x='BMI', marginal='box',
        title='Distribución del Índice de Masa Corporal (BMI)',
        labels={'BMI': 'BMI', 'count': 'Frecuencia'},
        color_discrete_sequence=['#e45756']
    )
    fig_bmi.update_layout(bargap=0.05)


    return html.Div([
        html.Div([
            dcc.Graph(figure=fig_coffee),
            dcc.Graph(figure=fig_sleep)
        ], style={'display': 'flex', 'flex-direction': 'row'}),
        html.Div([
            dcc.Graph(figure=fig_stress),
        ], style={'display': 'flex', 'flex-direction': 'row'}),
        html.Div([
            dcc.Graph(figure=fig_hr),
            dcc.Graph(figure=fig_bmi)
        ], style={'display': 'flex', 'flex-direction': 'row'}),
    ])


def get_bivariate_plots(df):
    """Genera gráficos de análisis bivariado."""
    health_risk_order = ['Low Risk', 'High Risk']
    stress_order = ['Low', 'Medium', 'High']
    
    # 1. Coffee Intake vs Stress Level (Boxplot - como en tu notebook)
    fig_coffee_stress = px.box(
        df, x='Stress_Level', y='Coffee_Intake',
        title='Consumo de Café (Tazas) por Nivel de Estrés',
        labels={'Stress_Level': 'Nivel de Estrés', 'Coffee_Intake': 'Consumo de Café (Tazas)'},
        color='Stress_Level',
        category_orders={"Stress_Level": stress_order},
        color_discrete_map={'Low': '#54a24b', 'Medium': '#f58518', 'High': '#e45756'}
    )
    
    # 2. Coffee Intake vs Sleep Hours (Scatter Plot con línea de tendencia)
    fig_coffee_sleep = px.scatter(
        df, x='Coffee_Intake', y='Sleep_Hours',
        opacity=0.5, trendline='ols',
        title='Consumo de Café vs Horas de Sueño',
        labels={'Coffee_Intake': 'Consumo de Café (Tazas)', 'Sleep_Hours': 'Horas de Sueño'}
    )
    
    # 3. BMI vs Heart Rate (Scatter Plot con línea de tendencia)
    fig_bmi_hr = px.scatter(
        df, x='BMI', y='Heart_Rate',
        opacity=0.5, trendline='ols',
        title='BMI vs Frecuencia Cardíaca',
        labels={'BMI': 'Índice de Masa Corporal (BMI)', 'Heart_Rate': 'Frecuencia Cardíaca (BPM)'}
    )
    
    # 4. Coffee Intake vs Health Risk (Violin Plot)
    fig_coffee_risk = px.violin(
        df, x='Health_Risk_Label', y='Coffee_Intake',
        box=True, # Muestra un box plot interno
        title='Distribución de Consumo de Café por Riesgo de Salud',
        labels={'Health_Risk_Label': 'Riesgo de Salud', 'Coffee_Intake': 'Consumo de Café (Tazas)'},
        color='Health_Risk_Label',
        category_orders={"Health_Risk_Label": health_risk_order},
        color_discrete_map={'Low Risk': '#4c78a8', 'High Risk': '#e45756'}
    )

    return html.Div([
        html.Div([
            dcc.Graph(figure=fig_coffee_stress),
            dcc.Graph(figure=fig_coffee_sleep)
        ], style={'display': 'flex', 'flex-direction': 'row'}),
        html.Div([
            dcc.Graph(figure=fig_bmi_hr),
            dcc.Graph(figure=fig_coffee_risk)
        ], style={'display': 'flex', 'flex-direction': 'row'}),
    ])


def get_geographic_plot(df):
    """Genera el gráfico de coropletas de consumo de café por país."""
    # Calcular el consumo promedio de café por país
    df_country_avg = df.groupby('Country')['Coffee_Intake'].mean().reset_index()
    df_country_avg.columns = ['Country', 'Avg_Coffee_Intake']
    
    # Crear el mapa de coropletas
    fig_map = px.choropleth(
        df_country_avg,
        locations='Country',
        locationmode='country names', # Plotly intentará mapear los nombres de países a códigos
        color='Avg_Coffee_Intake',
        hover_name='Country',
        color_continuous_scale=px.colors.sequential.Plasma,
        title='Consumo Promedio de Café por País (Tazas)',
        labels={'Avg_Coffee_Intake': 'Consumo Promedio de Café (Tazas)'}
    )
    
    fig_map.update_geos(
        showcoastlines=True, coastlinecolor="Black",
        showland=True, landcolor="#f0f0f0",
        showocean=True, oceancolor="#99ccee",
        showcountries=True, countrycolor="Black",
        projection_type="natural earth"
    )
    fig_map.update_layout(margin={"r":0,"t":40,"l":0,"b":0}) # Ajustar márgenes
    
    return dcc.Graph(figure=fig_map)


def get_model_analysis(df):
    """Entrena el modelo de Random Forest, calcula métricas e importancia de características."""
    
    # 1. Preparación de datos para el modelo (SIN CAMBIOS)
    X = df.drop(columns=['ID', 'Health_Issues', 'Caffeine_mg', 'Health_Risk', 'Health_Risk_Label'])
    y = df['Health_Risk'] 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    
    # 2. Preprocesador y Pipeline (SIN CAMBIOS)
    numerical_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ],
        remainder='passthrough'
    )
    
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1))
    ])
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # 3. CÁLCULO DE MÉTRICAS (Mantenemos el cálculo por si se requiere en el futuro, pero no se muestra)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # 4. REEMPLAZO DE LA TABLA POR LA IMAGEN
    metrics_image = html.Img(
        # La imagen de las métricas que subiste
        src='/assets/model_results.jpg', 
        alt='Tabla de Métricas del Modelo Predictivo (Accuracy, Precision, Recall, F1)',
        style={
            'width': '100%',            # Ocupa todo el ancho disponible del contenedor
            'maxWidth': '450px',        # Limita el ancho máximo para que no se estire demasiado
            'height': 'auto',
            'display': 'block',
            'margin': '20px auto',      # Centra la imagen horizontalmente
            'borderRadius': '8px',
            'boxShadow': '0 4px 8px rgba(0,0,0,0.1)'
        }
    )
    
    # 5. Importancia de Características (Feature Importance) (SIN CAMBIOS)
    feature_importances = model.named_steps['classifier'].feature_importances_
    
    ohe_feature_names = model.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out(categorical_features)
    final_feature_names = list(numerical_features) + list(ohe_feature_names)
    
    importance_df = pd.DataFrame({
        'Feature': final_feature_names,
        'Importance': feature_importances
    }).sort_values(by='Importance', ascending=False)

    # Gráfico de Importancia de Características (SIN CAMBIOS)
    fig_importance = px.bar(
        importance_df.head(15), x='Importance', y='Feature', orientation='h',
        title='Top 15 Importancia de Características para Riesgo de Salud',
        labels={'Importance': 'Importancia (Gini)', 'Feature': 'Característica'},
        color='Importance',
        color_continuous_scale=px.colors.sequential.Teal
    )
    fig_importance.update_layout(yaxis={'categoryorder':'total ascending'})

    return html.Div([
        html.H3("Métricas de Rendimiento"),
        # Insertamos la imagen en lugar del dcc.Markdown de la tabla
        metrics_image, 
        html.Br(),
        html.H3("Importancia de Características"),
        dcc.Graph(figure=fig_importance)
    ])


# Pre-calcular los componentes para el layout (buena práctica en Dash)
UNIVARIATE_GRAPHS = get_univariate_plots(df_tratado)
BIVARIATE_GRAPHS = get_bivariate_plots(df_tratado)
GEOGRAPHIC_MAP = get_geographic_plot(df_tratado)
MODEL_RESULTS_DIV = get_model_analysis(df_tratado)


def layout():
    return html.Div(
        style={"padding": "40px"},
        children=[

            html.H1("Resultados y Análisis de Datos", style={"textAlign": "center"}),
            html.Hr(),
            html.Br(),

            # --------------------------------------------
            # USO DE dcc.Tabs PARA SECCIONES
            # --------------------------------------------
            dcc.Tabs(id="results-tabs", value='tab-1', children=[
                
                # Pestaña 1: Análisis Univariado
                dcc.Tab(label='1. Análisis Univariado', value='tab-1', children=[
                    html.Div(style={'padding': '20px'}, children=[
                        dcc.Markdown("""
                        En esta sección se presentan las **distribuciones de variables clave** del dataset,
                        como: Consumo de café, Horas de sueño, Niveles de estrés, Frecuencia cardíaca e Índice de masa corporal (BMI).
                        """),
                        html.Hr(),
                        html.Div(children=UNIVARIATE_GRAPHS, id="univariado-graficos"),
                    ])
                ]),

                # Pestaña 2: Análisis Bivariado
                dcc.Tab(label='2. Análisis Bivariado', value='tab-2', children=[
                    html.Div(style={'padding': '20px'}, children=[
                        dcc.Markdown("""
                        Se exploran **relaciones y correlaciones** entre variables, incluyendo:
                        Coffee Intake vs Stress Level, Coffee Intake vs Sleep Duration, BMI vs Heart Rate, y Coffee Intake vs Health Risk.
                        """),
                        html.Hr(),
                        html.Div(children=BIVARIATE_GRAPHS, id="bivariado-graficos"),
                    ])
                ]),
                
                # Pestaña 3: Visualización Geográfica
                dcc.Tab(label='3. Mapa Geográfico', value='tab-3', children=[
                    html.Div(style={'padding': '20px'}, children=[
                        dcc.Markdown("""
                        Mapa mundial que muestra la **distribución geográfica del Consumo Promedio de Café** por país.
                        (Nota: La granularidad depende de la representación de países en Plotly).
                        """),
                        html.Hr(),
                        html.Div(children=GEOGRAPHIC_MAP, id="mapa-geografico"),
                    ])
                ]),

                # Pestaña 4: Modelo Predictivo
                dcc.Tab(label='4. Modelo Predictivo', value='tab-4', children=[
                    html.Div(style={'padding': '20px'}, children=[
                        dcc.Markdown("""
                        Resultados del **Modelo Random Forest** entrenado para predecir el Riesgo de Salud.
                        Se muestran métricas de rendimiento y la importancia de las características.
                        """),
                        html.Hr(),
                        html.Div(children=MODEL_RESULTS_DIV, id="modelo-predictivo"),
                    ])
                ]),
            ]),

            html.Br(),
            html.P("El dashboard integra los resultados visuales y analíticos más importantes del proyecto.")
        ]
    )

def get_layout():
    return layout()