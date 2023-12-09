import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, dash_table, callback, Input, Output

# Cargar el nuevo conjunto de datos
data_nike_adidas = pd.read_csv("Amazon_Nike_norm.csv")

def generate_page(data):
    data_resumen = data.groupby("Nombre", as_index=False).sum(numeric_only=True)

    # Crear la página del dashboard
    pagina = html.Div([
        html.H2("Dashboard Nike_Adidas"),
        html.P("Objetivo: Mostrar los resultados de Nike y Adidas"),
        html.Hr(),
        dcc.Dropdown(options=[{'label': 'Precio', 'value': 'Precio'}, {'label': 'Envio_p', 'value': 'Envio_p'}], value="Precio", id="dpColumn"),
        dcc.Graph(figure={}, id="fig_Column"),
        dash_table.DataTable(data=data_resumen.to_dict("records"), page_size=15, id="tbl")
    ])
    return pagina

# Callback para actualizar la gráfica según la columna seleccionada
@callback(
    Output(component_id="fig_Column", component_property="figure"),
    Input(component_id="dpColumn", component_property="value")
)
def update_grafica(column_chosen):
    data_resumen = data_nike_adidas.groupby("Nombre", as_index=False).sum(numeric_only=True)
    fig = px.line(data_resumen, x="Nombre", y=column_chosen)
    return fig

# Inicio del programa
if __name__ == "__main__":
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = generate_page(data_nike_adidas)
    app.run_server(debug=True)
