import pandas as pd
import plotly.express as px
import streamlit as st
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

st.set_page_config(
    page_title="TESTE",
    page_icon="🧊",
    layout="wide",
)

with st.sidebar:
    st.write("Testes Ronald")

data = {
    'Tipo de Manutenção': ['Ar Condicionado'] * 3 + ['Elétrica'] * 3 + ['Civil'] * 3 + ['Hidráulica'] * 3 + ['Mecânica'] * 3,
    'inicio': pd.to_datetime(['2024-01-01', '2024-04-15', '2024-07-20', '2024-01-15', '2024-05-16', '2024-09-10', '2024-02-01', '2024-05-19', '2024-08-25', '2024-02-15', '2024-06-10', '2024-10-05', '2024-03-05', '2024-07-15', '2024-11-01']),
    'fim': pd.to_datetime(['2024-02-05', '2024-05-15', '2024-08-20', '2024-03-20', '2024-06-20', '2024-11-10', '2024-03-03', '2024-06-19', '2024-09-25', '2024-04-10', '2024-07-10', '2024-11-20', '2024-04-05', '2024-08-15', '2024-12-01'])
}

df = pd.DataFrame(data)

fig = px.timeline(df, x_start="inicio", x_end="fim", y="Tipo de Manutenção", color="Tipo de Manutenção", labels={"Tipo de Manutenção": "Tipo de Manutenção"},)

# Remover a legenda
fig.update_layout(showlegend=False)

# Ajustar tamanho da fonte dos rótulos do eixo Y
fig.update_yaxes(tickfont=dict(size=16))

# Adicionar linhas divisoras, anotações e fundo de reforma
unique_maintenance_types = df['Tipo de Manutenção'].unique()
for i, maint_type in enumerate(unique_maintenance_types[:-1]):
    fig.add_shape(type='line',
                  x0=df['inicio'].min(),
                  y0=i + 0.5,
                  x1=df['fim'].max(),
                  y1=i + 0.5,
                  line=dict(color="rgba(255, 255, 255, 0.2)", width=2))

data_reforma1 = pd.to_datetime('2024-04-01')
data_reforma2 = pd.to_datetime('2024-05-16')
fig.add_vline(x=data_reforma1, line_width=2, line_dash="dash", line_color="red")
fig.add_vline(x=data_reforma2, line_width=2, line_dash="dash", line_color="red")
fig.add_vrect(x0=data_reforma1, x1=data_reforma2, fillcolor="lightgrey", opacity=0.5, line_width=0)

# Mostrar o gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)