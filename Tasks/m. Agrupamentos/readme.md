# Agrupamentos: Hierárquicos e Parciais  

A análise de agrupamento (*clustering*) é uma técnica de aprendizado não supervisionado usada para segmentar dados em grupos com características semelhantes. Entre os principais métodos, destacam-se os **agrupamentos hierárquicos** e os **agrupamentos parciais**.  

## ✅ Agrupamento Hierárquico  

O agrupamento hierárquico cria uma estrutura em forma de árvore (*dendrograma*), onde os dados são agrupados de forma iterativa, seguindo uma abordagem bottom-up (*aglomerativo*) ou top-down (*divisivo*).  

### 🔹 Como funciona?  
1. Cada ponto começa como um cluster separado.  
2. Os clusters mais próximos são mesclados com base em uma métrica de similaridade.  
3. Esse processo continua até que todos os pontos pertençam a um único cluster ou até atingir um critério pré-definido.  

### ✅ Uso do Dendrograma  
O **dendrograma** é uma representação visual do agrupamento hierárquico, mostrando a relação entre os dados e ajudando a determinar o número ideal de clusters ao observar onde os ramos devem ser cortados.  

## ✅ Agrupamento Particional (K-Means)  

Diferente do hierárquico, o **K-Means** é um método de agrupamento baseado em partições, onde os dados são divididos em **K grupos pré-definidos**.  

### 🔹 Como funciona?  
1. Definem-se **K centros** iniciais (centroides).  
2. Cada ponto é atribuído ao centroide mais próximo.  
3. Os centroides são recalculados com base na média dos pontos atribuídos a cada cluster.  
4. O processo é repetido até que os centroides não mudem significativamente.  

### ✅ Diferenças Principais  
- **Hierárquico**: Não requer a definição prévia do número de clusters, gera um dendrograma e pode ser mais interpretável.  
- **K-Means**: Necessita a definição de K, é mais eficiente para grandes volumes de dados e pode ser ajustado dinamicamente.  

Ambos os métodos são amplamente utilizados para segmentação de clientes, análise de padrões e outras aplicações onde identificar grupos similares é essencial.  
