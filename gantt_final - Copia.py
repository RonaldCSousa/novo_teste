import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="TESTE",
    page_icon="🧊",
    layout="wide",
)

with st.sidebar:
    st.write("Testes Ronald")

def color_coding(value, min_val, max_val, col_name, color_columns):
    """ Função para aplicar cores apenas em colunas específicas. """
    if col_name not in color_columns:
        return ''
    relative_val = (value - min_val) / (max_val - min_val) if max_val > min_val else 0
    red = 255
    green = int(210 - (150 * relative_val))
    blue = int(180 - (180 * relative_val))
    color_bg = f'rgb({red}, {green}, {blue})'
    color_font = 'black' if relative_val < 0.7 else 'white'
    return f'background-color: {color_bg}; color: {color_font}; font-weight: bold'

data = {
    'Tipo de Manutenção': ['Ar Condicionado'] * 3 + ['Elétrica'] * 3 + ['Civil'] * 3 + ['Hidráulica'] * 3 + ['Mecânica'] * 3,
    'inicio': pd.to_datetime(['2024-01-01', '2024-04-15', '2024-07-20', '2024-01-15', '2024-05-16', '2024-09-10', '2024-02-01', '2024-05-19', '2024-08-25', '2024-02-15', '2024-06-10', '2024-10-05', '2024-03-05', '2024-07-15', '2024-11-01']),
    'fim': pd.to_datetime(['2024-02-05', '2024-05-15', '2024-08-20', '2024-03-20', '2024-06-20', '2024-11-10', '2024-03-03', '2024-06-19', '2024-09-25', '2024-04-10', '2024-07-10', '2024-11-20', '2024-04-05', '2024-08-15', '2024-12-01'])
}

df = pd.DataFrame(data)

fig = px.timeline(df, x_start="inicio", x_end="fim", y="Tipo de Manutenção", color="Tipo de Manutenção", labels={"Tipo de Manutenção": "Tipo de Manutenção"})

# Datas da reforma
data_reforma1 = pd.to_datetime('2024-04-01')
data_reforma2 = pd.to_datetime('2024-05-16')

# Adicionar linha e anotação para as datas da reforma
fig.add_vline(x=data_reforma1, line_width=2, line_dash="dash", line_color="red")
fig.add_vline(x=data_reforma2, line_width=2, line_dash="dash", line_color="red")

fig.add_annotation(
    x=data_reforma1, 
    y=0.95, 
    text="INICIO DA OBRA",
    showarrow=True,
    arrowcolor="gold",
    arrowhead=1,
    font=dict(
        family="Arial, sans-serif",
        size=15,
        color="gold"
    ),
    xref="x",
    yref="paper"
)

fig.add_annotation(
    x=data_reforma2, 
    y=0.95, 
    text="FIM DA OBRA",
    showarrow=True,
    arrowhead=1,
    arrowcolor="gold",
    font=dict(
        family="Arial, sans-serif",
        size=15,
        color="gold"
    ),
    xref="x",
    yref="paper"
)

# Adicionar retângulo de fundo para o intervalo da reforma
fig.add_vrect(x0=data_reforma1, x1=data_reforma2, fillcolor="lightgrey", opacity=0.5, line_width=0)

# Ordenar por 'Tipo de Manutenção' e 'inicio'
df.sort_values(by=['Tipo de Manutenção', 'inicio'], inplace=True)

# Calcular o próximo início de manutenção para cada tipo
df['Próximo Início'] = df.groupby('Tipo de Manutenção')['inicio'].shift(-1)

# Função de cálculo de dias até a próxima manutenção considerando o fim da reforma
def calcular_dias(row):
    if pd.isna(row['Próximo Início']):
        if row['inicio'] > data_reforma2:  # Manutenção após o fim da reforma
            return (row['inicio'] - data_reforma2).days
    return (row['Próximo Início'] - row['fim']).days

df['Dias até próxima manutenção'] = df.apply(calcular_dias, axis=1).fillna(0)

def periodo_reforma(row):
    if row['inicio'] < data_reforma1:
        return 'Antes da Reforma'
    elif row['inicio'] > data_reforma2:
        return 'Depois da Reforma'
    else:
        return 'Durante a Reforma'

df['Período'] = df.apply(periodo_reforma, axis=1)

# Filtrar fora 'Durante a Reforma' para a exibição nas tabelas
df_filtered = df[df['Período'] != 'Durante a Reforma']

media_dias_periodo = df_filtered.groupby(['Tipo de Manutenção', 'Período'])['Dias até próxima manutenção'].mean().unstack(fill_value=0)

contagem_manutencoes = df_filtered.pivot_table(index='Tipo de Manutenção', columns='Período', aggfunc='size', fill_value=0)

df_merge = pd.merge(contagem_manutencoes, media_dias_periodo, on="Tipo de Manutenção", how="inner")

# Mostrar o gráfico no Streamlit primeiro
st.plotly_chart(fig, use_container_width=True)

# Colunas para exibir as tabelas abaixo do gráfico
col_media_dias, col_divisor, col_manut_antes_depois = st.columns([2, 0.01, 2])

with col_media_dias:
    st.write("Média de dias até a próxima manutenção por tipo e período:")
    st.dataframe(media_dias_periodo, use_container_width=True)

with col_manut_antes_depois:
    min_val = df_merge.min().min()
    max_val = df_merge.max().max()
    color_columns = ['Antes da Reforma', 'Depois da Reforma']
    styled_pivot_df = df_merge.style.apply(lambda x: x.apply(lambda val: color_coding(val, min_val, max_val, x.name, color_columns)))

    st.write("Quantidade de manutenções por tipo e período:")
    st.dataframe(styled_pivot_df, use_container_width=True)