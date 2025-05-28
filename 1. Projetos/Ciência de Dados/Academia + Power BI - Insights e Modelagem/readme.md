# Análise de Frequência em Academia - Power BI Dashboard (Projeto Acadêmico)

* Acesse o [Dashboard](https://app.powerbi.com/groups/me/reports/8ef11eb9-6638-469a-a10d-ac4890ebcf2e/40e7cacb3ce70ec76173?experience=power-bi)

## Disclaimer
**Este é um projeto acadêmico desenvolvido para fins educacionais.**  
* **Nenhum dado real foi utilizado** - Todos os conjuntos de dados são fictícios  
* **A empresa analisada não existe** - Criada apenas para simulação acadêmica  
* **As conclusões não representam situações reais** - Análises puramente demonstrativas

## Visão Geral
Este projeto tem como objetivo transformar dados brutos de check-ins em uma 
academia em insights acionáveis por meio de um dashboard interativo no Power BI. 
O relatório é projetado para ser atualizado semanalmente, auxiliando a gestão na 
identificação de padrões de frequência, otimização de horários de aulas e melhoria na 
experiência dos clientes.

## Colunas do dataset *(já tratadas)*

| Variável               | Tipo     | O que ela faz              | - | Variável                  | Tipo     | O que ela faz              |
|------------------------|----------|----------------------------|---|---------------------------|----------|----------------------------|
| gender                 | object   | Gênero do cliente          | - | birthday                  | object   | Data de nascimento         |
| Age                    | int64    | Idade calculada do cliente| - | abonoment_type            | int64    | Tipo de plano              |
| monthly_fee            | int32    | Valor mensal do plano     | - | commitment                | int32    | Grau de comprometimento    |
| visit_per_week         | int64    | Visitas por semana        | - | Mon                       | bool     | Vai à academia na segunda  |
| Tue                    | bool     | Vai à academia na terça   | - | Wed                       | bool     | Vai à academia na quarta   |
| Thu                    | bool     | Vai à academia na quinta  | - | Fri                       | bool     | Vai à academia na sexta    |
| Sat                    | bool     | Vai à academia no sábado  | - | Sun                       | bool     | Vai à academia no domingo  |
| avg_time_check_in      | object   | Horário médio de entrada  | - | avg_time_check_out        | object   | Horário médio de saída     |
| avg_time_in_gym        | int64    | Tempo médio na academia   | - | attend_group_lesson       | bool     | Participa de aulas em grupo|
| Kickboxen              | bool     | Frequenta aula de kickboxing | - | BodyPump                 | bool     | Frequenta aula de BodyPump |
| XCore                  | bool     | Frequenta aula de XCore   | - | Yoga                      | bool     | Frequenta aula de Yoga     |
| Running                | bool     | Frequenta corrida          | - | Pilates                   | bool     | Frequenta aula de Pilates  |
| LesMiles               | bool     | Frequenta aula de LesMiles| - | HIT                       | bool     | Frequenta aula de HIT      |
| Zumba                  | bool     | Frequenta aula de Zumba   | - | BodyBalance               | bool     | Frequenta aula de BodyBalance |
| Spinning               | bool     | Frequenta aula de Spinning| - | no_group_lesson           | bool     | Não participa de aulas em grupo |
| lemon                  | bool     | Prefere sabor limão       | - | berry_boost               | bool     | Prefere sabor frutas vermelhas |
| black_currant          | bool     | Prefere sabor cassis      | - | orange                    | bool     | Prefere sabor laranja      |
| coconut_pineapple      | bool     | Prefere sabor coco/abacaxi| - | passion_fruit             | bool     | Prefere sabor maracujá     |
| no_fav_drink           | bool     | Não tem bebida favorita   | - | drink_abo                 | bool     | Tem assinatura de bebidas  |
| personal_training      | bool     | Usa personal trainer       | - | name_personal_trainer     | object   | Nome do personal trainer   |
| uses_sauna             | bool     | Usa a sauna               | - | //                        | //       | //                         |




## Passos do Projeto

### Coleta de Dados

Download do dataset original no [Kaggle](https://www.kaggle.com/datasets/ka66ledata/gym-membership-dataset).

### Tratamento no Python (Jupyter Notebook)

* Limpeza de dados ausentes.

* Criação de colunas `Booleanas` para:
  * Dias da semana
  * Bebidas favoritas

* Insights iniciais

### Desenvolvimento no Power BI

* Transformação de colunas (Unpivot para dias da semana e aulas).

* Criação de faixas etárias e horárias.

* Criação de métricas e visualizações interativas.

* Implementação de filtros dinâmicos (gênero, faixa etária, horários).

* Design do dashboard para atualização semanal.

### Insights Principais

Horários de pico de movimento.

Aulas mais e menos frequentadas.

Comparativo entre planos (*Premium vs. Standard*).

Distribuição de clientes por idade e gênero.


## **Ferramentas Utilizadas:**
   - Power BI Desktop
   - Python (Jupyter Notebook)
   - Git para controle de versão

---

* Data de Conclusão: Maio/2025  
* Linkedin: [Pedro Henrique](https://www.linkedin.com/in/phcf/)

> *Your mind is the strongest and most valuable muscle you can grow in the gym*
