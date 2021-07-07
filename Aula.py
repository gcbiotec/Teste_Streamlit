import streamlit as st
import pandas as pd

st.image('saude-bem-estar.jpg')

st.header('Machine Learning App!')

st.markdown('Entre com os dados do seu paciente!')

'''
Modelo Machine Learning:

- Idade
- Tempo de Internação
- Creatinina

'''

dados = pd.read_csv('df2_csv.csv' , sep=';')

st.write(dados)

var = st.sidebar.selectbox('Selecione uma variável', ['idade','dias_inter'])

'''
Média:
'''
media_idade = dados['idade'].groupby(dados[var]).mean()
st.write(media_idade)

#Aqui mostra como table:
st.table(media_idade)

#Para plotar:
plot = dados['dias_inter'].value_counts().plot(kind='barh')
st.pyplot(plot.figure) 

variaveis = dados.columns.tolist()
var1 = st.sidebar.selectbox('Selecione uma variável', variaveis)

plot = dados[var1].value_counts().plot(kind='barh')
st.pyplot(plot.figure) 
