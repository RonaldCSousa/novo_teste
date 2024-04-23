import streamlit as st
import streamlit_antd_components as sac
import pandas as pd
from streamlit_extras.stylable_container import stylable_container

# Dados dos analistas
dados = {
    "cod_analista": [1, 2, 3, 4, 5],
    "nome_analista": ["Ana Silva", "Bruno Costa", "Carla Dias", "Diego Ramos", "Eliana Souza"]
}

# Criando o DataFrame
df_analistas = pd.DataFrame(dados)

# Inicializando estado da aba, se necessário
if 'testes' not in st.session_state:
    st.session_state['testes'] = 'Analista'
if 'cod_analista' not in st.session_state:
    st.session_state['cod_analista'] = None
if 'nome_analista' not in st.session_state:
    st.session_state['nome_analista'] = None



if st.button("testes"):

    with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    border: 5px solid rgba(255, 255, 255);
                    border-radius: 0.5rem;
                    padding: calc(1em - 1px)
                }
                """,
        ):
        # Definição das abas
        tab_state = sac.tabs([
            sac.TabsItem(label='Analista', icon="table"),
            sac.TabsItem(label='Estag', icon='table'),
        ], key="testes", align='center', variant='outline')

        # Mostrando as abas
        st.write(tab_state)

        if st.session_state["testes"] == "Analista":
            opcoes = df_analistas['nome_analista'].tolist()
            escolha_analista = st.selectbox("Selecione um analista:", options=opcoes, index=opcoes.index(st.session_state['nome_analista']) if st.session_state['nome_analista'] in opcoes else 0)
            if escolha_analista:
                st.session_state['nome_analista'] = escolha_analista
                st.session_state['cod_analista'] = df_analistas[df_analistas['nome_analista'] == escolha_analista]['cod_analista'].iloc[0]

        if st.session_state["testes"] == "Estag":
            opcoes = df_analistas['cod_analista'].tolist()
            escolha_cod = st.selectbox("Selecione um código de analista:", options=opcoes, index=opcoes.index(st.session_state['cod_analista']) if st.session_state['cod_analista'] in opcoes else 0)
            if escolha_cod:
                st.session_state['cod_analista'] = escolha_cod
                st.session_state['nome_analista'] = df_analistas[df_analistas['cod_analista'] == escolha_cod]['nome_analista'].iloc[0]

        st.markdown(f"Nome do analista: {st.session_state['nome_analista'] if st.session_state['nome_analista'] else 'N/A'}")
        st.markdown(f"Código do analista: {st.session_state['cod_analista'] if st.session_state['cod_analista'] else 'N/A'}")
