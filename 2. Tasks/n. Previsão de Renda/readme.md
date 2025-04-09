# Previsão de Renda  

A previsão de renda é um problema de regressão onde buscamos estimar a renda de um indivíduo com base em variáveis preditoras, como idade, escolaridade e ocupação. Para melhorar a qualidade do modelo, utilizamos técnicas como **linearização** e análise de **resíduos vs. valores preditos**.  

## ✅ Linearização  

Muitos modelos assumem uma relação linear entre as variáveis, mas nem sempre isso ocorre. Para contornar esse problema, aplicamos transformações matemáticas, como:  

- **Logaritmo**: Para reduzir efeitos de assimetria em distribuições de renda.  
- **Raiz quadrada ou exponencial**: Para ajustar relações não lineares.  

Após a transformação, o modelo pode capturar melhor os padrões nos dados.  

## ✅ Resíduos vs. Valores Preditos  

A análise de resíduos é fundamental para verificar a adequação do modelo. O ideal é que os resíduos (diferença entre valores reais e preditos) estejam distribuídos aleatoriamente em torno de zero, sem padrões visíveis.  

### O que analisar?  
- **Distribuição aleatória** → O modelo é adequado.  
- **Padrões nos resíduos** → Indica não linearidade ou omissão de variáveis importantes.  
- **Heterocedasticidade** (dispersão crescente dos resíduos) → Pode indicar necessidade de transformação na variável resposta.  

Essas técnicas ajudam a melhorar a precisão da previsão e garantem que o modelo esteja capturando corretamente os padrões da renda.  
