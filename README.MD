# Sistema CRUD de Vendas em Python

Este projeto é um sistema CRUD simples em Python que permite gerenciar vendas em um banco de dados MySQL. A aplicação possibilita criar, listar, atualizar e deletar registros diretamente pelo terminal.

## Estrutura do Projeto

crud_python/ │ 
├── main.py # Ponto de entrada da aplicação 
├── db.py # Gerencia a conexão com o banco de dados 
├── crud.py # Funções CRUD 
├── models.py # Modelos de dados 
├── utils.py # Funções utilitárias
├── requirements.txt # Dependências do projeto
└── README.md # Documentação


## Pré-requisitos

- Python 3.x
- MySQL
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório e acesse o diretório:

    ```bash
    git clone https://github.com/seu_usuario/crud_python.git
    cd crud_python
    ```

2. Crie e ative o ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados MySQL:

    ```sql
    CREATE DATABASE crud_python;
    USE crud_python;

    CREATE TABLE vendas (
        id_vendas INT AUTO_INCREMENT PRIMARY KEY,
        nome_produto VARCHAR(255),
        valor_produto DECIMAL(10,2)
    );
    ```

5. Configure suas credenciais MySQL no arquivo `db.py`, exemplo:

    ```plaintext
        host='localhost',
        user='root',
        password='1341',
        database='crud_python'
    ```

## Uso

1. Execute o programa:

    ```bash
    python main.py
    ```

2. Interaja com o menu para realizar operações de CRUD:

    - Criar venda
    - Listar todas as vendas
    - Atualizar uma venda
    - Deletar uma venda

## Contribuição

Sinta-se à vontade para contribuir com melhorias ao projeto abrindo uma issue ou enviando um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT.
