# HAR (Human Activity Recognition) e PCA  

## O que é HAR?  

HAR (*Human Activity Recognition*) é uma área de aprendizado de máquina voltada para o reconhecimento de atividades humanas a partir de sensores, como acelerômetros e giroscópios. Esses sensores capturam dados sobre os movimentos do corpo, permitindo classificar atividades como caminhar, correr, subir escadas, entre outras.  

## O papel do PCA no HAR  

O PCA (*Principal Component Analysis*) é uma técnica de redução de dimensionalidade que ajuda a lidar com a alta quantidade de variáveis presentes nos dados de sensores.  

### Por que usar PCA no HAR?  

- **Redução de Ruído**: Sensores captam dados brutos que podem conter ruídos e correlações redundantes. O PCA ajuda a filtrar informações mais relevantes.  
- **Melhora da Eficiência Computacional**: Com menos variáveis, os modelos de aprendizado de máquina podem ser treinados mais rapidamente.  
- **Melhor Generalização**: Reduzir a dimensionalidade pode evitar o overfitting e melhorar o desempenho do modelo em novos dados.  

Ao aplicar PCA no HAR, mantemos as informações mais importantes dos sensores, reduzimos a complexidade dos modelos e melhoramos a precisão da classificação das atividades.  
