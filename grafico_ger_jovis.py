import pandas as pd
import plotly.express as px
import streamlit as st

# Dados fictícios para o DataFrame
data = {
    'data': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-01', '2024-01-02', '2024-01-03'],
    'diretoria': ['Financeira', 'Financeira', 'RH', 'TI', 'TI', 'RH'],
    'gerencia': ['Contabilidade', 'Tesouraria', 'Recrutamento', 'Infraestrutura', 'Desenvolvimento', 'Treinamento'],
    'coordenação': ['Financeiro', 'Operações', 'RH1', 'TI1', 'TI2', 'RH2'],
    'nome do analista': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda'],
    'codigo do analista': [101, 102, 103, 104, 105, 106],
    'cargo': ['junior', 'senior', 'pleno', 'junior', 'senior', 'pleno']
}

# Criar o DataFrame
df = pd.DataFrame(data)

# Converter a coluna "data" para o tipo datetime
df['data'] = pd.to_datetime(df['data'])

# Título da aplicação
st.title('Análise de Analistas por Diretoria e Gerência')

# Criar o selectbox com as opções de diretorias únicas
diretorias = df['diretoria'].unique()
diretoria_selecionada = st.selectbox('Selecione a Diretoria', diretorias)

# Filtrar os dados pela diretoria selecionada
df_filtrado = df[df['diretoria'] == diretoria_selecionada]

# Agrupar e contar os analistas por mês e cargo, convertendo Period para string
df_filtrado['mes'] = df_filtrado['data'].dt.to_period('M').astype(str)
contagem = df_filtrado.groupby(['mes', 'cargo']).size().reset_index(name='count')

# Criar o gráfico com Plotly
fig = px.bar(contagem, x='mes', y='count', color='cargo', barmode='group',
             title=f'Quantidade de Analistas por Cargo na Diretoria {diretoria_selecionada} por Mês')

# Mostrar o gráfico no Streamlit
st.plotly_chart(fig)
