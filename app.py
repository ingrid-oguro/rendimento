import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

import pip
pip.main(["install", "openpyxl"])
PAGE_CONFIG = {"page_title": "CIA - Centro de Inteligência do Apoio ao aluno", "page_icon": ":globe_with_meridians:", "layout": "wide"}
st.set_page_config(**PAGE_CONFIG)

#GRÁFICO DISICPLINA
mf0 = pd.read_excel('mediafinal.xlsx')
mf = mf0.query('NOTA <= 10')

st.subheader('Rendimento na Disciplina')
disciplina = sorted(mf.DISCIPLINA.unique())
disciplina_selecionada = st.selectbox('Disciplina',disciplina)
disci2 = mf.query('DISCIPLINA == @disciplina_selecionada ')

alt.data_transformers.enable('default', max_rows=None)
grafico_final = alt.Chart(disci2).mark_circle(size=100).encode(
    alt.X('CODPERLET:O',scale=alt.Scale(zero=False) ,axis=alt.Axis( title='Periodo') ),
    alt.Y('NOTA',axis=alt.Axis(title='Nota', orient = "left") ),
    tooltip = ['NOME','RA'],
    #color=alt.Color('SIT_MATR',  legend=None )
    ).interactive().properties(width=800,height=400)
st.altair_chart(grafico_final, use_container_width=True)

#GRÁFICO CURSO
mg = pd.read_excel('mediageral.xlsx')

#curso = ['Engenharia de Produção']
#epr = mg.query('COMPLEMENTO == @curso ')

st.subheader('Rendimento na Graduação')
curso = sorted(mg.COMPLEMENTO.unique())
curso_selecionado = st.selectbox('Curso',curso)
curso2 = mf.query('COMPLEMENTO == @curso_selecionado ')

curso3 = curso2[curso2['NOTA'].notna()]

grafico_geral = alt.Chart(curso3).mark_circle(size=100).encode(
alt.X('CODPERLET:O',scale=alt.Scale(zero=False) ,axis=alt.Axis( title='Periodo') ),
alt.Y('NOTA',axis=alt.Axis(title='Nota', orient = "left") ),
tooltip = ['NOME','RA'],
#color=alt.Color('SIT_MATR',  legend=None )
 ).interactive().properties(width=800,height=400)
st.altair_chart(grafico_geral, use_container_width=True)
