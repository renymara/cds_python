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
from utils import plots_country as upc

data_path = f"data/zomato_processed.csv"
df_oficial = pd.read_csv(data_path)
df = df_oficial.copy()

#####============================================================================================================================================#####
#####============================================================================================================================================#####


#####============================================================================================================================================#####
# CONFIGURAÇÃO PÁGINA
#####============================================================================================================================================#####

st.set_page_config(
    page_title='Visão Países',
    page_icon='# :earth_americas:',
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

# Quantidade de restaurantes registrados por país
cols = ['restaurant_id', 'country_name']
df = df_filtrado.copy()
x = 'country_name'
y = 'restaurant_id'
operacao = pd.Series.nunique
title = 'Quantidade de Restaurantes por País'
xaxis_title = 'País'
yaxis_title = 'Quantidade de Restaurantes'
legend_title_text = 'Países'

# Gráfico de quantidade de restaurantesa por país
fig_restaurantes_por_pais = upc.country_bar_plot(df, cols, x, y, operacao, ascending = False, title = title, xaxis_title = xaxis_title, yaxis_title = yaxis_title, legend_title_text = legend_title_text)

#####============================================================================================================================================#####
#####============================================================================================================================================#####

# Quantidade de cidades registradas por país
cols_cities = ['city', 'country_name']
df = df_filtrado.copy()
y_cities = 'city'
operacao_cities = pd.Series.nunique
title_cities = 'Quantidade de Cidades por País'
xaxis_title_cities = 'País'
yaxis_title_cities = 'Quantidade de Cidades'
legend_title_text_cities = 'Países'

# Gráfico de quantidade de cidades registradas por país
fig_cidades_por_pais = upc.country_bar_plot(df, cols_cities, x, y_cities, operacao_cities, ascending = False, title = title_cities, xaxis_title = xaxis_title_cities, yaxis_title = yaxis_title_cities, legend_title_text = legend_title_text_cities)

#####============================================================================================================================================#####
#####============================================================================================================================================#####

# Quantidade de avaliações por país
cols_votes = ['votes', 'country_name']
df = df_filtrado.copy()
y_votes = 'votes'
operacao_votes = pd.Series.mean
title_votes = 'Quantidade Média de Avaliações por País'
xaxis_title_votes = 'País'
yaxis_title_votes = 'Quantidade de Avaliações'
legend_title_text_votes = 'Países'

# Gráfico de quantidade de avaliações por país
fig_avaliacoes_por_pais = upc.country_bar_plot(df, cols_votes, x, y_votes, operacao_votes, ascending = False, title = title_votes, xaxis_title = xaxis_title_votes, yaxis_title = yaxis_title_votes, legend_title_text = legend_title_text_votes)

#####============================================================================================================================================#####
#####============================================================================================================================================#####

# Média de preço para duas pessoas por país
cols = ['average_cost_for_two_brl', 'country_name']
df = df_filtrado.copy()
x = 'country_name'
y = 'average_cost_for_two_brl'
operacao = pd.Series.mean
title = 'Valor Médio em R$ do Preço para Duas Pessoas por País'
xaxis_title = 'País'
yaxis_title = 'Valor Médio do Preço em R$'
legend_title_text = 'Países'

# Gráfico
custo4two_por_pais = upc.country_bar_plot(df, cols, x, y, operacao, ascending = False, title = title, xaxis_title = xaxis_title, yaxis_title = yaxis_title, legend_title_text = legend_title_text)

#####============================================================================================================================================#####
#####============================================================================================================================================#####

# Restaurantes por culinária por país
df = df_filtrado.copy()
rest_culi_pais = upc.tree_country_cuisines_rest(df)

#####============================================================================================================================================#####
#####============================================================================================================================================#####


#####============================================================================================================================================#####
# VISÃO PAÍSES
#####============================================================================================================================================#####

# Restaurantes por culinária por país
rest_culi_pais = upc.tree_country_cuisines_rest(df)

st.markdown("# :earth_americas: Visão Países")
st.markdown('---')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_restaurantes_por_pais, use_container_width = True)
    with col2:
        st.plotly_chart(fig_cidades_por_pais, use_container_width = True)

with st.container():
    col3, col4= st.columns(2)
    with col3:
        st.plotly_chart(fig_avaliacoes_por_pais, use_container_width = True)
    with col4:
        st.plotly_chart(custo4two_por_pais, use_container_width = True)

with st.container():
    st.plotly_chart(rest_culi_pais, use_container_width = True)
