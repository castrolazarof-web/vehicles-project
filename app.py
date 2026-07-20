import pandas as pd
import plotly.graph_objects as go
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de anuncios de venta de coches')
st.write('Esta aplicación permite explorar el conjunto de datos de anuncios de venta de coches en EE.UU., '
         'mostrando la distribución del odómetro y la relación entre el odómetro y el precio.')

build_histogram = st.checkbox('Construir histograma del odómetro')

if build_histogram:
    st.write('Distribución del odómetro para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir gráfico de dispersión (Odómetro vs Precio)')

if build_scatter:
    st.write('Relación entre el odómetro y el precio de los vehículos')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig, use_container_width=True)
