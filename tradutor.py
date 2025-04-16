import pandas as pd
import streamlit as st
from googletrans import Translator

# Arquivo TXT
arquivo_txt = "dicionariobr.txt"

# Cria o Excel a partir do TXT
df = pd.read_csv(arquivo_txt, header=None, names=["Português"])
df["Finlandês"] = ""  # Traduções
df["Finlandês"] = df["Finlandês"].astype(str)
df.to_excel("dicionario.xlsx", index=False)  # Salva como Excel
print("Arquivo 'dicionario.xlsx' foi criado com sucesso!")

# Arquivo Excel
arquivo_excel = "dicionario.xlsx"

# Carrega o Excel
df = pd.read_excel(arquivo_excel)
df["Finlandês"] = df["Finlandês"].astype(str)

# Google tradutor
translator_google = Translator()

# Título do dashboard
st.title("Tradutor Português-Finlandês")

# Entrada da palavra
palavra = st.text_input("Digite uma palavra em Português:")

if palavra:
    if palavra in df["Português"].values:
        # Traduz a palavra
        traducao_google = translator_google.translate(palavra, src="pt", dest="fi").text
        # Atualiza o Excel
        df.loc[df["Português"] == palavra, "Finlandês"] = traducao_google
        df.to_excel(arquivo_excel, index=False)
        # Exibe a tradução
        st.write(f"A tradução de '{palavra}' para Finlandês é: **{traducao_google}**")
    else:
        st.write(f"A palavra '{palavra}' não foi encontrada no dicionário!")

# Histórico de traduções
st.subheader("Histórico de Traduções")
st.dataframe(df)


####PARA INICIAR O STREAMLIT:
    #abrir cmd 
    #cd (diretório)
    #streamlit run tradutor.py