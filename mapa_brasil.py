import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium,folium_static
import requests

# Função para carregar o GeoJSON uma única vez e armazenar no session_state
def load_geojson():
    geojson_url = 'https://raw.githubusercontent.com/giuliano-macedo/geodata-br-states/refs/heads/main/geojson/br_states.json'
    if 'geojson_data' not in st.session_state:
        response = requests.get(geojson_url)
        st.session_state.geojson_data = response.json()  # Armazena o GeoJSON no session_state
    return st.session_state.geojson_data

# Carregar os dados dos estados e suas respectivas notas
data = {
    'estado': ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'],
    'nota': [9, 8, 6, 7, 5, 10, 4, 5, 3, 6, 8, 9, 5, 7, 4, 6, 10, 2, 3, 8, 9, 5, 4, 10, 6, 7, 9]
}
df = pd.DataFrame(data)

# Função para determinar a cor com base na nota
def get_color(nota):
    if nota >= 9:
        return 'green'   # Verde para notas de 9 a 10
    elif nota >= 5:
        return 'yellow'  # Amarelo para notas de 5 a 8
    else:
        return 'red'     # Vermelho para notas de 0 a 4

# Criar um mapa do Brasil
mapa_brasil = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)
folium.TileLayer("cartodbpositron").add_to(mapa_brasil)

# Carregar o arquivo GeoJSON dos estados do Brasil e armazenar no session_state
geojson_data = load_geojson()

# Adicionar os estados ao mapa
folium.GeoJson(
    geojson_data,
    name='geojson',
    style_function=lambda feature: {
        'fillColor': get_color(df.loc[df['estado'] == feature['properties']['SIGLA'], 'nota'].values[0]),
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.7,
    }
).add_to(mapa_brasil)

# Adicionar controle de camadas
folium.LayerControl().add_to(mapa_brasil)

# Exibir o mapa no Streamlit
st.title('Mapa do Brasil com Notas por Estado')
st_data = st_folium(mapa_brasil, width=800, height=600) 