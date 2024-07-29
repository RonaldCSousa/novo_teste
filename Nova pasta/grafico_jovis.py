import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Criando o DataFrame com informações de coordenações e superintendências
data = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
    'Coordenação': ['Coord1', 'Coord1', 'Coord1', 'Coord1', 'Coord1',
                    'Coord2', 'Coord2', 'Coord2', 'Coord2', 'Coord2'],
    'Orçado_supt': [5000, 6000, 5500, 5250, 6500, 3000, 4000, 3500, 3250, 4000],
    'Orçado_rt': [5000, 6000, 5500, 5250, 6500, 3000, 4000, 3500, 3250, 4000],
    'FYF operações': [9500, 11500, 10500, 10000, 12500, 7500, 9500, 8500, 8000, 9500],
    'FYF RT': [10500, 11800, 11200, 10800, 13200, 8500, 9800, 9200, 8800, 10000]
}

df = pd.DataFrame(data)

# Configurando a página Streamlit
st.title('Orçado vs. FYF operações vs. FYF RT (com coordenações)')

# Adicionando o multiselect para coordenações
coord_options = df['Coordenação'].unique()
selected_coords = st.multiselect('Selecione as coordenações', coord_options, default=coord_options)

# Filtrando o DataFrame com base na seleção
filtered_df = df[df['Coordenação'].isin(selected_coords)]

# Agrupando os dados por mês e somando os valores para coordenações selecionadas
grouped_df = filtered_df.groupby('Mês').sum().reset_index()

# Calculando o delta
grouped_df['Delta'] = (grouped_df['Orçado_supt'] + grouped_df['Orçado_rt']) - (grouped_df['FYF operações'] + grouped_df['FYF RT'])

# Criando o gráfico de barras com Plotly
fig = go.Figure()

# Barras empilhadas para "Orçado"
fig.add_trace(go.Bar(
    x=grouped_df['Mês'],
    y=grouped_df['Orçado_supt'],
    name='Orçado - supt',
    marker_color='blue',
    text=grouped_df['Orçado_supt'],
    textposition='inside',
    offsetgroup=0
))

fig.add_trace(go.Bar(
    x=grouped_df['Mês'],
    y=grouped_df['Orçado_rt'],
    name='Orçado - rt',
    marker_color='lightblue',
    text=grouped_df['Orçado_rt'],
    textposition='inside',
    offsetgroup=0,
    base=grouped_df['Orçado_supt']
))

# Barras empilhadas para "FYF operações" e "FYF RT"
fig.add_trace(go.Bar(
    x=grouped_df['Mês'],
    y=grouped_df['FYF operações'],
    name='FYF operações',
    marker_color='orange',
    text=grouped_df['FYF operações'],
    textposition='inside',
    offsetgroup=1
))

fig.add_trace(go.Bar(
    x=grouped_df['Mês'],
    y=grouped_df['FYF RT'],
    name='FYF RT',
    marker_color='green',
    text=grouped_df['FYF RT'],
    textposition='inside',
    offsetgroup=1,
    base=grouped_df['FYF operações']
))

# Adicionando gráfico de linha para o Delta
fig.add_trace(go.Scatter(
    x=grouped_df['Mês'],
    y=grouped_df['Delta'],
    mode='lines+markers',
    name='Delta',
    line=dict(color='red'),
    yaxis='y2'
))

# Configurando layout do gráfico e legendas
fig.update_layout(
    title='Orçado vs. FYF operações vs. FYF RT (com coordenações)',
    xaxis_title='Mês',
    yaxis_title='Valor',
    legend=dict(x=1.05, y=1, xanchor='left', yanchor='top'),
    yaxis2=dict(overlaying='y', side='right', title='Delta'),
    barmode='group'
)

# Exibindo o gráfico no Streamlit
st.plotly_chart(fig)
