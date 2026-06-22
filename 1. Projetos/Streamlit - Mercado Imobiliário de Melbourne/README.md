# Análise e Previsão do Mercado Imobiliário de Melbourne + Georreferencia

**Autor**: [Pedro Henrique](https://www.linkedin.com/in/phcf)  
**Última atualização**: 26/03/2025  

##  Visão Geral do Projeto

Análise completa do mercado imobiliário residencial de Melbourne (2016-2018) contendo:

-  **Análise exploratória** geoespacial
-  **Modelos preditivos** com machine learning
-  **Dashboard interativo** via Streamlit
-  **Métricas de performance** (R² > 0.90)

## Como Acessar

###  Versão Online (Hospedada)
Aplicação disponível em:  

* Versão completa (recomendado caso vá baixar e utilizar em sua máquina)
  
 [Streamlit Completo](https://ebac-semantix.onrender.com/)  
  <br>
* Versão Pocket (30% dos dados sortidos aleatóriamente) (mais rápido, menos confiavel)
  
 [Streamlit Pocket](https://ebac-semantix-1.onrender.com/)

*Observações técnicas*:
- Tempo de carregamento inicial: 30-60 segundos
- Performance limitada pelo plano gratuito

###  Execução Local (Recomendado)
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/ebac-semantix.git

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run streamlit_app.py
```

## Base de Dados

| Característica | Detalhes                              |
|-----------------|----------------------------------------|
| Fonte          | Melbourne Housing Market              |
| Período        | Jan/2016 - Dez/2018                   |
| Amostra        | 34.857 transações válidas             |
| Variáveis      | 21 atributos incluindo preço, localização e características físicas |


##  Objetivos

### 1. Análise Exploratória
Mapeamento de heatmaps de preços por região

Identificação de outliers e correlações

Análise temporal de valorização

### 2. Modelagem Preditiva

```python
Copy
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=200)
# Código simplificado do modelo
```


## Stack Tecnológica

* **Linguagem**: Python 3.9+

* **Processamento**: Pandas, NumPy

* **ML**: Scikit-learn, XGBoost

* **Visualização**: Plotly, Matplotlib

* **Web**: Streamlit

* **Georreferencia**:  Folium

##  Contexto Educacional

Desenvolvido como projeto do curso **Profissão: Cientista de Dados** da <span style="color: cadetblue;">**EBAC**</span>  em parceria com a <span style="color: Darkorchid;">**Semantix**</span>.

![icon](https://github.com/user-attachments/assets/61cfac38-b979-4986-b898-cd0325954c1e)


## Contato
Para colaborações ou dúvidas:

Email: pedrohcf.1704@gmail.com

LinkedIn: [in/phcf](https://www.linkedin.com/in/phcf)

GitHub: [@PedroHenrique1704](https://github.com/PedroHenrique1704)


## Imagens da Aplicação
![foto 1](https://github.com/user-attachments/assets/1dea7f66-5a3a-4aca-9aee-97223e0b7af9)
![foto 2](https://github.com/user-attachments/assets/83922c03-43e9-4653-95ce-a48ff7364553)


> *"An investment in knowledge pays the best interest."* — Benjamin Franklin

