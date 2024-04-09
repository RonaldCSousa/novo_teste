import pandas as pd
import streamlit as st
import plotly.graph_objs as go
import calendar

# Definindo os dados corrigidos
data = {
    'NUMFUNC': [1, 2, 3, 4, 5, 6],
    'NOMFUNC': ['Ronald', 'Emerson', 'Ken', 'Nil', 'Kanno', 'Barbosa'],
    'NIVEL CARGO': ['JUNIOR', 'SENIOR', 'PLENO', 'JUNIOR', 'PLENO', 'PLENO'],
    'MOVIMENTACAO': ['ENTRADA', 'ENTRADA', 'PROMOCAO', 'SAIDA', 'SAIDA', 'SAIDA'],
    'GERENCIA': ['GPGO', 'GPGO', 'GPGO', 'GPA', 'GPA', 'GPA'],
    'DATABASE': ['2024-01-01', '2024-01-03', '2024-02-02', '2024-01-15', '2024-02-15', '2024-02-16']
}

# Criando um DataFrame a partir dos dados
df = pd.DataFrame(data)

# Convertendo a coluna 'DATABASE' para o tipo datetime
df['DATABASE'] = pd.to_datetime(df['DATABASE'])

# Extraindo o mês da coluna 'DATABASE'
df['MES'] = df['DATABASE'].dt.month

# Mapeando o número do mês para o nome abreviado do mês em português
meses = [
    'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
    'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'
]
df['MES'] = df['MES'].apply(lambda x: meses[x - 1])

# Contando as entradas e saídas em cada mês
# Contando as entradas e saídas em cada mês usando 'count'
count_entries = df[df['MOVIMENTACAO'] == 'ENTRADA'].groupby('MES')['MOVIMENTACAO'].count()
count_exits = df[df['MOVIMENTACAO'] == 'SAIDA'].groupby('MES')['MOVIMENTACAO'].count()


# Configurando o aplicativo Streamlit
st.title('Contagem de Entradas e Saídas por Mês')

# Criando o gráfico de barras com Plotly
trace1 = go.Bar(
    x=count_entries.index,
    y=count_entries.values,
    text=count_entries.values,
    textposition='outside',
    name='Entrada',
    offsetgroup=1
)

trace2 = go.Bar(
    x=count_exits.index,
    y=count_exits.values,
    text=count_exits.values,
    textposition='outside',
    name='Saída',
    offsetgroup=2
)

data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(title='Mês'),
    yaxis=dict(title='Contagem',showticklabels=False),
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)

# Exibindo o gráfico no Streamlit


st.plotly_chart(fig)
