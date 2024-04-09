# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots

# # Seu dataframe
# data = {
#     'Gerencia': ['GPGO', 'GPGO', 'GPGO', 'GPA', 'GPA', 'GPA'],
#     'Nivel Cargo': ['JUNIOR', 'PLENO', 'SENIOR', 'JUNIOR', 'PLENO', 'SENIOR'],
#     'Quantidade': [2, 3, 5, 1, 7, 2]
# }

# # Convertendo o dicionário para DataFrame
# df = pd.DataFrame(data)

# # Agrupando por 'Gerencia' e 'Nivel Cargo' e somando a 'Quantidade'
# grouped = df.groupby(['Gerencia', 'Nivel Cargo'])['Quantidade'].sum().unstack(fill_value=0)

# # Definir as cores para cada nível de cargo
# colors = {'JUNIOR': 'lightblue', 'SENIOR': 'lightgreen', 'PLENO': 'lightcoral'}

# # Streamlit
# st.title('Contagem de Analistas por Gerência e Nível de Cargo')

# # Criar a figura com subplots
# fig = make_subplots(rows=1, cols=len(grouped.index), shared_yaxes=True)

# # Adicionar as barras para cada gerência
# for i, gerencia in enumerate(grouped.index, start=1):
#     for nivel_cargo in ['JUNIOR', 'PLENO', 'SENIOR']:
#         quantidade = grouped.loc[gerencia, nivel_cargo]
#         fig.add_trace(
#             go.Bar(
#                 y=[nivel_cargo],
#                 x=[quantidade],
#                 name=nivel_cargo,
#                 marker_color=colors.get(nivel_cargo, 'gray'),
#                 showlegend=i == 1,
#                 orientation='h'
#             ),
#             row=1, col=i
#         )
#         # Adicionar anotação de texto dentro da barra
#         fig.add_annotation(
#             text=str(quantidade),
#             x=quantidade / 1.5,  # Posição central da barra
#             y=nivel_cargo,
#             xref=f'x{i}',
#             yref='y',
#             showarrow=False,
#             font=dict(color='black', size=12)
#         )

# # Atualizar layout do subplot
# fig.update_layout(height=300, width=600)
# fig.update_xaxes(visible=False)

# # Exibir gráfico
# st.plotly_chart(fig)


import streamlit as st
import pandas as pd
import plotly.express as px

# Seu dataframe
data = {
    'Gerencia': ['GPGO', 'GPGO', 'GPGO', 'GPA', 'GPA', 'GPA'],
    'Nivel Cargo': ['JUNIOR', 'PLENO', 'SENIOR', 'JUNIOR', 'PLENO', 'SENIOR'],
    'Quantidade': [2, 3, 5, 1, 7, 2]
}

# Convertendo o dicionário para DataFrame
df = pd.DataFrame(data)

# Definir as cores para cada nível de cargo
colors = {'JUNIOR': 'lightblue', 'SENIOR': 'lightgreen', 'PLENO': 'lightcoral'}

# Streamlit
st.title('Contagem de Analistas por Gerência e Nível de Cargo')

# Criar o gráfico de barras com plotly.express
fig = px.bar(
    df,
    x='Quantidade',
    y='Nivel Cargo',
    color='Nivel Cargo',
    color_discrete_map=colors,
    facet_col='Gerencia',
    orientation='h',
    text='Quantidade'  # Adiciona o valor da quantidade dentro das barras
)

# Atualizar layout do gráfico
fig.update_layout(height=300, width=600)
fig.update_xaxes(visible=False)

# Exibir gráfico
st.plotly_chart(fig)
