# Credit Score Prediction - Machine Learning Project

## Descrição do Projeto
Projeto focado na implementação de um sistema de machine learning para análise de crédito, utilizando programação estruturada com:

- **Classes especializadas** para pré-processamento de dados  
- **Funções modulares** para geração de gráficos e métricas  
- **Pipeline completo** de tratamento de dados e modelagem  


## ⚙️ Instalação
1. Instale as dependências:
```bash
pip install -r requirements.txt
```


## Visão Geral
Sistema de machine learning para identificação de potenciais maus pagadores (credit scoring) baseado em dados históricos de clientes. O projeto foca na construção de uma solução robusta com:

- **Arquitetura modular** utilizando classes e funções especializadas
- Pipeline completo de processamento de dados e visualizações
- Implementação com CatBoost para máxima eficiência

### Justificativa para uso do CatBoost
| Vantagem | Descrição |
|----------|-----------|
| **Nativo com dados categóricos** | Processa colunas categóricas sem pré-processamento |
| **Alto desempenho** | Algoritmo gradient boosting otimizado para velocidade |
| **Resistente a overfitting** | Mecanismos internos de regularização |
| **Interpretabilidade** | Gera importância de features automaticamente |
| **Suporte a texto** | Processamento integrado de features textuais |

### Dataset Structure
Dados obtidos do [Kaggle](https://www.kaggle.com/datasets/parisrohan/credit-score-classification) contendo:

#### Tabela de Features
| Nome da Coluna | Descrição/Função |
|----------------|------------------|
| ID | Identificador único do registro |
| Customer_ID | Identificador único do cliente |
| Month | Mês de referência dos dados |
| Name | Nome do cliente |
| Age | Idade do cliente |
| SSN | Número do seguro social |
| Occupation | Profissão do cliente |
| Annual_Income | Renda anual |
| Monthly_Inhand_Salary | Salário líquido mensal |
| Num_Bank_Accounts | Número de contas bancárias |
| Num_Credit_Card | Número de cartões de crédito |
| Interest_Rate | Taxa de juros média |
| Num_of_Loan | Número de empréstimos ativos |
| Type_of_Loan | Tipos de empréstimos contratados |
| Delay_from_due_date | Dias de atraso em pagamentos |
| Num_of_Delayed_Payment | Número de pagamentos atrasados |
| Changed_Credit_Limit | Variação no limite de crédito |
| Num_Credit_Inquiries | Consultas recentes ao crédito |
| Credit_Mix | Mix de produtos de crédito |
| Outstanding_Debt | Dívida total pendente |
| Credit_Utilization_Ratio | Utilização do limite de crédito |
| Credit_History_Age | Tempo de histórico creditício |
| Payment_of_Min_Amount | Paga apenas valor mínimo? |
| Total_EMI_per_month | Parcelamentos mensais totais |
| Amount_invested_monthly | Valor mensal investido |
| Payment_Behaviour | Padrão de comportamento de pagamento |
| Monthly_Balance | Saldo mensal disponível |
| Credit_Score | Target: Good/Standard/Poor |

### Abordagem Técnica
1. **Pré-processamento inteligente** com tratamento de:
   - Valores faltantes
   - Dados categóricos/textuais
   - Normalização de features numéricas <br><br>

2. **Engenharia de features** para criar indicadores adicionais 

3. **Modelagem com CatBoost** utilizando:
   - Validação cruzada
   - Early stopping
   - Otimização de hiperparâmetros <br><br>

4. **Análise de resultados** com:
   - Métricas de classificação multiclasse
   - Matriz de confusão
   - Curvas de aprendizado
