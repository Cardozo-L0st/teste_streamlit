import streamlit as st
import random

st.set_page_config(page_title="Teste de página")
st.write("Minha primeira página com Streamlit!")
st.write("---")
st.title("Criando um gerador de números aleatórios")
st.write("Será gerado um número de 1 até o valor digitiado pelo usuário")

st.header("Digite um número")
campo_texto = st.text_input("")

st.write(f"O número digititado foi {campo_texto}")

def gerarNumeroAleatorio():
    x = random.randint(1, int(campo_texto))
    return x

st.header("Botão")
if st.button("clique aqui"):
    st.write(f"Número gerado foi {gerarNumeroAleatorio()}")