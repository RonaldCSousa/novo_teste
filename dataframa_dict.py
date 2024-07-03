import pandas as pd
import streamlit as st

def create_column_configuration(df, name_col, help_col):
    """
    Cria a configuração das colunas do Streamlit usando os valores das colunas especificadas do DataFrame.
    
    Parâmetros:
    df (pd.DataFrame): DataFrame com os dados.
    name_col (str): Nome da coluna para usar como nome na configuração.
    help_col (str): Nome da coluna para usar como ajuda na configuração.
    
    Retorno:
    dict: Dicionário com a configuração das colunas, onde as chaves são os nomes das colunas.
    """
    column_configuration = {}
    for i, row in df.iterrows():
        column_name = row[name_col]
        help_text = row[help_col]
        column_configuration[column_name] = st.column_config.TextColumn(
            column_name, help=help_text
        )
    return column_configuration

# Exemplo de uso com os dados ajustados
data = {
    'nome_coluna': ['agencia', 'diretoria', 'gerencia'],
    'descricao_coluna': ['dados de agencia', 'dados de diretoria', 'dados de gerencia']
}

df = pd.DataFrame(data)

# Criando a configuração das colunas usando a função
column_configuration = create_column_configuration(df, 'nome_coluna', 'descricao_coluna')

# Exibindo a configuração das colunas no Streamlit
# for col_name, col_config in column_configuration.items():
#     st.write(f"Coluna: {col_name}")
#     st.write(col_config)

# Exemplo de como você pode usar a configuração em uma tabela (isso pode variar de acordo com o seu uso específico)
# st.dataframe(df)  # Apenas para exibir o DataFrame no Streamlit

data_teste = {
    "agencia": ["Agencia 1", "Agencia 2", "Agencia 3"],
    "diretoria": ["Diretoria A", "Diretoria B", "Diretoria C"]
}

# Criação do DataFrame
df_teste = pd.DataFrame(data_teste)


st.data_editor(
    df_teste,
    column_config=column_configuration,
    use_container_width=True,
    hide_index=True,
    num_rows="fixed",
)