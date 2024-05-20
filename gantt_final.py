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

def color_coding(value, min_val, max_val):
    """ Função para aplicar um novo tom de laranja, começando suavemente e intensificando-se. """
    # Normalizar o valor
    relative_val = (value - min_val) / (max_val - min_val) if max_val > min_val else 0
    # Interpolar de laranja muito suave para laranja mais saturado
    red = 255
    green = int(210 - (150 * relative_val))  # Começar com verde suave (210) até 60 (laranja saturado)
    blue = int(180 - (180 * relative_val))   # Começar com azul suave (180) até 0 (laranja saturado)
    color_bg = f'rgb({red}, {green}, {blue})'
    color_font = 'black' if relative_val < 0.7 else 'white'  # Mudança da cor da fonte para contraste
    return f'background-color: {color_bg}; color: {color_font}; font-weight: bold'


# Dados de exemplo com intervalos variados para cada manutenção
data = {
    'Tipo de Manutenção': [
        'Ar Condicionado', 'Ar Condicionado', 'Ar Condicionado',
        'Elétrica', 'Elétrica', 'Elétrica',
        'Civil', 'Civil', 'Civil',
        'Hidráulica', 'Hidráulica', 'Hidráulica',
        'Mecânica', 'Mecânica', 'Mecânica'
    ],
    'inicio': pd.to_datetime([
        '2024-01-01', '2024-04-15', '2024-07-20',
        '2024-01-15', '2024-05-16', '2024-09-10',
        '2024-02-01', '2024-05-19', '2024-08-25',
        '2024-02-15', '2024-06-10', '2024-10-05',
        '2024-03-05', '2024-07-15', '2024-11-01'
    ]),
    'fim': pd.to_datetime([
        '2024-02-05', '2024-05-15', '2024-08-20',
        '2024-03-20', '2024-06-20', '2024-11-10',
        '2024-03-03', '2024-06-19', '2024-09-25',
        '2024-04-10', '2024-07-10', '2024-11-20',
        '2024-04-05', '2024-08-15', '2024-12-01'
    ])
}

df = pd.DataFrame(data)

# Criar gráfico de Gantt
fig = px.timeline(df, x_start="inicio", x_end="fim", y="Tipo de Manutenção", color="Tipo de Manutenção", labels={"Tipo de Manutenção": "Tipo de Manutenção"})

# Data da reforma
data_reforma = pd.to_datetime('2024-05-16')

# Adicionar linha vertical para a data da reforma
fig.add_vline(x=data_reforma, line_width=2, line_dash="dash", line_color="red")

# Configurações adicionais para melhor visualização
fig.update_yaxes(categoryorder="total ascending")  # Organiza as tarefas no eixo Y pela ordem de início

# Mostrar o gráfico no Streamlit
st.plotly_chart(fig,use_container_width=True)

# Ordenar por 'Tipo de Manutenção' e 'inicio'
df.sort_values(by=['Tipo de Manutenção', 'inicio'], inplace=True)

# Calcular a diferença de dias entre o fim de uma manutenção e o início da próxima
df['Próximo Início'] = df.groupby('Tipo de Manutenção')['inicio'].shift(-1)
df['Dias até próxima manutenção'] = (df['Próximo Início'] - df['fim']).dt.days

# Segmentar as manutenções antes e depois da data da reforma
df['Período'] = df['inicio'].apply(lambda x: 'Antes da Reforma' if x < data_reforma else 'Depois da Reforma')

# Calcular a média de dias até a próxima manutenção para cada tipo e período
media_dias_periodo = df.groupby(['Tipo de Manutenção', 'Período'])['Dias até próxima manutenção'].mean().unstack()

# Contar quantas manutenções por tipo e por período
contagem_manutencoes = df.groupby(['Tipo de Manutenção', 'Período']).size().unstack(fill_value=0)


col_media_dias, col_divisor,col_manut_antes_depois = st.columns([2,0.01,2])


with col_media_dias:
    # Exibir a média de dias no Streamlit
    st.write("Média de dias até a próxima manutenção por tipo e período:")
    st.dataframe(media_dias_periodo,use_container_width=True)


with col_manut_antes_depois:

    min_val = contagem_manutencoes.min().min()
    max_val = contagem_manutencoes.max().max()

    styled_pivot_df = contagem_manutencoes.style.applymap(lambda x: color_coding(x, min_val, max_val))

    # Exibir a contagem de manutenções no Streamlit
    st.write("Quantidade de manutenções por tipo e período:")
    st.dataframe(styled_pivot_df, use_container_width=True)