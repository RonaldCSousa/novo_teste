import sqlite3
import pandas as pd

# Seu DataFrame
df = pd.DataFrame({
    'FUNCID': ['2', '3', '4'],
    'DATABASE': ['2023-12-27', '2023-12-30', '2023-12-29'],
    'COORDENACAO': ['Latitude1, Longitude2', 'Latitude2, Longitude2', 'Latitude3, Longitude3']
    # Adicione mais colunas e valores conforme necessário
})

# Converter a coluna 'DATABASE' para o formato correto
#df['DATABASE'] = pd.to_datetime(df['DATABASE']).dt.strftime('%Y-%m-%d')

# Conectar ao banco de dados SQLite
caminho_banco_dados = '/Trabalhos Pessoais/Capacita - UDA/teste_sqlite.db'
conn = sqlite3.connect(caminho_banco_dados)
cursor = conn.cursor()

# Substitua 'sua_tabela' pelo nome da tabela em seu banco de dados
nome_tabela = 'testes'

# Gerar uma lista de listas contendo os dados do DataFrame
dados = df.values.tolist()

# Construir a instrução SQL para a inserção apenas se não existir
sql_insert = f'''
    INSERT INTO {nome_tabela} ({', '.join(df.columns)})
    SELECT {', '.join(['?' for _ in df.columns])}
    WHERE NOT EXISTS (
        SELECT 1
        FROM {nome_tabela}
        WHERE {' AND '.join([f'{coluna} = ?' for coluna in df.columns])}
    )
'''

# Executar a inserção usando a instrução WHERE NOT EXISTS
for linha in dados:
    cursor.execute(sql_insert, linha + linha)  # Duplica a lista para atender à quantidade correta de bindings

# Commit para salvar as alterações no banco de dados
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()




