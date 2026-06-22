# Video da Aplicação

https://github.com/user-attachments/assets/459832bf-c24b-44fd-9e4c-2541b77a9add






# Sistema de Vendas - Aplicação Web CRUD

Aplicação web CRUD para gerenciamento de vendas de produtos, desenvolvida com Flask e MySQL. O projeto permite cadastrar, visualizar, editar e excluir registros por meio de uma interface simples e intuitiva.

## Funcionalidades

- **Create**: Adicionar novos produtos com nome e valor
- **Read**: Visualizar todos os produtos em uma tabela estilizada
- **Update**: Editar valores de produtos separadamente dos nomes
- **Delete**: Remover produtos com diálogo de confirmação
- **Interface Moderna**: Design gradiente bonito com layout responsivo
- **Banco de Dados em Tempo Real**: Integração direta com banco de dados MySQL

## Estrutura de Pastas

```
crud.py/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── templates/             # Templates HTML
│   ├── index.html        # Página principal (lista todos os produtos)
│   ├── create.html       # Formulário para adicionar novos produtos
│   ├── update.html       # Formulário para editar valores de produtos
│   └── update_name.html  # Formulário para editar nomes de produtos

```

## Pré-requisitos

Antes de executar este aplicativo, certifique-se de ter:

1. **Python 3.7+** instalado no seu sistema
2. **MySQL Server** rodando no localhost
3. Um banco de dados MySQL chamado `bdcrud` com uma tabela chamada `vendas`

## Instalação

1. **Navegue até o diretório do projeto:**
   ```bash
   cd crud.py
   ```

2. **Instale as dependências necessárias:**
   ```bash
   pip install -r requirements.txt
   ```

   Isso instalará:
   - Flask (framework web)
   - mysql-connector-python (conector de banco de dados MySQL)

## Configuração do Banco de Dados

### Criar o Banco de Dados

```sql
CREATE DATABASE bdcrud;
```

### Criar a Tabela

```sql
USE bdcrud;

CREATE TABLE vendas (
    idproduto INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(255) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL
);
```

### Configurar Conexão com o Banco de Dados

Edite a função `get_db_connection()` em `app.py` se suas credenciais MySQL forem diferentes:

```python
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="phcf1704",  # Altere para sua senha do MySQL
        database="bdcrud"
    )
```

## Executando a Aplicação

1. **Inicie o servidor Flask:**
   ```bash
   python app.py
   ```

2. **Abra seu navegador web** e navegue para:
   ```
   http://127.0.0.1:5000
   ```

   O aplicativo estará rodando em modo de debug, então qualquer alteração no código recarregará automaticamente o servidor.

## Como Usar

### Adicionar um Produto

1. Clique no botão **"+ Adicionar Produto"**
2. Digite o nome do produto e o valor
3. Clique em **"Salvar"** para adicionar o produto

### Visualizar Produtos

- A página principal exibe todos os produtos em uma tabela
- Cada linha mostra: Nome do Produto, Valor e Botões de Ação

### Editar Valor do Produto

1. Clique no botão **"Editar o Valor"** (amarelo) ao lado de qualquer produto
2. Digite o novo valor
3. Clique em **"Atualizar"** para salvar as alterações

### Editar Nome do Produto

1. Clique no botão **"Editar o Nome"** (azul) ao lado de qualquer produto
2. Digite o novo nome do produto
3. Clique em **"Atualizar Nome"** para salvar as alterações

### Excluir um Produto

1. Clique no botão **"Excluir"** (vermelho) ao lado de qualquer produto
2. Confirme a exclusão no diálogo
3. O produto será removido do banco de dados

## Recursos da Interface

- **Design Gradiente**: Fundo gradiente roxo moderno
- **Layout Responsivo**: Funciona em diferentes tamanhos de tela
- **Ações Codificadas por Cores**:
  - Amarelo: Editar valor
  - Azul: Editar nome
  - Vermelho: Excluir
- **Diálogos de Confirmação**: Evita exclusões acidentais
- **Estado Vazio**: Mensagem amigável quando não existem produtos

## Solução de Problemas

### Erro de Conexão Recusada

Se você ver "A conexão com 127.0.0.1 foi recusada":
- Certifique-se de que o servidor Flask está rodando (`python app.py`)
- Verifique se nenhum outro aplicativo está usando a porta 5000

### Erro de Conexão com o Banco de Dados

Se você não consegue conectar ao banco de dados:
- Verifique se o MySQL está rodando
- Verifique suas credenciais do banco de dados em `app.py`
- Certifique-se de que o banco de dados `bdcrud` existe

### Editar/Excluir Não Funciona

Se as operações de edição ou exclusão não parecem funcionar:
- Verifique a saída do terminal para instruções de debug SQL
- Verifique se a estrutura da tabela do banco de dados corresponde ao esquema esperado
- Certifique-se de que o nome do produto existe no banco de dados

## Notas

- O aplicativo roda em modo de desenvolvimento por padrão
- Todas as operações do banco de dados usam consultas parametrizadas para prevenir injeção SQL

## Tecnologias Utilizadas

- **Flask**: Framework web Python
- **MySQL**: Banco de dados relacional
- **HTML5/CSS3**: Estilização do frontend
- **Jinja2**: Motor de templates

