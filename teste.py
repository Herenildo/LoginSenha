
Claro! Aqui está um exemplo simples de como testar a conexão com um banco de dados PostgreSQL usando SQLAlchemy em Python:

python
Copiar código
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Defina a string de conexão com seu banco de dados PostgreSQL
# Substitua 'seu_usuario', 'sua_senha', 'seu_host' e 'seu_banco' pelos valores apropriados
CONN_STRING = 'postgresql://seu_usuario:sua_senha@seu_host/seu_banco'

def testar_conexao(conn_string):
    try:
        # Crie uma engine SQLAlchemy
        engine = create_engine(conn_string)
        
        # Tente conectar ao banco de dados
        with engine.connect():
            print("Conexão bem-sucedida!")
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

# Chame a função para testar a conexão
testar_conexao(CONN_STRING)