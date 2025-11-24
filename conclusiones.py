import dash
from dash import html, dcc

# Registrar la página
dash.register_page(__name__, path="/conclusiones", name="Conclusiones y Recomendaciones", order=7)

def layout():
    return html.Div(
        # Limitamos el ancho y centramos el contenido
        style={"padding": "40px", "maxWidth": "850px", "margin": "0 auto"},
        children=[
            
            # 1. ICONO SUPERIOR DE CONCLUSIÓN
            html.Img(
                src='/assets/conclusion.png', 
                alt='Icono de Conclusión y Éxito',
                style={
                    'display': 'block',
                    'margin': '0 auto 30px auto', # Centrado y margen inferior
                    'height': '150px',
                }
            ),

            html.H1("Conclusiones y Sugerencias Finales", 
                    className="display-5",
                    style={"textAlign": "center", 'marginBottom': '40px'}),
            
            html.Hr(),

            # --- 2. Conclusiones Clave ---
            html.H2("✅ Conclusiones Clave del Análisis", style={'color': '#20B2AA'}), # Color para resaltar el éxito
            
            # Usamos una lista HTML sencilla con dcc.Markdown para mejor formato de texto
            html.Ul(
                style={'listStyleType': 'none', 'paddingLeft': '0'},
                children=[
                    html.Li(dcc.Markdown("""
                        **🧠 El Nivel de Estrés es el Factor Más Influyente:** El modelo de Random Forest demostró que la variable **Stress_Level** fue la característica con mayor importancia para predecir el Riesgo de Salud, superando a todos los factores relacionados con el café.
                    """)),
                    html.Li(dcc.Markdown("""
                        **☕ Consumo y Riesgo (Umbral):** El análisis bivariado mostró una clara tendencia: los individuos clasificados con **Alto Riesgo de Salud** tienen una distribución de Consumo de Café significativamente mayor, con una media superior a **4 tazas diarias** como punto de inflexión.
                    """)),
                    html.Li(dcc.Markdown("""
                        **📉 Correlaciones Indirectas:** Existe una correlación inversa notable entre **Consumo de Café** y **Horas de Sueño** (mayor café, menos sueño), lo cual impacta directamente el bienestar y refuerza la necesidad de moderación en el consumo vespertino.
                    """)),
                ]
            ),
            
            html.Hr(style={'marginTop': '40px'}),

            # --- 3. Recomendaciones ---
            html.H2("💡 Recomendaciones y Estrategias Sugeridas", style={'color': '#FF8C00'}), # Color para resaltar la acción
            
            # Usamos un dcc.Markdown con estructura de lista numerada y blockquote para destacarla
            dcc.Markdown("""
            1.  **Moderación del Consumo:** Se recomienda enfáticamente **limitar el consumo de café a 3 tazas o menos** por día para la población general, especialmente en individuos con historial de alto estrés o problemas de sueño.
            2.  **Manejo del Estrés como Prioridad:** Dado que el estrés es el predictor más fuerte, cualquier programa de salud debe enfocarse prioritariamente en técnicas de **manejo y reducción de estrés** (ej. meditación o ejercicio) como medida preventiva principal.
            3.  **Seguimiento al Sueño:** Es crucial promover la concientización para garantizar **más de 7 horas de sueño** de calidad, ya que la deficiencia del sueño actúa como un factor que potencia el riesgo de salud asociado a otros hábitos.
            """, className="blockquote"),
            
            html.Hr(style={'marginTop': '40px'}),
            
            # --- 4. Próximos Pasos ---
            html.H3("🚀 Próximos Pasos y Desarrollo Futuro", className="text-info"),
            dcc.Markdown("""
            Se podría incluir una **sección interactiva** donde el usuario ingrese sus propios datos (Consumo, Horas de Sueño, Estrés, etc.) y obtenga una **predicción inmediata** de su Riesgo de Salud utilizando el modelo entrenado. Esto transformaría el Dashboard de una herramienta de análisis a una herramienta de utilidad directa para el usuario.
            """)
        ]
    )