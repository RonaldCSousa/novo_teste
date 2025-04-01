import streamlit as st

# CSS customizado para a tabela com cores do Itaú Unibanco, ajustando o tamanho das células
css_content = """
    <style>
        /* Estilo geral da tabela */
        table {
            width: 80%;  /* Define a largura da tabela para 80% da largura da página */
            border-collapse: collapse;  /* Faz com que as bordas das células se unam */
            margin: 30px auto;  /* Adiciona uma margem de 30px em cima e embaixo, e centraliza a tabela */
            font-family: 'Arial', sans-serif;  /* Define a fonte da tabela para Arial */
            background-color: #ffffff;  /* Fundo branco */
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);  /* Adiciona uma sombra suave ao redor da tabela */
        }

        /* Estilo das células */
        th, td {
            border: 1px solid #dddddd;  /* Adiciona uma borda de 1px com cor cinza claro */
            padding: 8px 10px;  /* Diminui o espaçamento interno das células para 8px vertical e 10px horizontal */
            text-align: center;  /* Alinha o texto das células ao centro */
            font-size: 12px;  /* Reduz o tamanho da fonte para 12px */
            color: #333;  /* Define a cor do texto como cinza escuro */
        }

        /* Cabeçalhos com fundo azul e texto branco */
        th {
            background-color: #004B87;  /* Define o fundo do cabeçalho com o azul do Itaú */
            color: white;  /* Define a cor do texto do cabeçalho como branco */
            font-weight: bold;  /* Define o texto do cabeçalho como negrito */
        }

        /* Efeito de hover nas células */
        tr:hover {
            background-color: #f1f1f1;  /* Quando o usuário passar o mouse sobre a linha, o fundo muda para cinza claro */
            cursor: pointer;  /* Muda o cursor para indicar que é interativo */
        }

        /* Bordas arredondadas */
        table, th, td {
            border-radius: 5px;  /* Adiciona bordas arredondadas à tabela e às células */
        }

        /* Estilo para a primeira coluna, destacando-a com laranja */
        .merge {
            background-color: #FF6A13;  /* Define o fundo da primeira coluna com o laranja do Itaú */
            color: white;  /* Define o texto dessa coluna como branco */
            font-weight: bold;  /* Define o texto da primeira coluna como negrito */
        }

        /* Estilo para células de descrição */
        td {
            font-style: italic;  /* Define o texto das células de descrição como itálico */
        }
    </style>
"""

# HTML para a tabela customizada com cores do Itaú Unibanco e células menores
html_content = """
    <table>
        <tr>
            <th rowspan="6" class="merge">Banco</th>
            <th>Caixas</th>
            <td>Caixas físicos e automáticos</td>
        </tr>
        <tr>
            <th>Cliente</th>
            <td>Clientes que utilizam os serviços bancários</td>
        </tr>
        <tr>
            <th>Finanças</th>
            <td>Gestão das finanças internas e externas</td>
        </tr>
        <tr>
            <th rowspan="3" class="merge">Caixa</th>
            <th>Dinheiro</th>
            <td>Dinheiro disponível no caixa eletrônico</td>
        </tr>
        <tr>
            <th>Cheque</th>
            <td>Cheques para transações e compensações</td>
        </tr>
        <tr>
            <th>Pix</th>
            <td>Transações via sistema de pagamento instantâneo</td>
        </tr>
        <tr>
            <th rowspan="2" class="merge">Empréstimos</th>
            <th>Crédito Pessoal</th>
            <td>Empréstimos para pessoas físicas com diversas condições</td>
        </tr>
        <tr>
            <th>Empréstimo Imobiliário</th>
            <td>Empréstimos para a compra de imóveis</td>
        </tr>
    </table>
    <br>
    <table>
        <tr>
            <th rowspan="3" class="merge">Analista</th>
            <th>Testes</th>
            <td>Testes de qualidade para novos sistemas</td>
        </tr>
        <tr>
            <th>Salário</th>
            <td>Salário base mais bônus por desempenho</td>
        </tr>
        <tr>
            <th>Produção</th>
            <td>Produção de relatórios e acompanhamento de metas</td>
        </tr>
        <tr>
            <th rowspan="2" class="merge">Gestão</th>
            <th>Estratégia</th>
            <td>Planejamento estratégico da empresa</td>
        </tr>
        <tr>
            <th>Operações</th>
            <td>Gestão das operações diárias e processos internos</td>
        </tr>
    </table>
"""


    # Exibir tudo em uma única chamada com "+" para combinar
st.markdown(css_content + html_content, unsafe_allow_html=True)


import pandas as pd
import streamlit as st

# Criar um DataFrame de exemplo
data = {
    'Categoria': ['Banco', 'Banco', 'Banco', 'Caixa', 'Caixa', 'Caixa', 'Empréstimos', 'Empréstimos','Empréstimos'],
    'Subcategoria': ['Caixas', 'Cliente', 'Finanças', 'Dinheiro', 'Cheque', 'Pix', 'Crédito Pessoal', 'Empréstimo Imobiliário','Crédito Pessoal'],
    'Descrição': [
        'Caixas físicos e automáticos',
        'Clientes que utilizam os serviços bancários',
        'Gestão das finanças internas e externas',
        'Dinheiro disponível no caixa eletrônico',
        'Cheques para transações e compensações',
        'Transações via sistema de pagamento instantâneo',
        'Empréstimos para pessoas físicas com diversas condições',
        'Empréstimos para a compra de imóveis',
        'Empréstimos para a compra de imóveis',
    ]
}

df = pd.DataFrame(data)

# Definindo o CSS customizado
css_content = """
    <style>
        table {
            width: 80%;
            border-collapse: collapse;
            margin: 30px auto;
            font-family: 'Arial', sans-serif;
            background-color: #ffffff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        th, td {
            border: 1px solid #dddddd;
            padding: 8px 10px;
            text-align: center;
            font-size: 12px;
            color: #333;
        }
        th {
            background-color: #004B87;
            color: white;
            font-weight: bold;
        }
        tr:hover {
            background-color: #f1f1f1;
            cursor: pointer;
        }
        table, th, td {
            border-radius: 5px;
        }
        .merge {
            background-color: #FF6A13;
            color: white;
            font-weight: bold;
        }
        td {
            font-style: italic;
        }
    </style>
"""

# Criando o HTML dinamicamente
html_content = "<table>"

# Cabeçalhos da tabela
html_content += "<tr><th>Categoria</th><th>Subcategoria</th><th>Descrição</th></tr>"

# Variável para armazenar a categoria anterior
previous_categoria = None

# Gerar a tabela com base nos dados do DataFrame
for index, row in df.iterrows():
    categoria = row['Categoria']
    subcategoria = row['Subcategoria']
    descricao = row['Descrição']

    # Se a categoria for a mesma da linha anterior, não exibe novamente
    categoria_display = categoria if categoria != previous_categoria else ""

    # Adiciona a linha com a descrição, exibindo ou não a categoria
    html_content += f"<tr><td>{categoria_display}</td><td>{subcategoria}</td><td>{descricao}</td></tr>"

    # Atualiza a categoria anterior
    previous_categoria = categoria

html_content += "</table>"

# Exibir a tabela no Streamlit com CSS aplicado
st.markdown(css_content + html_content, unsafe_allow_html=True)


import pandas as pd
import streamlit as st

# Criar um DataFrame de exemplo
data = {
    'Categoria': ['Banco', 'Banco', 'Banco', 'Caixa', 'Caixa', 'Caixa', 'Empréstimos', 'Empréstimos', 'Empréstimos'],
    'Subcategoria': ['Caixas', 'Cliente', 'Finanças', 'Dinheiro', 'Cheque', 'Pix', 'Crédito Pessoal', 'Empréstimo Imobiliário', 'Crédito Pessoal'],
    'Descrição': [
        'Caixas físicos e automáticos',
        'Clientes que utilizam os serviços bancários',
        'Gestão das finanças internas e externas',
        'Dinheiro disponível no caixa eletrônico',
        'Cheques para transações e compensações',
        'Transações via sistema de pagamento instantâneo',
        'Empréstimos para pessoas físicas com diversas condições',
        'Empréstimos para a compra de imóveis',
        'Empréstimos para a compra de imóveis',
    ]
}

df = pd.DataFrame(data)

# Definindo o CSS customizado
css_content = """
    <style>
        table {
            width: 80%;
            border-collapse: collapse;
            margin: 30px auto;
            font-family: 'Arial', sans-serif;
            background-color: #ffffff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        th, td {
            border: 1px solid #dddddd;
            padding: 8px 10px;
            text-align: center;
            font-size: 12px;
            color: #333;
        }
        th {
            background-color: #004B87;
            color: white;
            font-weight: bold;
        }
        tr:hover {
            background-color: #f1f1f1;
            cursor: pointer;
        }
        table, th, td {
            border-radius: 5px;
        }
        .merge {
            background-color: #FF6A13;
            color: white;
            font-weight: bold;
        }
        td {
            font-style: italic;
        }
    </style>
"""

# Filtrando categorias únicas
categorias = df['Categoria'].unique()

# Gerando uma tabela separada para cada categoria
for categoria in categorias:
    # Filtrando os dados por categoria
    df_categoria = df[df['Categoria'] == categoria]

    # Criando o HTML da tabela
    html_content = "<table>"

    # Cabeçalhos da tabela
    html_content += "<tr><th>Categoria</th><th>Subcategoria</th><th>Descrição</th></tr>"

    # Variável para armazenar a categoria anterior
    previous_categoria = None

    # Adicionando as linhas da tabela com o índice da categoria
    for index, row in df_categoria.iterrows():
        subcategoria = row['Subcategoria']
        descricao = row['Descrição']

        # Se a categoria for a mesma da linha anterior, não exibe novamente
        categoria_display = categoria if categoria != previous_categoria else ""

        # Adiciona a linha com a descrição, exibindo ou não a categoria
        html_content += f"<tr><td>{categoria_display}</td><td>{subcategoria}</td><td>{descricao}</td></tr>"

        # Atualiza a categoria anterior
        previous_categoria = categoria

    html_content += "</table>"

    # Exibindo cada tabela para a categoria
    st.markdown(css_content + html_content, unsafe_allow_html=True)
