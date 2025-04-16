import pandas as pd
import streamlit as st
from googletrans import Translator
from translate import Translator as TranslatePython

### Parte 1: Transformar TXT em Excel
# arquivo TXT
arquivo_txt = "dicionariobr.txt"

## Ler o TXT e criar o Excel
df = pd.read_csv(arquivo_txt, header=None, names=["Português"])
df["Finlandês (Google)"] = ""  # Coluna para as traduções do Google
df["Finlandês (Translate-python)"] = ""  # Coluna para a biblioteca alternativa
df["Finlandês (Google)"] = df["Finlandês (Google)"].astype(str)  # Força o tipo para string
df["Finlandês (Translate-python)"] = df["Finlandês (Translate-python)"].astype(str)
df.to_excel("dicionario.xlsx", index=False)  # Cria o Excel
print("Arquivo 'dicionario.xlsx' foi criado com sucesso!")

## Excel gerado
arquivo_excel = "dicionario.xlsx"

## Streamlit
df = pd.read_excel(arquivo_excel)  # Carrega o Excel
df["Finlandês (Google)"] = df["Finlandês (Google)"].astype(str)  # Garante que as colunas são strings
df["Finlandês (Translate-python)"] = df["Finlandês (Translate-python)"].astype(str)

#Tradutores
translator_google = Translator()
translator_alternativo = TranslatePython(from_lang="portuguese", to_lang="finnish")

# Interface do Streamlit
st.title("Tradutor Português-Finlandês")

## Opção para selecionar a ferramenta de tradução (googletrans ou pythontrans)
opcao_tradutor = st.radio(
    "Escolha a ferramenta de tradução:",
    ("Google Translator", "Biblioteca Translate-python")
)

# Word input
palavra = st.text_input("Digite uma palavra em Português:")

if palavra:
    if palavra in df["Português"].values:
        if opcao_tradutor == "Google Translator":
            # Tradução com Google Translator
            traducao_google = translator_google.translate(palavra, src="pt", dest="fi").text
            df.loc[df["Português"] == palavra, "Finlandês (Google)"] = traducao_google
            st.write(f"**Tradução (Google Translator):** {traducao_google}")
        elif opcao_tradutor == "Biblioteca Translate-python":
            # Tradução com biblioteca translate-python
            traducao_alternativa = translator_alternativo.translate(palavra)
            df.loc[df["Português"] == palavra, "Finlandês (Translate-python)"] = traducao_alternativa
            st.write(f"**Tradução (Biblioteca Translate-python):** {traducao_alternativa}")

        # Salva o DataFrame atualizado no Excel
        df.to_excel(arquivo_excel, index=False)
    else:
        st.write(f"A palavra '{palavra}' não foi encontrada no dicionário!")

##### Exibir o histórico completo de traduções
st.subheader("Histórico de Traduções")
st.dataframe(df)