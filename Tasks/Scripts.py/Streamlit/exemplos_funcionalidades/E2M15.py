import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO
import os
import random
from datetime import datetime

# 1 - Titulo + Icon
st.set_page_config(
    page_title="E2M15",
    page_icon=".\\icon\\ebac.jpg",  
    )

# Dicionário contendo os dataframes
dataframes = {
    'Janeiro': 'SINASC_RO_2019_JAN.csv',
    'Fevereiro': 'SINASC_RO_2019_FEV.csv',
    'Março': 'SINASC_RO_2019_MAR.csv',
    'Abril': 'SINASC_RO_2019_ABR.csv',
    'Maio': 'SINASC_RO_2019_MAI.csv',
    'Junho': 'SINASC_RO_2019_JUN.csv',
    'Julho': 'SINASC_RO_2019_JUL.csv',
    'Agosto': 'SINASC_RO_2019_AGO.csv',
    'Setembro': 'SINASC_RO_2019_SET.csv',
    'Outubro': 'SINASC_RO_2019_OUT.csv',
    'Novembro': 'SINASC_RO_2019_NOV.csv',
    'Dezembro': 'SINASC_RO_2019_DEZ.csv'
}

# 2 - Sidebar seletor de mês    
opcao = st.sidebar.selectbox('Escolha o mês:', list(dataframes.keys()))
DATE_COLUMN = 'dtnasc'

# 3 - Mostrar o dataframe
def load_data(mes):
    sinascmes = os.path.join('.\\input\\', dataframes[mes])
    df = pd.read_csv(sinascmes)
    df.columns = map(str.lower, df.columns)  # Renomear colunas para minúsculas
    df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN])
    return df

data = load_data(opcao)

# 4 - Filtro (DF)
st.sidebar.subheader('Filtros no dataframe')
filtro = st.sidebar.selectbox('Filtrar por Sexo:', ['Todos', 'Masculino', 'Feminino'])
if filtro != 'Todos':
    data = data[data['sexo'] == filtro]

# 5 - Botão para mostrar o dataframe
if st.checkbox('Mostrar dataframe'):
    st.subheader(f'Data - Sinasc RO {opcao} 2019')
    st.write(data)

# 6 - Botão para baixar o DataFrame
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
    label="Baixar DataFrame como CSV",
    data=csv,
    file_name=f'dataframe_sinasc_{opcao}.csv',
    mime='text/csv'
)

# 7 - Estatísticas Resumidas
st.subheader('Estatísticas Resumidas')
st.write(data.describe())


# 8 - Multi seleção de colunas
st.markdown('---')
columns = st.multiselect("Monte o dataframe com as colunas que preferir:", data.columns.tolist())
if columns:
    st.write(data[columns])


# 9 - Markdown
st.markdown('-------')

# 10 - Histograma
st.text('Gráfico: quantidade de bebês que nasceram na primeira semana do mês')
primeira_semana = data[data[DATE_COLUMN].dt.day <= 7]
hist_values = np.histogram(primeira_semana[DATE_COLUMN].dt.day, bins=7, range=(1, 8))[0]
st.bar_chart(hist_values)

# 11 - Histograma (Imagem)
st.markdown('----')
st.text('O mesmo gráfico, mas como imagem')
fig, ax = plt.subplots()
ax.bar(np.arange(1, 8), hist_values, width=0.7)
ax.set_xticks(np.arange(1, 8))
ax.set_xticklabels([f'Dia {i}' for i in range(1, 8)], rotation=45)
ax.set_ylabel('Número de Nascimentos')
ax.set_xlabel('Dias da Primeira Semana')
ax.set_title('Nascimentos na Primeira Semana do Mês')
st.pyplot(fig)

# 12 - Mapa com Slider
st.markdown('---')
st.text('Mapa com Slider')
dia_min, dia_max = st.slider('Selecione o intervalo de dias', min_value=1, max_value=31, value=(1, 7))
intervalo_dias = data[(data[DATE_COLUMN].dt.day >= dia_min) & (data[DATE_COLUMN].dt.day <= dia_max)]
hist_values, bins = np.histogram(intervalo_dias[DATE_COLUMN].dt.day, bins=dia_max - dia_min + 1, range=(dia_min, dia_max + 1))
fig, ax = plt.subplots()
ax.bar(bins[:-1], hist_values, width=0.7)
ax.set_xticks(bins[:-1])
ax.set_xticklabels([f'{int(day)}' for day in bins[:-1]], rotation=90)
ax.set_ylabel('Número de Nascimentos')
ax.set_xlabel('Dias do Mês')
ax.set_title(f'Nascimentos de {dia_min} a {dia_max} do Mês')
st.pyplot(fig)

st.markdown('---')
st.text('Gráfico de linhas:')
st.line_chart(data[DATE_COLUMN].dt.day.value_counts())

# 13 - Salvando o gráfico em um objeto BytesIO (em memória)
buf = BytesIO()
fig.savefig(buf, format="png")
buf.seek(0)  # Mover o ponteiro para o início do buffer

# 14 - Checkbox para Download
if st.checkbox('Liberar Download'):
    st.download_button(
        label="Baixar Gráfico",
        data=buf,
        file_name="grafico_nascimentos.png",
        mime="image/png"
    )

# 15 - Link
if st.checkbox('Ebac Webinar'):
    st.markdown("[Ebac Webinars](https://ebaconline.com.br/webinars)")

st.markdown('---')

# 16 - Musicas
musicas = ["Sparking Zero.mp3", "Big apple 3 AM.mp3"]
musica_selecionada = st.selectbox("Escolha uma música: (cuidado com o volume)", musicas)

# Exibir o player de áudio para a música selecionada
audio_file = f"ost/{musica_selecionada}"
st.audio(audio_file, format="audio/mp3")

st.markdown('---')

# 17 - Gerador de pequenas histórias
st.text("Gerador de pequenas histórias")
user_input = st.text_input("Digite um nome:", value = 'Pedro')
number = st.number_input("Insira um número: (0 a 100)", min_value=0, max_value=100)

# Lista de elementos para a narrativa
comeco_hist = [
    f"{user_input} estava caminhando pela floresta,",
    f"{user_input} encontrou um misterioso objeto brilhante,",
    f"{user_input} ouviu um barulho estranho vindo de trás de uma árvore,",
    f"{user_input} decidiu seguir um caminho desconhecido,",
    f"{user_input} viu um animal selvagem se aproximando,",
    f"A aventura de {user_input} começou quando ele/ela encontrou um mapa antigo,",
    f"{user_input} encontrou um grupo de viajantes,",
    f"{user_input} se deparou com um desafio inesperado,"
]

meio_hist = [
    "maçãs",
    "chaves de fenda",
    "almôndegas",
    "teclados",
    "roscas",
    "sofás",
]

fim_hist = [
    "para salvar o dia.",
    "para atravessar para o outro lado.",
    "para evitar algo pior.",
    "para chegar em casa."
]

# 18 - Gerar uma narrativa aleatória
if user_input:
    random_comeco = random.choice(comeco_hist)
    random_meio = random.choice(meio_hist)
    random_fim = random.choice(fim_hist)

    narrative = (
        f"A história de {user_input} com o número {number}: {random_comeco} "
        f"e no fim ele acabou precisando usar suas {number} {random_meio} "
        f"{random_fim}"
    )

    # Exibir a narrativa
    st.write(narrative)


# 19 - Horario
# 20 - Data

# Botão para atualizar a hora e a data

current_time = datetime.now()
formatted_date = current_time.strftime("%d/%m/%Y")  # Formato da data

# Exibir a data atual
st.sidebar.write(f"🗓️ Data atual: {formatted_date}")

# Exibir a hora atual
current_time_str = current_time.strftime("%H:%M:%S")
st.sidebar.write(f"🕒 Última vez atualizada: {current_time_str}")

# Botão para atualizar a hora embaixo da exibição da hora
if st.sidebar.button("Atualizar Hora"):
    current_time_str = datetime.now().strftime("%H:%M:%S")
    




