import pandas as pd
import plotly.express as px

data = pd.read_csv("Amazon_Adidas_norm.csv")

# Filtrar datos con precios mayores a 100
data_precios_mayores_a_100 = data[data['Precio'] > 100]

# Gráfica de Línea
fig_line = px.line(data_precios_mayores_a_100, x="Nombre", y="Precio", title="Gráfica de Línea")
# fig_line.show()

# Gráfica de Caja y Bigotes
fig_box = px.box(data_precios_mayores_a_100, y="Precio", title="Gráfica de Caja y Bigotes")
# fig_box.show()

# Gráfica de Área
areafig = px.area(data_precios_mayores_a_100, x="Nombre", y="Precio", title="Gráfica de Área")
# areafig.show()

# Gráfica de Barras
data_precios_mayores_a_100.Date = pd.to_datetime(data_precios_mayores_a_100.Date)
data2 = data_precios_mayores_a_100.set_index("Date")
data_mes = data2.resample(rule="M").mean()
data_mes = data_mes.reset_index()
barras = px.bar(data_mes, x="Date", y="Precio", title="Gráfica de Barras")
barras.update_layout(xaxis_title="Mes", yaxis_title="Dólar($)", title="Stocks Mensuales")
# barras.show()

# Gráfica de Histograma
histograma = px.histogram(data_precios_mayores_a_100, x="Nombre", y="Precio", title="Gráfica de Histograma")
# histograma.show()

# Gráfica de Pastel
df_tips = px.data.tips()
fig_pastel = px.pie(df_tips, values="total_bill", names="day", title="Gráfica de Pastel")
fig_pastel.show()
