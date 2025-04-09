# O que é Bagging?  

Bagging (*Bootstrap Aggregating*) é uma técnica de aprendizado de máquina usada para melhorar a estabilidade e a precisão de modelos preditivos, reduzindo a variância e evitando o overfitting.  

## Como funciona?  

1. São geradas várias amostras aleatórias do conjunto de dados original, com reposição (*bootstrap*).  
2. Um modelo é treinado para cada amostra de forma independente.  
3. As previsões dos modelos são combinadas para obter um resultado final mais robusto.  
   - Para problemas de **classificação**, geralmente é usada a média das previsões ou votação majoritária.  
   - Para problemas de **regressão**, a média das previsões numéricas é utilizada.  

## Aplicações  

Bagging é amplamente utilizado em algoritmos como o **Random Forest**, que combina múltiplas árvores de decisão para criar um modelo mais preciso e generalizável.  

Essa técnica é eficaz quando modelos individuais têm alta variância e se beneficiam da combinação de
