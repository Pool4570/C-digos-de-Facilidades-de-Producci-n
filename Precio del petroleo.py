# Importar las librerí­as
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Crear un DataFrame con los datos
data = {
    'Año': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Precio (USD/barril)': [96.29, 49.49, 40.76, 52.51, 69.78, 64.04, 41.47, 69.72, 85.4, 82.95]
}
df = pd.DataFrame(data)

# Crear un gráfico de lí­nea con Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(df['Año'], df['Precio (USD/barril)'], marker='o', label='Precio del petróleo')
plt.xlabel('Año')
plt.ylabel('Precio (USD/barril)')
plt.title('Tendencia del precio del petróleo (2014-2023)')
plt.grid(True)
plt.legend()
plt.show()

# Crear un gráfico interactivo con Plotly
fig = px.line(df, x='Año', y='Precio (USD/barril)', title='Tendencia del precio del petróleo (2014-2023)')
fig.show()

# Crear un gráfico de tendencia con Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x='Año', y='Precio (USD/barril)', data=df)
plt.xlabel('Año')
plt.ylabel('Precio (USD/barril)')
plt.title('Tendencia del precio del petróleo (2014-2023)')
plt.grid(True)
plt.show()
