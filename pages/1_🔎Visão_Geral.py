import pandas as pd
import numpy as np
import folium
import sys
import os
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# Adiciona o caminho da pasta 'utils' ao sys.path
sys.path.append(os.path.abspath(os.path.join('..', 'utils')))
from utils import plots_geral as upg

#####============================================================================================================================================#####
# Configuração e leitura de dados
#####============================================================================================================================================#####

data_path = "data/zomato_processed.csv"
df_oficial = pd.read_csv(data_path)
df = df_oficial.copy()

#####============================================================================================================================================#####
#####============================================================================================================================================#####


#####============================================================================================================================================#####
# CONFIGURAÇÃO PÁGINA
#####============================================================================================================================================#####

st.set_page_config(
    page_title='Visão Geral',
    page_icon='🔎',
    layout='wide'
)

#####============================================================================================================================================#####
#####============================================================================================================================================#####


#####============================================================================================================================================#####
# BARRA LATERAL
#####============================================================================================================================================#####
image_path = 'logo/logo.jpg'
image = Image.open(image_path)
st.sidebar.image(image)
st.sidebar.markdown('# :red[ZOMATO RESTAURANTS]')

st.sidebar.markdown("---")

st.sidebar.markdown('### Filtro:')
country_options = st.sidebar.multiselect(
    'Selecione os Países',
    ['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada', 'Singapore', 'United Arab Emirates', 'India', 'Indonesia', 
     'New Zealand', 'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey'],
    default=['Brazil', 'India', 'United States of America', 'England', 'South Africa']
)

# Filtro
linhas_selecionadas = df['country_name'].isin(country_options)
df_filtrado = df.loc[linhas_selecionadas, :]

#####============================================================================================================================================#####
# GRÁFICOS
#####============================================================================================================================================#####
# Gráfico de restaurantes no mapa
df = df_filtrado.copy()
cols = ['restaurant_name', 'latitude', 'longitude', 'average_cost_for_two', 'cuisines', 'aggregate_rating', 'currency', 'color_name']
mapa_html = upg.mapa(df, cols)

#####============================================================================================================================================#####
# VISÃO GERAL
#####============================================================================================================================================#####
st.markdown("# 🔎 Visão Geral")
st.subheader('Métricas Gerais', divider='grey')

df = df_oficial.copy()

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        # Quantos restaurantes únicos estão registrados?
        restaurantes_unicos = df['restaurant_id'].nunique()
        col1.metric(label='Restaurantes', value=restaurantes_unicos)
    with col2:
        # Quantos países únicos estão registrados?
        paises_unicos = df['country_name'].nunique()
        col2.metric(label='Países', value=paises_unicos)
    with col3:
        # Quantas cidades únicas estão registradas?
        cidades_unicas = df['city'].nunique()
        col3.metric(label='Cidades', value=cidades_unicas)
    with col4:
        # Qual o total de avaliações feitas?
        avaliacao_geral = df['votes'].sum()
        col4.metric(label='Avaliações', value=avaliacao_geral)
    with col5:
        # Qual o total de tipos de culinária registrados?
        culinarias_unicas = df['cuisines'].nunique()
        col5.metric(label='Culinárias', value=culinarias_unicas)

st.subheader('Localização dos Restaurantes', divider='grey')
# Mostrando o mapa usando o componente HTML do Streamlit
with st.container():
    components.html(mapa_html, width = 1024, height=600)
