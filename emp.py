import pandas as pd

# Criando o DataFrame inicial com agências e segmentos
data_with_codes = {
    "agencia": ["AG001", "AG001", "AG002", "AG002", "AG003", "AG003", "AG003"],
    "segmento": ["emp", "pro", "emp", "business", "emp", "pro", "business"],
}

df_with_codes = pd.DataFrame(data_with_codes)

# Contando os segmentos por agência
segment_counts = df_with_codes.groupby(["agencia", "segmento"]).size().unstack(fill_value=0)

# Criando a coluna 'qtd_segmentos' com apenas os segmentos que têm contagem > 0
segment_counts['qtd_segmentos'] = segment_counts.apply(
    lambda row: ', '.join(f"{seg}: {int(count)}" for seg, count in row.items() if count > 0),
    axis=1
)

# Selecionando apenas 'agencia' e 'qtd_segmentos'
result = segment_counts.reset_index()[['agencia', 'qtd_segmentos']]

# Exibindo o resultado
print(result)
