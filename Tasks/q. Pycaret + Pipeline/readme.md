
# 🧠 Credit Scoring com PyCaret e Streamlit

Este projeto tem como objetivo realizar uma análise e modelagem de um problema de classificação binária utilizando um modelo de Credit Scoring. A ideia é prever se um cliente será inadimplente ou não, com base em variáveis socioeconômicas e comportamentais.

---

## 📚 Etapas Realizadas

### 🔍 1. Exploração dos Dados
- Leitura dos dados
- Análise exploratória e tratamento de dados faltantes
- Criação de novas variáveis
- Análise de correlação e distribuição das variáveis

### 🛠️ 2. Preparação dos Dados
- Transformação de variáveis categóricas
- Detecção e tratamento de outliers
- Normalização de variáveis numéricas
- Balanceamento da base (opcional)

### 🤖 3. Modelagem com PyCaret
- Setup da base com definições das variáveis alvo, exclusão, etc.
- Comparação automática entre diversos algoritmos
- Ajuste fino (tuning) do melhor modelo
- Interpretação do modelo com gráficos (Feature Importance, ROC, PR Curve etc.)
- Avaliação dos resultados com matriz de confusão, curva ROC, métricas, etc.

---

## 📈 Aplicativo Streamlit – Avaliação de Modelo de Credit Scoring

O projeto também inclui uma interface interativa desenvolvida com **Streamlit**, onde é possível carregar dados e realizar todo o processo de avaliação de um modelo de credit scoring utilizando o PyCaret. A interface foi construída com foco em usabilidade e visualização dos resultados.

### 🚀 Funcionalidades do App

- Upload de arquivos `.ftr` ou `.pkl`
- Opção de utilizar uma amostra (20%) dos dados
- Ajuste do limite para categorias raras
- Ajuste do tamanho do treino e do limite de outliers
- Pipeline completo com:
  - Curva ROC
  - Matriz de confusão
  - Curva Precision-Recall
  - Relatório de Classificação
  - Importância das variáveis
  - Análise de limiar
  - Curva de calibração
  - Erro de predição
- Download do modelo treinado (`modelo_credit_scoring.pkl`)
- Interface com design customizado via CSS
- Ícones com links diretos para GitHub e LinkedIn do autor

### 🧠 Modelo Utilizado

O modelo treinado automaticamente pela aplicação é o **LightGBM**, que também é tunado (ajuste de hiperparâmetros) automaticamente antes da avaliação.

### 🖼️ Capturas de Tela

* Iniciando o **Streamlit**

[streamlit1.webm](https://github.com/user-attachments/assets/3a974115-bc29-42b7-bb56-8d4a46236438)


* Resultado do **Streamlit**

[streamlit2.webm](https://github.com/user-attachments/assets/ed25484a-1cfe-4b3b-85fe-b774c8af53c1)


### ▶️ Como Executar

1. Clone o repositório:
  
2. Instale os requisitos:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o aplicativo:
   ```bash
   streamlit run app.py
   ```

### 🗂️ Estrutura da Aplicação

```
projeto-credit-scoring/
│
├── Pycaret.ipynb               # Jupyter Notebook
├── app.py                      # Aplicativo Streamlit principal
├── css/
│   └── estilo.css              # Estilo customizado
├── img/
│   ├── pag_icon.png            # Ícone da aba
│   ├── icon.png                # Ícone da sidebar
│   ├── git.png                 # Ícone GitHub
│   ├── in.png                  # Ícone LinkedIn
├── imgs/
│   ├── home.png
│   ├── avaliacao.png
│   └── comparacao.png
├── README.md
└── requirements.txt
```

---

### 📬 Contato

Entre em contato para dúvidas ou sugestões:

- GitHub: [PedroHenrique1704](https://github.com/PedroHenrique1704)
- LinkedIn: [phcf](https://www.linkedin.com/in/phcf/)
