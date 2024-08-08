import pandas as pd
import folium
from folium.plugins import MarkerCluster

def mapa(df, cols):
    
    # Localização de cada restaurante
    df_mapa = df.loc[:, cols]
    
    # Cria o mapa vazio
    mapa = folium.Map(location=[df_mapa['latitude'].mean(), df_mapa['longitude'].mean()], zoom_start=1.5)
    
    # Adiciona o MarkerCluster ao mapa
    marker_cluster = MarkerCluster().add_to(mapa)
    
    # Itera sobre as linhas do DataFrame para adicionar marcadores
    for index, location in df_mapa.iterrows():
        # Criando o conteúdo do popup
        popup_content = f"""
        <h4>{location['restaurant_name']}</h4> <br> 
        <b>Tipo de Cozinha:</b> {location['cuisines']} <br>
        <b>Custo Médio para Duas Pessoas:</b> {location['currency']} {location['average_cost_for_two']} <br>
        <b>Avaliação:</b> {location['aggregate_rating']}
        """
        
        folium.Marker([location['latitude'], location['longitude']],
                      popup=folium.Popup(popup_content, max_width=500),
                      icon=folium.Icon(color=location['color_name'], icon='cutlery', prefix='fa')).add_to(marker_cluster)
        
    # Retorna o HTML do mapa
    return mapa._repr_html_()
