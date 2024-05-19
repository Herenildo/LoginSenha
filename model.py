from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


USUARIO = "postgres"
SENHA = "admin"
HOST = "localhost"
BANCO = "nyodata"
PORT = 5432

CONN = f"postgresql+psycopg2://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CONN, echo=True)

Session = sessionmaker(bind=engine)


session = Session()
Base = declarative_base()


def testar_conexao(conn_string):
    try:
        # Crie uma engine SQLAlchemy
        engine = create_engine(conn_string)
        
        # Tente conectar ao banco de dados
        with engine.connect():
            print("Conexão bem-sucedida!")
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")


testar_conexao(CONN)

'''

class Pessoa(Base):
    __tablename__ = "pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))

'''

Base.metadata.create_all(engine)
