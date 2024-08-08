import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

def filter_best(df, cols, group):

    df_aux = df.sort_values(by='aggregate_rating', ascending=False).groupby(group).first().reset_index()

    # Exibir informações desejadas: nome do restaurante, país, tipo de culinária e a nota
    cols_to_show = cols
    df = df_aux[cols_to_show]
    
    return df

#-----------------------------------------------------------------------------------------------#

def cuisines_bar_plot(df, cols, x, y, operacao, ascending = False, title='Título', xaxis_title='Eixo X', yaxis_title='Eixo Y', legend_title_text = 'Legenda'):
    # Seleciona as colunas especificadas
    df_aux = df.loc[:, cols]
    
    # Aplica a operação especificada
    df_aux = df_aux.groupby(x)[y].agg(operacao).reset_index()

    # Ordena o DataFrame com base no y
    df_aux = df_aux.sort_values(by = y, ascending = ascending).reset_index(drop=True)

    # Seleciona os 10 primeiros números
    df_aux = df_aux.head(10)
    
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
        texttemplate='%{text:.1f}', 
        textposition='outside',  # exibir o valor fora da barra
        textfont_size=10  # tamanho da fonte dos valores
    )
    
    # Plota o Gráfico
    return go.Figure(fig)