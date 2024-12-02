import pandas as pd
import re

# Exemplo de DataFrame
dados = {
    "endereco_completo": [
        "R 1 das flores, 200 loja 2",
        "Av. Brasil 456",
        "Praça da Liberdade, 789 Bloco B",
        "Estrada Velha 1020",
        "Rua das Laranjeiras 15 Ap 301",
        "Rua Setor Bancário Sul Qd. 2 Bloco F",
        "CLN 104 Bloco C Loja 30",
        "SQS 308 Bloco G Ap 102",
        "SHIN QI 5 Conjunto 3 Casa 22",
        "SMAS Trecho 3, Lote 9",
        "Rua Augusta 123 Bloco A",
        "Avenida Paulista, 1578 Loja 5",
        "Alameda Santos 45 Ap 304",
        "Estrada do M'Boi Mirim, 1020 Casa 2",
        "Rua 25 de Março 789 Loja 23",
        "Rua Castro Alves 20 30",
        "Praça da Sé 45",
        "Rodovia Raposo Tavares 12500",
        "Travessa João Ramalho 321 Bloco B",
        "Vila Mariana Rua 2 Ap 1201"
    ]
}

df = pd.DataFrame(dados)

# Função para processar endereços e separar os casos de Brasília
def processar_endereco(texto):
    texto = texto.strip()  # Remove espaços extras no início/fim
    complemento = ""
    numero = ""
    
    # Detectar padrões de Brasília
    padrao_brasilia = r"(CLN|SQS|SHIN|SMAS|Qd\.|Quadra|Bloco|Conjunto|Trecho|Lote)"
    if re.search(padrao_brasilia, texto, re.IGNORECASE):
        return pd.Series([texto, None, None, "Sim"])  # Marcar como pendente para Brasília
    
    # Remover todas as vírgulas antes de continuar
    texto = texto.replace(",", "")
    
    # Identificar e separar o complemento (ex.: Loja, Bloco, Ap)
    match_complemento = re.search(r"(Loja|LT|Bloco|Ap|Apto)\s*\d*\w*", texto, re.IGNORECASE)
    if match_complemento:
        complemento = match_complemento.group(0)
        texto = texto.replace(complemento, "").strip()
    
    # Adicionar vírgula antes do último número se não houver vírgula já
    texto = re.sub(r"(\d+)(?!.*\d)(?!,)", r", \1", texto)

    # Separar números que estão após a vírgula
    if "," in texto:
        numero = texto.split(",")[-1].strip()
        texto = texto.split(",")[0].strip()
    
    return pd.Series([texto, numero, complemento, "Não"])

# Aplicar o processamento ao DataFrame
df[["endereco", "numero", "complemento", "pendente_brasilia"]] = df["endereco_completo"].apply(processar_endereco)

# Criar DataFrames separados
df_pendentes = df[df["pendente_brasilia"] == "Sim"].drop(columns=["pendente_brasilia"])
df_processados = df[df["pendente_brasilia"] == "Não"].drop(columns=["pendente_brasilia"])

# Exibir resultados
print("Endereços Processados:")
print(df_processados)

print("\nEndereços Pendentes (Brasília):")
print(df_pendentes)
