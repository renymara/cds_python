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
from utils import plots_cuisine as upn

data_path = f"data/zomato_processed.csv"
df_oficial = pd.read_csv(data_path)
df = df_oficial.copy()

#####============================================================================================================================================#####
#####============================================================================================================================================#####


#####============================================================================================================================================#####
# CONFIGURAÇÃO PÁGINA
#####============================================================================================================================================#####

st.set_page_config(
    page_title='Visão Culinárias',
    page_icon='🍴',
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

# Melhores restaurantes por país
df = df_oficial.copy()
cols = ['country_name', 'restaurant_name', 'cuisines', 'aggregate_rating']
group = 'country_name'

best_rest_for_country = upn.filter_best(df, cols, group)

#####============================================================================================================================================#####
#####============================================================================================================================================#####

# Melhor restaurante por culinária
df = df_oficial.copy()
cols = ['cuisines', 'restaurant_name', 'country_name', 'aggregate_rating']
group = 'cuisines'

best_rest_for_cuisine = upn.filter_best(df, cols, group)

#####============================================================================================================================================#####
#####============================================================================================================================================#####

# 10 Culinárias com as Melhores Avaliações
cols = ['cuisines', 'aggregate_rating']
df = df_filtrado.copy()
x = 'cuisines'
y = 'aggregate_rating'
operacao = 'mean'  # Alteração aqui para usar a string 'mean'
title = '10 Culinárias com as Melhores Avaliações'
xaxis_title = 'Culinárias'
yaxis_title = 'Notas'
legend_title_text = 'Culinárias'

cuisines_best10 = upn.cuisines_bar_plot(df, cols, x, y, operacao, ascending = False, title = title, xaxis_title = xaxis_title, yaxis_title = yaxis_title, legend_title_text = legend_title_text)

#####============================================================================================================================================#####
#####============================================================================================================================================#####

# 10 Culinárias com as Piores Avaliações
cols = ['cuisines', 'aggregate_rating']
df = df_filtrado.copy()
x = 'cuisines'
y = 'aggregate_rating'
operacao = 'mean'  # Alteração aqui para usar a string 'mean'
title = '10 Culinárias com as Piores  Avaliações'
xaxis_title = 'Culinárias'
yaxis_title = 'Notas'
legend_title_text = 'Culinárias'

cuisines_worst = upn.cuisines_bar_plot(df, cols, x, y, operacao, ascending = True, title = title, xaxis_title = xaxis_title, yaxis_title = yaxis_title, legend_title_text = legend_title_text)

#####============================================================================================================================================#####
#####============================================================================================================================================#####


#####============================================================================================================================================#####
# VISÃO CULINÁRIAS
#####============================================================================================================================================#####

st.markdown("# 🍽️ Visão Culinárias")
st.markdown('---')

st.subheader('Melhores Restaurantes por País')
with st.container():
     st.dataframe(best_rest_for_country, use_container_width = True)

st.subheader('Melhor Restaurante por Culinária')
with st.container():
     st.dataframe(best_rest_for_cuisine, use_container_width = True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(cuisines_best10, use_container_width = True)
    with col2:
        st.plotly_chart(cuisines_worst, use_container_width = True)





















