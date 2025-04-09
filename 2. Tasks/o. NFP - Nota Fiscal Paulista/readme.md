# Nota Fiscal Paulista (NFP) e Análise com WoE e IV  

## ✅ O que é a Nota Fiscal Paulista?  

A **Nota Fiscal Paulista (NFP)** é um programa do Governo do Estado de São Paulo que incentiva os consumidores a exigirem a nota fiscal nas compras. O objetivo é reduzir a sonegação fiscal e permitir que parte do ICMS recolhido seja devolvida ao consumidor cadastrado.  

### 🔹 Como funciona?  
1. O consumidor informa seu CPF ao realizar uma compra.  
2. Uma porcentagem do imposto pago retorna como crédito, podendo ser utilizado para abatimento do IPVA ou resgate em conta bancária.  
3. Além disso, há sorteios periódicos com prêmios em dinheiro.  

## ✅ Uso de WoE e IV na Análise  

Ao analisar dados da **Nota Fiscal Paulista**, utilizamos **WoE (Weight of Evidence)** e **IV (Information Value)** para entender padrões e a importância das variáveis.  

### 🔹 O que é WoE?  
**Weight of Evidence (WoE)** mede a separação entre grupos (como consumidores que resgatam créditos e os que não resgatam) com base em uma variável.  

Fórmula:  

**WoE = ln ( % de bons / % de maus )**

- Valores positivos indicam maior concentração de "bons" (exemplo: consumidores ativos no programa).  
- Valores negativos indicam maior presença de "ruins" (exemplo: consumidores que raramente utilizam os benefícios).  

### 🔹 O que é IV?  
**Information Value (IV)** avalia a capacidade preditiva de uma variável.  

**IV = Σ ( % de bons - % de ruins ) × WoE**

- **IV < 0.02** → Variável irrelevante.  
- **0.02 ≤ IV < 0.1** → Fraca influência.  
- **0.1 ≤ IV < 0.3** → Média influência.  
- **IV ≥ 0.3** → Forte influência.  

### ✅ WoE sobre o Tempo  

Ao aplicar **WoE sobre o tempo**, podemos identificar padrões sazonais, como:  
- Se consumidores utilizam mais a NFP em determinados meses.  
- Se há períodos em que mais pessoas resgatam créditos.  
- Se o tempo desde o último resgate influencia no comportamento futuro.  

Essas análises ajudam a prever quais consumidores têm maior probabilidade de continuar participando do programa e permitem estratégias para engajar aqueles que não resgatam seus créditos com frequência.  
