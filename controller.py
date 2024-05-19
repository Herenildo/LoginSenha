from model import Pessoa, retorna_session, testar_conexao
from sqlalchemy.exc import SQLAlchemyError
import hashlib


class ControllerCadastro():
    @classmethod
    def verifica_dados(cls, nome, email,senha):
        if len(nome) > 50 or len(nome) <3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4

        return 1


    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = retorna_session()
        if not session:
            return 6


        try:
            usuario = session.query(Pessoa).filter(Pessoa.email == email).all()

            if len(usuario)> 0:
                return 5

            dados_verificados = cls.verifica_dados(nome, email, senha)

            if dados_verificados != 1:
                return dados_verificados

       
            senha = hashlib.sha256(senha.encode()).hexdigest()
            p1 = Pessoa(nome=nome, email=email,senha=senha)
            session.add(p1)
            session.commit()
            print("Cadastro realizado com sucesso.")
            return 1

        except SQLAlchemyError as e:
            print(f"Erro ao cadastrar usuário: {e}")
            session.rollback()  # Desfaz qualquer mudança pendente no caso de erro
            return 6

        finally:
            session.close()

testar_conexao()



class ControllerLogin():
    @classmethod
    def login(cls, email, senha):
        session = retorna_session()
        senha =  hashlib.sha256(senha.encode()).hexdigest()
        conectado = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha).all()
        if len(conectado) == 1:
            return {'Conectado':True, 'id': conectado[0].id}
        else:
            return False

#print(ControllerCadastro.cadastrar('Laina','laina@gmail.com','456Mudar'))
#print(ControllerLogin.login('laina@gmail.com','456Mudar'))
