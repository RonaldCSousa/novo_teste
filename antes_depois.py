import pandas as pd

# Dados iniciais
dados = {
    "agencia": [3, 10, 18, 18, 18, 20],
    "tipo de manutenção": ["Civil", "Porta Automática", "Porta Automática", "Hidráulica", "Porta Automática", "Civil"],
    "data da manutenção": pd.to_datetime(["2023-02-19", "2023-09-23", "2023-03-18", "2023-08-14", "2023-09-27", "2023-10-15"]),
    "data da obra": pd.to_datetime(["2023-11-07", "2023-08-19", "2023-05-22", "2023-12-28", "2023-01-26", pd.NaT])
}

df = pd.DataFrame(dados)

# Criando a coluna 'teve reforma'
df['teve reforma'] = ~df['data da obra'].isna()

# Determinar se a manutenção foi antes ou depois da obra
df['depois da obra'] = df['data da manutenção'] > df['data da obra']

# Agrupar por agência, tipo de manutenção e depois da obra, contando ocorrências
resultado_agrupado = df.groupby(['agencia', 'tipo de manutenção', 'teve reforma', 'depois da obra']).size().reset_index(name='quantidade')

# Pivotear os dados para o formato final
resultado_final = resultado_agrupado.pivot_table(index=['agencia', 'tipo de manutenção', 'teve reforma'], columns='depois da obra', values='quantidade', fill_value=0).reset_index()

# Renomear colunas para refletir os dados de maneira clara
resultado_final.columns = ['agencia', 'tipo de manutenção', 'teve reforma', 'quantidade_antes', 'quantidade_depois']

# Separação dos dados antes e depois da obra
df_antes = resultado_final[['agencia', 'tipo de manutenção', 'quantidade_antes', 'teve reforma']]
df_depois = resultado_final[['agencia', 'tipo de manutenção', 'quantidade_depois', 'teve reforma']]

# Criação de uma coluna única 'qtd' para quantidades
df_antes['qtd'] = df_antes['quantidade_antes']
df_depois['qtd'] = df_depois['quantidade_depois']

# Remoção das colunas de quantidades originais
df_antes.drop("quantidade_antes", axis=1, inplace=True)
df_depois.drop("quantidade_depois", axis=1, inplace=True)

# Concatenação dos DataFrames ajustados
df_concat = pd.concat([df_antes, df_depois])

# Ordenação por agência
df_concat.sort_values(by='agencia', inplace=True)

print(df_concat)
