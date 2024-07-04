import streamlit as st
from streamlit_echarts import st_echarts

data = {
    "legend": {
        "data": ["orcSSRA", "orcRT", "totalSSRA", "totalRT", "Diferença"]
    },  # DEFINE O QUE VAI APARECER NA LEGENDA
    "tooltip": {},  # O TOOLTIP ESTÁ COM CONFIGURAÇÃO DEFAULT, QUALQUER OUTRO FORMATO, DEVEMOS ADICIONAR AQUI! PS: RETIRAR ISSO DO CÓDIGO DESABILITA O TOOLTIP!
    "dataset": {
        # ! TORNAR DINÂMICO: PASSAR OS NOMES DAS COLUNAS QUE SERÃO UTILIZADAS DENTRO DO GRÁFICO
        "dimensions": ["Data", "orcSSRA", "orcRT", "totalSSRA", "totalRT", "Diferença"],
        # ! TORNAR DINÂMICO: LISTA DE DICTS COM OS VALORES (DF)
        "source": [
            {
                "Data": "jun/23",
                "orcSSRA": 10,
                "orcRT": 23,
                "totalSSRA": 65,
                "totalRT": 30,
            },
            {
                "Data": "jul/23",
                "orcSSRA": 13,
                "orcRT": 98,
                "totalSSRA": 12,
                "totalRT": 87,
            },
        ],
    },
    "xAxis": {
        "type": "category"
    },  # DEFINE O EIXO X SENDO AS CATEGORIAS, NO CASO AS DATAS
    "yAxis": {},  # PRECISA DISSO, O CÓDIGO QUEBRA SEM!!
    # ! LISTA DE DICTS QUE VAI DEFINIR COMO DEVE SER FEITO O AGRUPAMENTO (PODE OU NÃO SER DINÂMICO)
    "series": [
        {
            "type": "bar",  # DEFINE O TIPO DA GRÁFICO --> BARRA
            "name": "orcSSRA",  # DEFINE O NOME DO DADO QUE DEVE RETORNAR O VALOR (CONVERSA COM A LEGENDA)
            "stack": "orc",  # DEFINE A BARRA EM QUE QUE O VALOR DEVE SER EMPILHADO --> orçados
            "itemStyle": {"color": "#00008B"},  # DEFINE A COR DO VALOR (BARRA)
            "label": {
                "show": True,
                "position": "inside",
            },  # DEFINE A VISUALIZAÇÃO DA LABEL E SUA POSIÇÃO
        },
        {
            "type": "bar",  # DEFINE O TIPO DA GRÁFICO --> BARRA
            "name": "orcRT",  # DEFINE O NOME DO DADO QUE DEVE RETORNAR O VALOR (CONVERSA COM A LEGENDA)
            "stack": "orc",  # DEFINE A BARRA EM QUE QUE O VALOR DEVE SER EMPILHADO --> orçados
            "itemStyle": {"color": "#ADD8E6"},  # DEFINE A COR DO VALOR (BARRA)
            "label": {
                "show": True,
                "position": "inside",
            },  # DEFINE A VISUALIZAÇÃO DA LABEL E SUA POSIÇÃO
        },
        {
            "type": "bar",  # DEFINE O TIPO DA GRÁFICO --> BARRA
            "name": "totalSSRA",  # DEFINE O NOME DO DADO QUE DEVE RETORNAR O VALOR (CONVERSA COM A LEGENDA)
            "stack": "total",  # DEFINE A BARRA EM QUE QUE O VALOR DEVE SER EMPILHADO --> totais
            "itemStyle": {"color": "#FF8C00"},  # DEFINE A COR DO VALOR (BARRA)
            "label": {
                "show": True,
                "position": "inside",
            },  # DEFINE A VISUALIZAÇÃO DA LABEL E SUA POSIÇÃO
        },
        {
            "type": "bar",  # DEFINE O TIPO DA GRÁFICO --> BARRA
            "name": "totalRT",  # DEFINE O NOME DO DADO QUE DEVE RETORNAR O VALOR (CONVERSA COM A LEGENDA)
            "stack": "total",  # DEFINE A BARRA EM QUE QUE O VALOR DEVE SER EMPILHADO --> totais
            "itemStyle": {"color": "#FFD700"},  # DEFINE A COR DO VALOR (BARRA)
            "label": {
                "show": True,
                "position": "inside",
            },  # DEFINE A VISUALIZAÇÃO DA LABEL E SUA POSIÇÃO
        },
        {
            "type": "line",  # TIPO DO GRÁFICO
            "name": "Diferença",  # NOME DA LINNHA
            # ! TORNAR DINÂMICO: PARA CADA PONTO DA LINHA FAZER UM DICT CONTENDO AS CHAVES
            # ! --> value (VALOR DO PONTO NO GRÁFICO): NORMALIZAÇÃO DO VALOR DA DIFERENÇA ENTRE AS BARRAS, COM MAX. VALENDO A MENOR BARRA E
            # ! MIN COM O VALOR DA MAIOR BARRA. O RESULTADO DEVE SER MULTIPLICADO POR 10 E ADICIONADO DE MIN. + 10 (não sei se essa é a melhor maneira ahahah)
            # ! --> labels (VALOR QUE SERÁ VISUALIZADO NA LABEL): DIFERENÇA ENTRE SOMA DOS orçados E SOMA dos totais
            "data": [
                {
                    "value": (((10 + 23) - (65 + 30)) - 111) / (33 - 111) * 10
                    + 111
                    + 10,
                    "label": {"show": True, "position": "top", "formatter": f"{-62}"},
                },
                {
                    "value": (((13 + 98) - (12 + 87)) - 111) / (33 - 111) * 10
                    + 111
                    + 10,
                    "label": {"show": True, "position": "top", "formatter": f"{12}"},
                },
            ],
            "itemStyle": {"color": "red"},  # COR DA LINHA --> ESTÁ COMO VERMELHA
        },
    ],
}

st_echarts(options=data, height="600px")
