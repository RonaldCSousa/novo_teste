import folium
import pandas as pd
import random
import streamlit as st
from streamlit_folium import st_folium
import requests


import json

# Caminho para o seu arquivo JSON
caminho_do_arquivo = 'br_states.json'

# Abrindo e lendo o arquivo JSON
with open(caminho_do_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)

# Função para carregar o GeoJSON
def load_geojson():
    geojson_url = 'https://raw.githubusercontent.com/giuliano-macedo/geodata-br-states/refs/heads/main/geojson/br_states.json'
    if 'geojson_data' not in st.session_state:
        response = requests.get(geojson_url)
        st.session_state.geojson_data = response.json()  # Armazena no session_state
    return st.session_state.geojson_data

# Função para gerar dados fictícios de agências por estado
def gerar_classificacoes():
    estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 
               'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 
               'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    classificacoes_por_estado = []
    
    for estado in estados:
        num_agencias = random.randint(10, 20)  # Entre 10 a 20 agências por estado
        classificacoes = random.choices(['aderente', 'mediana', 'crítica'], k=num_agencias)
        classificacoes_por_estado.append({'estado': estado, 'classificacoes': classificacoes})
    
    return pd.DataFrame(classificacoes_por_estado)

# Gerar dados fictícios de agências apenas uma vez
if 'df_agencias' not in st.session_state:
    st.session_state.df_agencias = gerar_classificacoes()

# Carregar dados do session_state
df = st.session_state.df_agencias

# Função para determinar a classificação dominante em cada estado
def get_dominant_classificacao(classificacoes):
    contagem = pd.Series(classificacoes).value_counts()  # Conta quantas vezes cada classificação aparece
    return contagem.idxmax()  # Retorna a classificação com maior número de agências

# Função para definir a cor com base na classificação dominante
def get_color(classificacao_dominante):
    if classificacao_dominante == 'aderente':
        return 'green'   # Verde para aderente
    elif classificacao_dominante == 'mediana':
        return 'yellow'  # Amarelo para mediana
    else:
        return 'red'     # Vermelho para crítica

# Definir a classificação dominante para cada estado
df['classificacao_dominante'] = df['classificacoes'].apply(get_dominant_classificacao)

# Criar o mapa do Brasil
mapa_brasil = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)
folium.TileLayer("cartodbpositron").add_to(mapa_brasil)

# Carregar o GeoJSON e adicionar ao mapa
geojson_data = load_geojson()

# Adicionar os estados ao mapa com base na classificação dominante
folium.GeoJson(
    geojson_data,
    name='geojson',
    style_function=lambda feature: {
        'fillColor': get_color(df.loc[df['estado'] == feature['properties']['SIGLA'], 'classificacao_dominante'].values[0]),
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.7,
    },
    tooltip=folium.GeoJsonTooltip(
        fields=['SIGLA'],  # Exibe a sigla do estado
        aliases=['Estado: '],
        # sticky=True,
        # labels=True,
        # localize=True,
        # style="""
        #     background-color: white;
        #     border: 1px solid black;
        #     border-radius: 5px;
        #     font-size: 12px;
        #     """,
    ),
    # highlight_function=lambda x: {
    #     'fillColor': get_color(df.loc[df['estado'] == x['properties']['SIGLA'], 'classificacao_dominante'].values[0]),
    #     'color': 'black',
    #     'weight': 1,
    #     'fillOpacity': 0.7,
    # }
).add_to(mapa_brasil)

# Adicionar controle de camadas
folium.LayerControl().add_to(mapa_brasil)

# Exibir o mapa no Streamlit
st.title('Mapa do Brasil com Classificação de Agências por Estado (Maior Volume)')
st_data = st_folium(mapa_brasil, width=800, height=600)