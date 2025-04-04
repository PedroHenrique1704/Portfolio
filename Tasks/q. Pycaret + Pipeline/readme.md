# Sistema de Credit Scoring Simples  

O **Credit Scoring** é um sistema que avalia o risco de um indivíduo inadimplir um crédito. Ele se baseia em variáveis financeiras e comportamentais para atribuir uma pontuação ao cliente. Quanto maior a pontuação, menor o risco de inadimplência.  

## ✅ Etapas do Sistema de Credit Scoring  

### 1️⃣ Coleta de Dados  
Os dados utilizados geralmente incluem:  
- Informações demográficas (idade, estado civil, etc.).  
- Histórico de crédito (atrasos, empréstimos em aberto).  
- Renda e estabilidade financeira.  

### 2️⃣ Amostragem  
A qualidade da amostragem influencia diretamente no modelo. Algumas técnicas comuns incluem:  

- **Balanceamento de classes**: Em problemas de inadimplência, a classe "inadimplente" costuma ser menor que a "adimplente", exigindo técnicas como *oversampling* (SMOTE) ou *undersampling*.  
- **Divisão Treino/Teste**: Normalmente, usamos 70% dos dados para treino e 30% para teste.  

### 3️⃣ Análises Exploratórias  
Antes de modelar, analisamos padrões nos dados:  
- **Distribuição das variáveis**: Detectamos outliers e padrões suspeitos.  
- **Correlação entre variáveis**: Identificamos quais variáveis são mais relevantes para a previsão.  
- **Análise de WoE e IV**: Avaliamos a influência de cada variável na inadimplência.  

## ✅ Modelagem e Avaliação  

### 🔹 Modelos Comuns  
- **Regressão Logística**: Simples e interpretável.  
- **Árvores de Decisão / Random Forest**: Capturam relações não lineares.  
- **XGBoost / LightGBM**: Modelos mais avançados e eficientes.  

### 🔹 Métricas de Avaliação  
- **AUC-ROC**: Mede a capacidade de separação do modelo.  
- **KS-Statistic**: Avalia a diferença entre as distribuições de adimplentes e inadimplentes.  
- **Matriz de Confusão e F1-Score**: Verificam o equilíbrio entre precisão e recall.  

## ✅ Importância do Credit Scoring  
Um bom sistema de credit scoring permite que instituições financeiras tomem decisões mais seguras, reduzam perdas por inadimplência e ofereçam crédito de forma justa e sustentável.  
