import pandas as pd
import numpy as np
import streamlit as st
#import plotly.express as px
import altair as pd

import pip
pip.main(["install", "openpyxl"])


mf0 = pd.read_excel('/content/drive/MyDrive/Base_desempenho/mediafinal.xlsx')
mf = mf0.query('NOTA <= 10')
disci = ['Automação Industrial']
disci2 = mf.query('DISCIPLINA == @disci')

alt.data_transformers.enable('default', max_rows=None)
grafico_final = alt.Chart(disci2).mark_circle(size=100).encode(
    alt.X('CODPERLET:O',scale=alt.Scale(zero=False) ,axis=alt.Axis( title='Periodo') ),
    alt.Y('NOTA',axis=alt.Axis(title='Nota', orient = "left") ),
    tooltip = ['NOME','RA'],
    #color=alt.Color('SIT_MATR',  legend=None )
    ).interactive().properties(width=800,height=400)
st.altair_chart(grafico_final, use_container_width=True)
