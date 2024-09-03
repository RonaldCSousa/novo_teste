import pandas as pd

# Dados iniciais
data = {
    "AGENCIA": [1, 1, 1, 2, 2, 3],
    "COMODO": ["TERREO", "TERREO", "1 PAVIMENTO", "TERREO", "2 PAVIMENTO", "1 PAVIMENTO"],
    "METRAGEM": [50, 20, 300, 150, 200, 100],
    "STATUS": ["UTILIZADO", "DISPONIVEL", "UTILIZADO", "DISPONIVEL", "UTILIZADO", "UTILIZADO"]
}

df = pd.DataFrame(data)

# Função que usa iterrows para criar uma string de informações concatenadas
def concatenate_info(row):
    result = []
    for _, row in row.iterrows():
        result.append(f"{row['COMODO']}: {row['METRAGEM']}")
    return ', '.join(result)

def processing_data_concated_columns(df, status,name_column):

    df = df[df["STATUS"] == status]
    # Aplicando a função usando groupby e apply
    result = df.groupby('AGENCIA').apply(concatenate_info).reset_index(name=name_column)

    return result


def sum_values(df):
    # Agrupamento por AGENCIA e STATUS, somando a METRAGEM
    df_groupby = df.groupby(["AGENCIA", "STATUS"])["METRAGEM"].sum().reset_index()

    # Usando pivot para criar colunas para cada STATUS, mantendo AGENCIA como índice
    df_pivot = df_groupby.pivot(index="AGENCIA", columns="STATUS", values="METRAGEM")

    df_pivot = df_pivot.fillna(0)

    df_pivot = df_pivot.astype("int")

    return df_pivot

df_concant = processing_data_concated_columns(df=df, status="UTILIZADO",name_column="DETALHE ÁREA UTILIZADA")
df_sum = sum_values(df=df)

df_final = pd.merge(left=df_sum,right=df_concant,on="AGENCIA")


# Exibindo o resultado final
print(df_concant)
print(df_sum)
print(df_final)
