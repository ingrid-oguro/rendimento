import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

import pip
pip.main(["install", "openpyxl"])
PAGE_CONFIG = {"page_title": "CIA - Centro de Inteligência do Apoio ao aluno", "page_icon": ":globe_with_meridians:", "layout": "wide"}
st.set_page_config(**PAGE_CONFIG)

mf0 = pd.read_excel('mediafinal.xlsx')
mf = mf0.query('NOTA <= 10')
disci = ['Automação Industrial']
disci2 = mf.query('DISCIPLINA == @disci')

st.subheader('Rendimento na Disciplina')
disciplina = sorted(disci2.DISCIPLINA.unique())
disciplina_selecionada = st.selectbox('Disciplina',disciplina)
disci3 = disci2.query('DISCIPLINA == @disciplina_selecionada ')

alt.data_transformers.enable('default', max_rows=None)
grafico_final = alt.Chart(disci3).mark_circle(size=100).encode(
    alt.X('CODPERLET:O',scale=alt.Scale(zero=False) ,axis=alt.Axis( title='Periodo') ),
    alt.Y('NOTA',axis=alt.Axis(title='Nota', orient = "left") ),
    tooltip = ['NOME','RA'],
    #color=alt.Color('SIT_MATR',  legend=None )
    ).interactive().properties(width=800,height=400)
st.altair_chart(grafico_final, use_container_width=True)
