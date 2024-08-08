import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

def country_bar_plot(df, cols, x, y, operacao, ascending = False, title = 'Título', xaxis_title = 'Eixo X', yaxis_title = 'Eixo Y', legend_title_text = 'Legenda'):
    # Seleciona as colunas especificadas
    df_aux = df.loc[:, cols]
    
    # Aplica a operação especificada
    df_aux = df_aux.groupby(x).agg(operacao).reset_index()

    # Ordena o DataFrame
    df_aux = df_aux.sort_values(by = y, ascending = ascending).reset_index(drop=True)

    # Gráfico
    fig = px.bar(df_aux, 
                 x = x, 
                 y = y,
                 color = x, 
                 title = title,
                 text = y) # adiciona o valor nas barras
    
    # Renomeia eixos e legenda
    fig.update_layout(xaxis_title = xaxis_title,  # renomeia o eixo x
                      yaxis_title = yaxis_title,  # renomeia o eixo y
                      legend_title_text = legend_title_text,  # título da legenda
                      template = 'plotly_dark',  # altera o tema
                      font = dict(size=12),  # altera o tamanho da fonte
                      title_x = 0,  # centraliza o título
                      height = 600,  # define a altura do gráfico
                      width = 1024)   # define a largura do gráfico
    
    # Atualiza as anotações para exibir os valores nas barras
    fig.update_traces(
        texttemplate='%{text:.0f}', 
        textposition='outside',  # exibir o valor fora da barra
        textfont_size=10  # tamanho da fonte dos valores
    )
    
    # Retorna a figura Plotly
    return go.Figure(fig)

#-----------------------------------------------------------------------------------------------#

# Plot tree
def tree_country_cuisines_rest(df): 
    # Agrupar os dados
    agg_df = df.groupby(['country_name', 'cuisines', 'restaurant_name']).size().reset_index(name='count')
    
    # Criar o treemap
    fig = px.treemap(agg_df, 
                     path=['country_name', 'cuisines', 'restaurant_name'], 
                     values='count',
                     title='Restaurantes por Tipo de Culinárias em cada País',
                     color='country_name')
    
    # Atualizar layout do gráfico
    fig.update_layout(
        title_x=0,  # Centralizar o título
        font=dict(size=14),  # Tamanho da fonte
        template='plotly_dark'  # Tema escuro
    )
    
    # Mostrar o gráfico
    return go.Figure(fig)