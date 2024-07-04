import streamlit as st
from streamlit_echarts import st_echarts

data = {
    "legend": {
        "data": ["orcSSRA", "orcRT", "totalSSRA", "totalRT", "Diferença"]
    },
    "tooltip": {},
    "dataset": {
        "dimensions": ["Data", "orcSSRA", "orcRT", "totalSSRA", "totalRT", "Diferença"],
        "source": [
            {"Data": "jun/23", "orcSSRA": 10, "orcRT": 23, "totalSSRA": 65, "totalRT": 30, "Diferença": 0},
            {"Data": "jul/23", "orcSSRA": 13, "orcRT": 98, "totalSSRA": 12, "totalRT": 87, "Diferença": 0},
        ],
    },
    "xAxis": {"type": "category"},
    "yAxis": {"show": False},
    "series": [
        {
            "type": "bar",
            "name": "orcSSRA",
            "stack": "orc",
            "itemStyle": {"color": "#00008B"},
            "label": {"show": True, "position": "inside"},
        },
        {
            "type": "bar",
            "name": "orcRT",
            "stack": "orc",
            "itemStyle": {"color": "#ADD8E6"},
            "label": {"show": True, "position": "inside"},
        },
        {
            "type": "bar",
            "name": "totalSSRA",
            "stack": "total",
            "itemStyle": {"color": "#FF8C00"},
            "label": {"show": True, "position": "inside"},
        },
        {
            "type": "bar",
            "name": "totalRT",
            "stack": "total",
            "itemStyle": {"color": "#FFD700"},
            "label": {"show": True, "position": "inside"},

        },
                {
            "type": "bar",
            "name": "total",
            "stack": "total",
            "itemStyle": {"color": "#FFD700"},
            "label": {"show": False, "position": "inside",},
            "markPoint": {
                "data": [
                    {"name": "Total", "coord": ["jun/23", 65 + 30], "value": 65 + 30},
                    {"name": "Total", "coord": ["jul/23", 12 + 87], "value": 12 + 87},
                ],
                "label": {"show": True, "position": "top", "formatter": "{c}",}
            }
        },
        {
            "type": "line",
            "name": "Diferença",
            "data": [
                {"value": ((10 + 23) - (65 + 30)) + 200, "label": {"show": True, "position": "top", "formatter": f"{((10 + 23) - (65 + 30))}"}},
                {"value": ((13 + 98) - (12 + 87)) + 200, "label": {"show": True, "position": "top", "formatter": f"{((13 + 98) - (12 + 87))}"}},
            ],
            "itemStyle": {"color": "red"},
        },
    ],
}

st_echarts(options=data, height="500px")
