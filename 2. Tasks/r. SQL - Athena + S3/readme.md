# 🧠 Athena + S3 — Introdução e Prática com SQL

## 📍 O que é o Athena?

O **Amazon Athena** é um serviço da AWS que permite consultar dados diretamente no **Amazon S3** usando **SQL padrão** (baseado em Presto). Ele elimina a necessidade de mover os dados para um banco de dados, oferecendo uma solução *serverless*, escalável e prática para análise de grandes volumes de dados.

---

## 🗂️ O que é o S3?

O **Amazon S3 (Simple Storage Service)** é o serviço de armazenamento de objetos da AWS. É nele que os arquivos (como CSV, JSON ou Parquet) ficam armazenados. No nosso caso, os dados foram salvos em buckets organizados por pastas e partições, que o Athena consegue ler diretamente.

---

## 🔧 Como utilizamos nos exercícios

Durante os exercícios, realizamos operações básicas e intermediárias usando **SQL no Athena** para interagir com os arquivos armazenados no **S3**. As etapas principais envolveram:

### ✅ Criação de Tabelas

- Definimos tabelas no Athena que apontavam para arquivos CSV no S3, especificando colunas, tipos e localização.
- Utilizamos `CREATE EXTERNAL TABLE` com particionamento em alguns casos para otimizar consultas.

### 📄 Consultas com `SELECT`

- Usamos `SELECT` para explorar os dados, filtrar registros com `WHERE`, ordenar com `ORDER BY`, agrupar com `GROUP BY`, e realizar agregações como `COUNT`, `SUM`, `AVG`, etc.
- Também aplicamos alias, junções (`JOIN`), e subqueries.

### 🧩 Atualizações com `MERGE` e `WHEN`

- Simulamos atualizações e inserções condicionais usando o comando `MERGE`, combinando dados novos com tabelas existentes.
- A cláusula `WHEN` foi usada para definir o comportamento da fusão:
  - `WHEN MATCHED THEN UPDATE`: atualiza registros existentes.
  - `WHEN NOT MATCHED THEN INSERT`: insere novos registros.

### 📌 Outras ações realizadas

- **Criação de views** para facilitar a leitura de consultas complexas.
- **Particionamento** e formatação dos dados para reduzir o custo e o tempo das queries.
- Uso de **funções SQL** para transformação de dados diretamente nas queries (ex: `CAST`, `DATE_FORMAT`, `CASE WHEN`, etc).

---

## 🧪 Resultado

Ao final dos exercícios, conseguimos:

- Integrar Athena e S3 de forma eficiente;
- Manipular dados com SQL direto em arquivos no S3;
- Automatizar tarefas de análise com queries reutilizáveis;
- Reduzir custos com estratégias de particionamento e formatos otimizados (ex: Parquet).
