# Framework de Persistência

Para esse trabalho foi desenvolvida uma aplicação simples de cadastro de pessoas (Nome, CPF, RG, Endereço…) utilizando a linguagem de programação Python 3 com a biblioteca Tkinter e o Framework de persistência de dados SQLAlchemy. Como banco de dados foi utilizado o PostgreSQL 12.

Para instalação das dependências:

    pip install python-dotenv sqlachemy psycopg2
    
Para executar o programa:

    python3 main.py

O SQLAlchemy permite definir o nível de isolamento de transações no momento da criação da “engine” da conexão ou no momento da criação das transações, como no exemplo abaixo:

    with engine.connect() as conn:
        conn = conn.execution_options(
            isolation_level="SERIALIZABLE",
            postgresql_readonly=True,
            postgresql_deferrable=True
        )	
        with conn.begin():
            #  aqui são executadas as queries da transação
            conn.execute(sql1)
            conn.execute(sql2)

Os valores possíveis para o parâmetro transaction_level são:
- READ COMMITTED
- READ UNCOMMITTED
- REPEATABLE READ
- SERIALIZABLE
- AUTOCOMMIT

