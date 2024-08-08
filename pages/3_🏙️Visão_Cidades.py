import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import sys
import os
import streamlit as st
from PIL import Image

#####============================================================================================================================================#####
#####============================================================================================================================================#####

# Adiciona o caminho da pasta 'utils' ao sys.path
sys.path.append(os.path.abspath(os.path.join('..', 'utils')))
from utils import plots_city as upy

data_path = f"data/zomato_processed.csv"
df_oficial = pd.read_csv(data_path)
df = df_oficial.copy()

#####============================================================================================================================================#####
#####============================================================================================================================================#####


#####============================================================================================================================================#####
# CONFIGURAÇÃO PÁGINA
#####============================================================================================================================================#####

st.set_page_config(
    page_title='Visão Cidades',
    page_icon='🏙️',
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
    default = ['Brazil', 'India', 'United States of America', 'England', 'South Africa']
)

# Filtro
linhas_selecionadas = df['country_name'].isin(country_options)
df_filtrado = df.loc[linhas_selecionadas, :]

#####============================================================================================================================================#####
#####============================================================================================================================================#####

#####============================================================================================================================================#####
# GRÁFICOS
#####============================================================================================================================================#####

# Quantidade de Restaurantes nas 10 Cidades com mais Cadastros de Restaurantes no País
cols = ['country_name', 'city', 'restaurant_id']
df = df_filtrado.copy()
x = 'city'
y = 'restaurant_id'
z = 'country_name'
operacao = pd.Series.nunique
title = 'Quantidade de Restaurantes nas 10 Cidades com mais Cadastros de Restaurantes no País'
xaxis_title = 'Cidades'
yaxis_title = 'Quantidade de Restaurantes'
legend_title_text = 'Países'

restaurantes_por_cidade = upy.cities_bar_plot(df, cols, x, y, z, operacao, ascending = [True, False], title = title, xaxis_title = xaxis_title, yaxis_title = yaxis_title, legend_title_text = legend_title_text)

#####============================================================================================================================================#####
#####============================================================================================================================================#####

# Quantidade de Restaurantes com a Média de Avaliação maior que 4.0 nas 10 Cidades com mais Cadastros do País
cols = ['country_name', 'city', 'aggregate_rating', 'restaurant_id']
df = df_filtrado.copy()
lines = df['aggregate_rating'] >= 4.0
x = 'city'
y = 'restaurant_id'
z = 'country_name'
r = 'aggregate_rating'
operacao = ['mean', 'nunique']
title = 'Quantidade de Restaurantes com a Média de Avaliação maior que 4.0 nas 10 Cidades com mais Cadastros do País'
xaxis_title = 'Cidades'
yaxis_title = 'Quantidade de Restaurantes'
legend_title_text = 'Países'

restaurantes_4stars_por_cidade = upy.cities_rank_bar_plot(df, lines, cols, x, y, z, r, operacao, ascending = [True, False], title = title, xaxis_title = xaxis_title, yaxis_title = yaxis_title, legend_title_text = legend_title_text)

#####============================================================================================================================================#####
#####============================================================================================================================================#####

# Quantidade de Restaurantes com a Média de Avaliação menor que 3.0 nas 10 Cidades com mais Cadastros do País
cols = ['country_name', 'city', 'aggregate_rating', 'restaurant_id']
df = df_filtrado.copy()
lines = df['aggregate_rating'] <= 3.0
x = 'city'
y = 'restaurant_id'
z = 'country_name'
r = 'aggregate_rating'
operacao = ['mean', 'nunique']
title = 'Quantidade de Restaurantes com a Média de Avaliação menor que 3.0 nas 10 Cidades com mais Cadastros do País'
xaxis_title = 'Cidades'
yaxis_title = 'Quantidade de Restaurantes'
legend_title_text = 'Países'

restaurantes_3stars_por_cidade = upy.cities_rank_bar_plot(df, lines, cols, x, y, z, r, operacao, ascending = [True, False], title = title, xaxis_title = xaxis_title, yaxis_title = yaxis_title, legend_title_text = legend_title_text)

#####============================================================================================================================================#####
#####============================================================================================================================================#####

# Quantidade de Restaurantes com Culinária Distinta nas 10 Cidades com mais Cadastros do País
cols = ['country_name', 'city', 'cuisines']
df = df_filtrado.copy()
x = 'city'
y = 'cuisines'
z = 'country_name'
operacao = pd.Series.nunique
title = 'Quantidade de Restaurantes com Culinária Distinta nas 10 Cidades com mais Cadastros do País'
xaxis_title = 'Cidades'
yaxis_title = 'Quantidade de Restaurantes'
legend_title_text = 'Países'

culinaria_por_cidade = upy.cities_bar_plot(df, cols, x, y, z, operacao, ascending = [True, False], title = title, xaxis_title = xaxis_title, yaxis_title = yaxis_title, legend_title_text = legend_title_text)

#####============================================================================================================================================#####
#####============================================================================================================================================#####


#####============================================================================================================================================#####
# VISÃO CIDADES
#####============================================================================================================================================#####

st.markdown("# 🏙️ Visão Cidades")
st.markdown('---')

with st.container():
    st.plotly_chart(restaurantes_por_cidade, use_container_width = True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(restaurantes_4stars_por_cidade, use_container_width = True)
    with col2:
        st.plotly_chart(restaurantes_3stars_por_cidade, use_container_width = True)

with st.container():
    st.plotly_chart(culinaria_por_cidade, use_container_width = True)
