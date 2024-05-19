from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import OperationalError
from urllib.parse import quote_plus

USUARIO = "postgres"
SENHA = "admin"
HOST = "localhost"
BANCO = "nyodata"
PORT = 5432

# Escape da senha para incluir caracteres especiais
SENHA_ESCAPADA = quote_plus(SENHA)

# String de conexão com parâmetros de codificação
CONN = f"postgresql+psycopg2://{USUARIO}:{SENHA_ESCAPADA}@{HOST}:{PORT}/{BANCO}?client_encoding=utf8"

# Criação do engine
engine = create_engine(CONN, echo=True)

# Criação da sessão
Session = sessionmaker(bind=engine)

# Base declarativa
Base = declarative_base()

# Definição do modelo Pessoa
class Pessoa(Base):
    __tablename__ = "pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(200))
    senha = Column(String(100))

# Criação da tabela
Base.metadata.create_all(engine)

def retorna_session():
    try:
        session = Session()
        return session
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def testar_conexao():
    try:
        # Testar a conexão com o banco de dados
        with engine.connect():
            print("Conexão bem-sucedida!")
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
