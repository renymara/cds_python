import pandas as pd
import numpy as np
import sys
import os
import streamlit as st
from PIL import Image

#####============================================================================================================================================#####
#####============================================================================================================================================#####

data_path = f"data/zomato_processed.csv"
df_oficial = pd.read_csv(data_path)
df = df_oficial.copy()

#####============================================================================================================================================#####
#####============================================================================================================================================#####


#####============================================================================================================================================#####
# CONFIGURAÇÃO PÁGINA
#####============================================================================================================================================#####

st.set_page_config(
    page_title='Home',
    page_icon='🏠',
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

#####============================================================================================================================================#####
#####============================================================================================================================================#####

#####============================================================================================================================================#####
# LAYOUT HOME
#####============================================================================================================================================#####

st.header("ZOMATO RESTAURANTS!")
st.markdown('---')
st.subheader('Um Projeto de Análise de Dados')

st.markdown('Aqui você vai encontrar uma análise detalhada sobre os dados da companhia Zomato Restaurants, que tem vários restaurantes pelo mundo, e junto com eles, muita informação.')

st.markdown(
    """
    ### Informações sobre o Dashboard
    - Visão Geral: Perspectiva geral das informações sobre os dados da companhia Zomato Restaurants
    - Visão Países: Perpectiva dos dados da companhia Zomato Restaurants tendo como foco os países
    - Visão Cidade: Perpectiva dos dados da companhia Zomato Restaurants tendo como foco as cidades
    - Visão Culinárias: Perpectiva dos dados da companhia Zomato Restaurants tendo como foco as culinárias
    
    ### Alguma dúvida? Fale comigo!
    - LinkedIn: https://www.linkedin.com/in/renymara-hanna/
    - Github: https://github.com/renymara
"""
)














