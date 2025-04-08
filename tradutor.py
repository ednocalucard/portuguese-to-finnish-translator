import pandas as pd
import streamlit as st
from googletrans import Translator

# Parte 1: Transformar TXT em Excel
# Nome do arquivo TXT
arquivo_txt = "dicionariobr.txt"

# Ler o TXT e criar o Excel
df = pd.read_csv(arquivo_txt, header=None, names=["Português"])
df["Finlandês"] = ""  # Coluna para as traduções
df["Finlandês"] = df["Finlandês"].astype(str)  # Força o tipo para string
df.to_excel("dicionario.xlsx", index=False)  # Cria o Excel
print("Arquivo 'dicionario.xlsx' foi criado com sucesso!")

# Nome do arquivo Excel gerado
arquivo_excel = "dicionario.xlsx"

# Parte 2: Fluxo Streamlit
df = pd.read_excel(arquivo_excel)  # Carrega o Excel
df["Finlandês"] = df["Finlandês"].astype(str)  # Garante que a coluna é string

# Inicializa o tradutor
translator = Translator()

# Interface do Streamlit
st.title("Tradutor Português-Finlandês")

# Entrada de palavra pelo usuário
palavra = st.text_input("Digite uma palavra em Português:")

if palavra:
    if palavra in df["Português"].values:
        # Traduz a palavra
        traducao = translator.translate(palavra, src="pt", dest="fi").text
        # Atualiza a coluna "Finlandês" na mesma linha
        df.loc[df["Português"] == palavra, "Finlandês"] = traducao
        # Salva o DataFrame atualizado no Excel
        df.to_excel(arquivo_excel, index=False)
        # Exibe o resultado ao usuário
        st.write(f"A tradução de '{palavra}' para Finlandês é: **{traducao}**")
    else:
        st.write(f"A palavra '{palavra}' não foi encontrada no dicionário!")

# Exibe o histórico completo de traduções
st.subheader("Histórico de Traduções")
st.dataframe(df)