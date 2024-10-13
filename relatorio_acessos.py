import pandas as pd

# DataFrame de exemplo com múltiplos usuários
df = pd.DataFrame({
    'usuario': ['src.etc Login efetuado por: Ronald Sousa', 
                'src.etc Login efetuado por: Maria Oliveira', 
                'src.etc Login efetuado por: João Silva',
                'src.etc Login efetuado por: Ronald Sousa', 
                'src.etc Login efetuado por: Maria Oliveira'],
    'data': [
        pd.Timestamp('2024-10-13 08:00:00'),
        pd.Timestamp('2024-10-13 08:05:00'),
        pd.Timestamp('2024-10-13 08:20:00'),
        pd.Timestamp('2024-10-13 08:30:00'),
        pd.Timestamp('2024-10-13 09:00:00')
    ]
})

# Limpar a coluna 'usuario'
df['usuario'] = df['usuario'].str.replace(r'src\.etc Login efetuado por: ', '', regex=True)

# Lista de todos os usuários
todos_usuarios = ['Ronald Sousa', 'Maria Oliveira', 'João Silva', 'José Almeida']

# Ordenar pelo tempo de login e agrupar por usuário
df = df.sort_values(by=['usuario', 'data'])

# Função para filtrar registros com intervalo de 10 minutos
def filtrar_intervalo(grupo):
    grupo['diferenca'] = grupo['data'].diff()
    return grupo[(grupo['diferenca'].isnull()) | (grupo['diferenca'] >= pd.Timedelta(minutes=10))]

# Aplicar a função de filtragem para cada usuário
df_filtrado = df.groupby('usuario', group_keys=False).apply(filtrar_intervalo)

# Remover a coluna de diferença, se não for mais necessária
df_filtrado = df_filtrado.drop(columns=['diferenca'])

# 1. Contabilizar a quantidade total de acessos por usuário
total_acessos_por_usuario = df_filtrado['usuario'].value_counts().reset_index()
total_acessos_por_usuario.columns = ['usuario', 'quantidade_acessos']

# 2. Fazer um merge com a lista de todos os usuários
total_acessos_por_usuario = pd.DataFrame(todos_usuarios, columns=['usuario']).merge(
    total_acessos_por_usuario, 
    on='usuario', 
    how='left'
).fillna(0)

# Converter a quantidade de acessos para int
total_acessos_por_usuario['quantidade_acessos'] = total_acessos_por_usuario['quantidade_acessos'].astype(int)

# 3. Adicionar a coluna "TEVE ACESSO ?"
total_acessos_por_usuario['TEVE ACESSO ?'] = total_acessos_por_usuario['quantidade_acessos'].apply(lambda x: 'Sim' if x > 0 else 'Não')

# 4. Trocar a posição das colunas
total_acessos_por_usuario = total_acessos_por_usuario[['usuario', 'TEVE ACESSO ?', 'quantidade_acessos']]

# 5. Contabilizar a quantidade de acessos por data e por usuário
df_acessos_por_data_usuario = df_filtrado.groupby(['usuario', df_filtrado['data'].dt.date]).size().reset_index(name='quantidade_acessos')

# Salvar em um arquivo Excel com duas planilhas
excel_filename = 'quantidade_acessos.xlsx'
with pd.ExcelWriter(excel_filename) as writer:
    total_acessos_por_usuario.to_excel(writer, sheet_name='Total Acessos', index=False)
    df_acessos_por_data_usuario.to_excel(writer, sheet_name='Acessos por Data', index=False)

print(f"Dados salvos em '{excel_filename}' com sucesso!")