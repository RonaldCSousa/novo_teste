import streamlit as st
import pandas as pd

def criar_dataframe():
    return pd.DataFrame([
        {"Ativo": False, "codigo_analista": 1001, "nome": "Ana", "cargo": "Pleno", "superintendencia": "Tecnologia", "gerencia": "Logística", "coordenacao": "Equipe A", "Tipo": "Entrada"},
        {"Ativo": False, "codigo_analista": 1002, "nome": "Bruno", "cargo": "Sênior", "superintendencia": "Operações", "gerencia": "Logística", "coordenacao": "Equipe B", "Tipo": "Saída"},
        {"Ativo": False, "codigo_analista": 1003, "nome": "Carlos", "cargo": "Júnior", "superintendencia": "Tecnologia", "gerencia": "Desenvolvimento", "coordenacao": "Equipe C", "Tipo": "Entrada"},
        {"Ativo": False, "codigo_analista": 1004, "nome": "Daniela", "cargo": "Júnior", "superintendencia": "Financeira", "gerencia": "Risco", "coordenacao": "Equipe A", "Tipo": "Saída"},
        {"Ativo": False, "codigo_analista": 1005, "nome": "Eduardo", "cargo": "Pleno", "superintendencia": "Financeira", "gerencia": "Logística", "coordenacao": "Equipe B", "Tipo": "Entrada"},
    ])

def exibir_selecao_tipo():
    return st.radio("Tipo de seleção", ["Única", "Múltipla"], horizontal=True)

def filtrar_dataframe(df, selecao_tipo):
    if selecao_tipo == "Múltipla":
        filtro_tipo = st.radio("Filtrar por:", ["Entrada", "Saída"], horizontal=True)
        return df[df["Tipo"] == filtro_tipo], filtro_tipo
    return df, None

def exibir_tabela(df):
    df_visualizacao = df[["Ativo", "nome", "cargo", "superintendencia"]]
    return st.data_editor(df_visualizacao, num_rows="fixed", key="data_editor")

def exibir_detalhes_selecionados(df, selecao_tipo, filtro_tipo):
    selected_analyst = df.loc[df["Ativo"] == True]
    ativos_selecionados = len(selected_analyst)

    if selecao_tipo == "Única" and ativos_selecionados > 1:
        st.info("Selecione APENAS um analista ou troque para a MULTIPLA seleção")
    elif ativos_selecionados > 0:
        titulo = "Dados completos do Analista Selecionado" if selecao_tipo == "Única" else f"Dados completos de {ativos_selecionados} Analista(s) Selecionado(s) ({filtro_tipo})"
        st.subheader(titulo)
        st.data_editor(selected_analyst, num_rows="fixed", key="data_editor_final")
    elif selecao_tipo == "Múltipla":
        st.info(f"Nenhum analista de {filtro_tipo} foi selecionado.")

def main():
    st.title("Seleção de Analistas")
    df = criar_dataframe()
    selecao_tipo = exibir_selecao_tipo()
    df_filtrado, filtro_tipo = filtrar_dataframe(df, selecao_tipo)
    df_editado = exibir_tabela(df_filtrado)
    df["Ativo"] = df_editado["Ativo"]
    exibir_detalhes_selecionados(df, selecao_tipo, filtro_tipo)

if __name__ == "__main__":
    main()
