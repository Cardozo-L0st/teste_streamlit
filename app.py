import streamlit as st
import random

st.set_page_config(page_title="Teste de página")
st.write("Minha primeira página com Streamlit!")
st.write("---")
st.title("Criando um gerador de números")
texto = "nenhum até agora"

#Campos de texto para pedir os valores
quantidade_numero = st.text_input("Quantidade de número", "")
do_numero = st.text_input("Do número", "")
ate_numero = st.text_input("Até o número", "")

#Gerando valores
def gerador_numeros():
    if do_numero > ate_numero:
        return st.write("O valor do campo 'Do número' precisa ser menor que o valor do campo 'Até o número'")
    else:
        numeros_sorteados = []
        i = 0
        while i != int(quantidade_numero):
            gerar = random.randint(int(do_numero), int(ate_numero))
            numeros_sorteados.append(gerar)
            i+=1
        return numeros_sorteados

#botões do jogo
if st.button("Sortear"):
    if do_numero == "" or ate_numero == "":
        st.write("Necessário digitar um valor nos campos: 'Do número' e 'Até o número'")
    else:
        texto = gerador_numeros()

def texto_final():
    st.write(f"Números sorteados: {texto}")

texto_final()