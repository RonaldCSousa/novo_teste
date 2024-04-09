import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from datetime import datetime
import pandas as pd
from datetime import datetime,timedelta
from plotly.subplots import make_subplots

# Criando um dataframe com os dados fornecidos
data = {
    'NUMFUNC': [1, 2, 3, 4, 5, 6],
    'NOMFUNC': ['Ronald', 'Emerson', 'Ken', 'Nil', 'Kanno', 'Barbosa'],
    'NIVEL CARGO': ['JUNIOR', 'SENIOR', 'PLENO', 'JUNIOR', 'PLENO', 'PLENO'],
    'MOVIMENTACAO': ['ENTRADA', 'ENTRADA', 'PROMOCAO', 'SAIDA', 'SAIDA', 'SAIDA'],
    'GERENCIA': ['GPGO', 'GPGO', 'GPGO', 'GPA', 'GPA', 'GPA']
}

df = pd.DataFrame(data)

# Agrupando os dados pela coluna 'MOVIMENTACAO'
movimentacao_counts = df['MOVIMENTACAO'].value_counts()

# Criando o gráfico de barras horizontal com Plotly
fig = px.bar(y=movimentacao_counts.index, x=movimentacao_counts.values, 
             text=movimentacao_counts.values,
             labels={'y':'Tipo de Movimentação', 'x':'Volumetria'},
             title='Volumetria de Movimentação',
             orientation='h')

fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.update_xaxes(visible=False)


# Exibindo o gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)