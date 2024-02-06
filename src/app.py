import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Validador de schema excel"
)

#Title
st.title("Insira o seu excel para validação")

st.markdown('**Hello World!** 🌍')

st.write('Esta é uma demonstração de algumas funcionalidades do streamlit')

input_text = st.text_input("Digite algo aqui:")

st.write(f"Você digitou: {input_text}")

# Slider para números
numero = st.slider('Escolha um número', 0, 100, 50)

# Exibir o número escolhido
st.write(f'Você escolheu o número: {numero}')

#Gráfico barras simples
dados = pd.DataFrame({
    'coluna': ['A', 'B', 'C', 'D', 'E'],
    'valores': np.random.randn(5)
})

