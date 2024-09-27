import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

sns.set()  

def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).unstack().plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return None

# Função para carregar os dados de um único mês
def carregar_dados_mes(mes):
    arquivo = f'./input/SINASC_RO_2019_{mes}.csv'
    if os.path.exists(arquivo):
        print(f"Carregando dados do mês {mes}...")
        return pd.read_csv(arquivo)
    else:
        print(f"Aviso: Arquivo {arquivo} não encontrado.")
        return None

# Captura os argumentos da linha de comando
meses = sys.argv[1:]  # Exemplo: ['JAN', 'FEV', 'MAR']
if not meses:
    print("Erro: Nenhum mês especificado. Informe pelo menos um mês (ex: JAN FEV MAR).")
    sys.exit(1)

# Processa os dados de cada mês separadamente
for mes in meses:
    sinasc = carregar_dados_mes(mes)

    if sinasc is not None:
        # Captura a maior data de nascimento no formato YYYY-MM
        max_data = sinasc['DTNASC'].max()[:7]
        print(f"Maior data de nascimento para {mes}: {max_data}")

        # Cria a pasta de saída para o mês específico
        os.makedirs(f'./output/figs/{mes}', exist_ok=True)

        # Gera os gráficos e salva na pasta correspondente ao mês
        plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'Média idade mãe por data', 'Data nascimento')
        plt.savefig(f'./output/figs/{mes}/media_idade_mae_por_data.png')
        plt.close()  # Fecha o gráfico para evitar sobreposição

        plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'Média idade mãe', 'Data de nascimento', 'unstack')
        plt.savefig(f'./output/figs/{mes}/media_idade_mae_por_sexo.png')
        plt.close()

        plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'Média peso bebê', 'Data de nascimento', 'unstack')
        plt.savefig(f'./output/figs/{mes}/media_peso_bebe_por_sexo.png')
        plt.close()

        plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'Peso mediano', 'Escolaridade mãe', 'sort')
        plt.savefig(f'./output/figs/{mes}/peso_mediano_por_escolaridade_mae.png')
        plt.close()

        plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'Apgar1 médio', 'Gestação', 'sort')
        plt.savefig(f'./output/figs/{mes}/media_apgar1_por_gestacao.png')
        plt.close()

