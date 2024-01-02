import sqlite3
import pandas as pd

# Seu DataFrame
df = pd.DataFrame({
    'FUNCID': ['2', '3', '4'],  
    'DATABASE': ['2023-12-27', '2023-12-28', '2023-12-29'],
    'COORDENACAO': ['Latitude1, Longitude2', 'Latitude2, Longitude2', 'Latitude3, Longitude3']
    # Adicione mais colunas e valores conforme necessário
})

# Conectar ao banco de dados SQLite
caminho_banco_dados = '/Trabalhos Pessoais/Capacita - UDA/teste_sqlite.db'
conn = sqlite3.connect(caminho_banco_dados)
cursor = conn.cursor()

# Substitua 'sua_tabela' pelo nome da tabela em seu banco de dados
nome_tabela = 'testes'

# Ajustar as colunas para excluir a coluna de autoincremento (por exemplo, 'id')
colunas_sem_autoincremento = [coluna for coluna in df.columns if coluna != 'id']

# Gerar uma lista de tuplas contendo os dados do DataFrame
dados = [tuple(x) for x in df[colunas_sem_autoincremento].to_numpy()]

# Construir a instrução SQL para a inserção
sql_insert = f"INSERT INTO {nome_tabela} ({', '.join(colunas_sem_autoincremento)}) VALUES ({', '.join(['?' for _ in colunas_sem_autoincremento])})"

# Verificar a existência de dados duplicados antes da inserção
unique_check_sql = f"SELECT COUNT(*) FROM {nome_tabela} WHERE {' AND '.join([f'{col} = ?' for col in colunas_sem_autoincremento])}"
dados_novos = [linha for linha in dados if cursor.execute(unique_check_sql, linha).fetchone()[0] == 0]

# Executar a inserção usando executemany
if dados_novos:
    cursor.executemany(sql_insert, dados_novos)

# Commit para salvar as alterações no banco de dados
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
