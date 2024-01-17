import pandas as pd

def criar_tipo_movimentacao(df):
    # Converter a coluna 'data' para o tipo datetime
    df['data'] = pd.to_datetime(df['data'])

    # Ordenar o dataframe por 'numfunc' e 'data' em ordem decrescente
    df = df.sort_values(by=['numfunc', 'data'], ascending=[True, False])

    # Criar a coluna 'tipo_movimentacao' com base na comparação entre a data mais recente e a data anterior
    df['tipo_movimentacao'] = df.duplicated(subset='numfunc', keep='first').map({True: 'Entrada', False: 'Saida'})

    # Preencher a coluna 'tipo_movimentacao' com os valores da coluna 'movimentacao' nos casos não duplicados
    df.loc[~df.duplicated(subset='numfunc', keep=False), 'tipo_movimentacao'] = df['movimentacao']

    return df

# Dados de exemplo
data = {'numfunc': [1, 1, 2],
        'nome_analista': ['Ana', 'Ana', 'Bob'],
        'gerencia': ['Gerencia_Anterior', 'Gerencia_Atual', 'Gerencia_Unica'],
        'coordenacao': ['Coord_Anterior', 'Coord_Atual', 'Coord_Unica'],
        'data': ['2022-01-01', '2022-01-08', '2022-01-15'],
        'movimentacao': ['Saida', 'Entrada', 'Unica']}

# Criar dataframe
df = pd.DataFrame(data)

# Aplicar a função
df = criar_tipo_movimentacao(df)

# Exibir dataframe com a nova coluna
print(df)
