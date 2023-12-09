import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Leer el CSV y filtrar los datos
data = pd.read_csv("Amazon_Adidas.csv")
filtered_data = data[data['Precio'] > 100]

# Crear la gráfica
fig = px.bar(filtered_data, x='Nombre', y='Precio', color='Envio_p', title='Productos con Precio > $100')

# Configuración de la aplicación Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H2("Gráfica de productos con Precio > $100"),
    dcc.Graph(figure=fig)
])

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
