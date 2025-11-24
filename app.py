import dash
from dash import html, dcc

# Inicialización de la aplicación Dash
# La propiedad 'pages_folder' le dice a Dash dónde buscar los archivos .py de las páginas
#app = dash.Dash(__name__, use_pages=True, pages_folder="pages")
EXTERNAL_STYLESHEETS = [
    # Puedes usar un tema de Bootstrap. 'flatly' o 'lumen' son buenos para estilos formales.
    'https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/flatly/bootstrap.min.css' 
]

app = dash.Dash(__name__, 
                use_pages=True, 
                pages_folder="pages", 
                external_stylesheets=EXTERNAL_STYLESHEETS)
# Estilo básico para el menú de navegación (opcional, pero recomendado)
navbar_style = {
    "display": "flex",
    "justify-content": "space-around",
    "padding": "10px",
    "backgroundColor": "#f8f9fa",
    "boxShadow": "0 2px 4px 0 rgba(0,0,0,.1)",
    "marginBottom": "20px"
}

# --- Layout principal del Dashboard ---
app.layout = html.Div([
    html.H1("☕ Dashboard de Consumo de Café y Salud", 
            style={'textAlign': 'center', 'color': '#343a40', 'paddingTop': '20px'}),
    
    # 1. Menú de Navegación (Enlaces a cada página)
    html.Div(
        style=navbar_style,
        children=[
            dcc.Link(
                f"{page['name']}", href=page["relative_path"],
                style={'padding': '10px', 'textDecoration': 'none', 'color': '#007bff'}
            ) for page in dash.page_registry.values()
        ]
    ),
    
    html.Hr(),
    
    # 2. Contenedor para el Contenido de la Página
    # Aquí se renderizará el layout del archivo .py de la página seleccionada
    dash.page_container
])

# Ejecución del servidor local
if __name__ == "__main__":
    # debug=True permite recarga automática al guardar cambios
    app.run(debug=True, host='0.0.0.0')