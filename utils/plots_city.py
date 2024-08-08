import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

def cities_bar_plot(df, cols, x, y, z, operacao, ascending = [True, False], title='Título', xaxis_title='Eixo X', yaxis_title='Eixo Y', 
                    legend_title_text = 'Legenda'):
    # Seleciona as colunas especificadas
    df_aux = df.loc[:, cols]
    
    # Aplica a operação especificada
    df_aux = df_aux.groupby([z, x])[y].apply(operacao).reset_index()
    
    # Ordena o DataFrame com base no z e y
    df_aux = df_aux.sort_values(by = [z, y], ascending = ascending)

    # Seleciona os 10 primeiros números
    df_aux = df_aux.groupby(z).head(10).reset_index()
    
    # Gráfico
    fig = px.bar(df_aux, 
                 x = x, 
                 y = y,
                 color = z, 
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
    
    # Plota o Gráfico
    return go.Figure(fig)

#-----------------------------------------------------------------------------------------------#

def cities_rank_bar_plot(df, lines, cols, x, y, z, r, operacao, ascending = [True, False], title='Título', xaxis_title='Eixo X', yaxis_title='Eixo Y', 
                         legend_title_text = 'Legenda'):
   
    # Seleciona as colunas especificadas e aplica o filtro
    df_aux = df.loc[lines, cols]
    
    # Aplica a operação especificada
    df_aux = df_aux.groupby([z, x]).agg({r: operacao[0], y: operacao[1]})
    df_aux.columns = [r, y]
    df_aux.reset_index(inplace = True)
    
    # Ordena o DataFrame com base no z e y
    df_aux = df_aux.sort_values(by = [z, y], ascending = ascending)

    # Seleciona os 10 primeiros números
    df_aux = df_aux.groupby(z).head(10).reset_index(drop=True)
    
    # Gráfico
    fig = px.bar(df_aux, 
                 x = x, 
                 y = y,
                 color = z, 
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

    # Plota o Gráfico
    return go.Figure(fig)