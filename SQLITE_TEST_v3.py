import sqlite3
import pandas as pd

# Seu DataFrame
df = pd.DataFrame({
    'FUNCID': ['2', '3', '4'],
    'DATABASE': ['2023-12-27', '2023-12-28', '2023-12-29'],
    'COORDENACAO': ['Latitude1, Longitude2', 'Latitude2, Longitude2', 'Latitude3, Longitude3']
    # Adicione mais colunas e valores conforme necessário
})

# Converter a coluna 'DATABASE' para o formato correto
df['DATABASE'] = pd.to_datetime(df['DATABASE']).dt.strftime('%Y-%m-%d')

# Conectar ao banco de dados SQLite
caminho_banco_dados = '/Trabalhos Pessoais/Capacita - UDA/teste_sqlite.db'
conn = sqlite3.connect(caminho_banco_dados)
cursor = conn.cursor()

# Substitua 'sua_tabela' pelo nome da tabela em seu banco de dados
nome_tabela = 'testes'

# Ler os dados existentes da tabela no banco de dados
df_bd = pd.read_sql_query(f"SELECT * FROM {nome_tabela}", conn)

# Garantir que as colunas 'FUNCID' e 'DATABASE' sejam do mesmo tipo
df['FUNCID'] = df['FUNCID'].astype(df_bd['FUNCID'].dtype)
df['DATABASE'] = pd.to_datetime(df['DATABASE']).dt.strftime('%Y-%m-%d')

# Mesclar os DataFrames com base na coluna 'FUNCID' e 'DATABASE'
df_merged = pd.merge(df, df_bd, on=['FUNCID', 'DATABASE'], how='left', indicator=True)

# Filtrar os dados que estão apenas no DataFrame original
dados_novos = df_merged[df_merged['_merge'] == 'left_only'].drop('_merge', axis=1)

# Fechar a conexão com o banco de dados
conn.close()

# Se houver dados novos, realizar a inserção no banco de dados usando executemany
if not dados_novos.empty:
    conn = sqlite3.connect(caminho_banco_dados)
    colunas_sem_autoincremento = [coluna for coluna in dados_novos.columns if coluna != 'id']
    dados_novos_tuplas = [tuple(x) for x in dados_novos[colunas_sem_autoincremento].to_numpy()]
    
    # Construir a instrução SQL para a inserção
    sql_insert = f"INSERT INTO {nome_tabela} ({', '.join(colunas_sem_autoincremento)}) VALUES ({', '.join(['?' for _ in colunas_sem_autoincremento])})"
    
    # Executar a inserção usando executemany
    cursor.executemany(sql_insert, dados_novos_tuplas)

    # Commit para salvar as alterações no banco de dados
    conn.commit()

    # Fechar a conexão com o banco de dados
    conn.close()




