# Relação Inadimplencia e Escolaridade

Utilizando do *dataframe* com variaveis abaixo e com 10127 linhas. Sera analisado a relação entre *clientes inadimplentes* e sua *escolaridade*.

| Variável                | Descrição                                                             | Tipo    |
|-------------------------|-----------------------------------------------------------------------|---------|
| id                      | Número de identificação                                               | int64   |
| default                 | Inadimplência (True = inadimplente)                                   | int64   |
| idade                   | Idade do cliente                                                      | int64   |
| sexo                    | Gênero do cliente                                                     | object  |
| dependentes             | Quantidade de dependentes do cliente                                  | int64   |
| escolaridade            | Grau de escolaridade                                                  | object  |
| estado_civil            | Estado civil do cliente                                               | object  |
| salario_anual           | Salário anual do cliente, dividido em categorias e em dólar            | object  |
| tipo_cartao             | Categoria do cartão do cliente, dividido em categorias                | object  |
| meses_de_relacionamento | Tempo em que o cliente utiliza os serviços                            | int64   |
| qtd_produtos            | Quantidade de produtos adquiridos pelo cliente                        | int64   |
| iteracoes_12m           | Quantidade de interações do cliente com o banco nos últimos 12 meses  | int64   |
| meses_inativo_12m       | Quantidade de meses que o cliente não efetuou uma ação no banco nos últimos 12 meses | int64   |
| limite_credito          | Limite de crédito do cliente                                          | object  |
| valor_transacoes_12m    | Valor total de todas as transações realizadas nos últimos 12 meses    | object  |
| qtd_transacoes_12m      | Quantidade de transações realizadas pelo cliente nos últimos 12 meses | int64   |

