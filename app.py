import streamlit as st
import random

st.set_page_config(page_title="Teste de página")
st.write("Minha primeira página com Streamlit!")
st.write("---")
st.title("Criando um gerador de números")

#Campos de texto para pedir os valores
quantidade_numero = st.text_input("Quantidade de número", "")
do_numero = st.text_input("Do número", "")
ate_numero = st.text_input("Até o número", "")

#Gerando valores
def gerador_numeros():
    gerar = random.randint(int(do_numero), int(ate_numero))
    return gerar

#botões do jogo
if st.button("Sortear"):
    st.write(gerador_numeros())

def texto_final():
    st.write("Números sorteados: nenhum até agora")

texto_final()