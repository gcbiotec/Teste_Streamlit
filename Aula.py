import streamlit as st
import pandas as pd
import pickle


st.image('saude-bem-estar.jpg')

st.header('Calule seu risco cardíaco!')

st.markdown('Entre com os seus dados para verificar seu risco:')

# '''
# Os dados utilizados serão:
#
# - Idade
# - Tempo de Internação
# - Fumante
# - Colesterol
#
# '''

col1, col2 = st.beta_columns(2)

x1 = col1.slider('Pressão Arterial Sistólica', 50, 150, 70, 1, help = 'Essa é pressão sistólica mais alta')
x6 = col1.slider('Pressão Arterial Diastólica', 50, 150, 50, 1, help = 'Essa é pressão diastólica mais alta')
x2 = col1.slider('Glicose', 50, 250, 70, 2, help = 'Qual sua glicose em mg/dL?')
x3 = col1.slider('Idade',10, 105, 30, 1, help = 'Qual a sua idade')
x4 = col1.slider('Colesterol Total', 50, 250, 80, 10, help = 'Qual é a medida do seu colesterol?')
x5 = col1.slider('Número de cigarros por dia', 0, 65, 0, 1, help = 'Quantos cigarros por dia?')

x7 = col2.radio('Hipertensão: 1 = Sim / 0 = Não', ['1','0'])
x8 = col2.radio('Diabetes: 1 = Sim / 0 = Não', ['1','0'])
x9 = col2.radio('Toma medicação para pressão: 1 = Sim / 0 = Não', ['1','0'])
# x10 = col2.radio('Sexo: 1 = Masc / 0 = Fem', ['1','0'])

st.markdown('---')

dicionario = {'sysBP': [x1],
              'glucose': [x2],
              'age': [x3],
              'totChol': [x4],
              'cigsPerDay': [x5],
              'diaBP': [x6],
              'prevalentHyp': [x7],
              'diabetes': [x8],
              'BPMeds': [x9],
              # 'male': [x10],
              }

dados = pd.DataFrame(dicionario)

st.write(dados)

st.markdown('---')

with open('modelo_regress_Log.pkl', 'rb') as f:
    modelo = pickle.load(f)

#	saida = predict_model(modelo, dados)

if st.button('EXECUTAR O MODELO'):
    saida = modelo.predict(dados)
	#classificacao = int(saida['TenYearCHD'])

if saida == 0:
    st.markdown('Você não tem previsão de doença, continue se cuidando!')
else:
    st.markdown('Você tem chance de desenvolver doença cardíaca! Mude sua rotina')


# my_range = range(1,250)
# number = st.select_slider("Escolha o valor", options = my_range, value = 5)


# dados = pd.read_csv('df2_csv.csv' , sep=';')

# st.write(dados)

# var = st.sidebar.selectbox('Selecione uma variável', ['idade','dias_inter'])

# '''
# Média:
# '''
# media_idade = dados['idade'].groupby(dados[var]).mean()
# st.write(media_idade)
#
# #Aqui mostra como table:
# st.table(media_idade)
#
# #Para plotar:
# plot = dados['dias_inter'].value_counts().plot(kind='barh')
# st.pyplot(plot.figure)
#
# variaveis = dados.columns.tolist()
# var1 = st.sidebar.selectbox('Selecione uma variável', variaveis)
#
# plot = dados[var1].value_counts().plot(kind='barh')
# st.pyplot(plot.figure)
