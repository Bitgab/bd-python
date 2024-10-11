import os 
from sqlalchemy     import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
os.system("cls || clear")

# Criando banco de dados.
db = create_engine("sqlite:///bancoDeDados")

# Criando uma conexão com banco de dados.
Session = sessionmaker(bind=db)
session = Session()

# Criando tabelas.
Base = declarative_base()

class Aluno(Base):
    # Definindo o nome da tabela.
    __tablename__ = "aluno"
    # Definindo atributos da tabela.
    ra    = Column ("R.A", Integer, primary_key=True, autoincrement=True)
    nome  = Column ("nome", String)
    idade = Column ("idade", Integer)
    email = Column ("e-mail", String)
    senha = Column ("senha", String)

    # Definindo atributos da classe.
    def __init__(self,nome: str, email: str, senha: str) -> None:
        self.nome  = nome
        self.idade = idade
        self.email = email
        self.senha = senha
  
# Criando tabela no banco.
Base.metadata.create_all(bind=db)

# Pergunta ao usuário.
for i in range (2):
    nome  = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ") 

    aluno = Aluno(senha=senha, nome=nome, email=email) 
    session.add(aluno)
    session.commit()
    print()  
# Mostrar conteúdo  do banco de dados.
print("Listando aluno no banco de dados.")
lista_aluno  =  session.query(Aluno).all()

for aluno in lista_aluno:
    print(f"{aluno.nome} - {aluno.idade} - {aluno.email}")

# Deletando um usuário.
print("\nExcluindo usuário no banco de dados.")
email_usuario = input("Informe o e-mail do usuário: ")
aluno = session.query(Aluno).filter_by(email = email_usuario).first()
if aluno:
    session.delete(aluno)
    session.commit()   
    print("\nAluno deletado com sucesso.")
else: 
    print("Aluno não encontrado.")    

#Mostrando conteúdo do banco de dados.
print("\nListando usuário no banco de dados.")
lista_aluno = session.query(Aluno).all()

for aluno in lista_aluno:
    print(f"{aluno.nome} - {aluno.idade} - {aluno.email}")

# Atualizar um usuário.
print("\nAtualizando os dados de um usuário") 

email_usuario = input("Informe o e-mail do usuário: ")
aluno = session.query(Aluno).filter_by(email = email_usuario).first() 
if aluno:
    aluno.nome  = input("Digite o nome: ")
    aluno.idade = input("Digite sua idade: ")
    aluno.email = input("Digite seu e-mail: ")
    aluno.senha = input("Digite sua senha: ")
    session.commit()
else:     
    print("Aluno não encontrado.")  
# Pesquisando um usuário.
print("\nPesquisando um usuário pelo e-mail.")
email_usuario = input("Iforme o e-mail do usuário: ")

aluno = session.query(Aluno).filter_by(email = email_usuario).filter()
if aluno:
    print(f"{aluno.nome} - {aluno.idade} - {aluno.email}")
else: 
    print("Aluno não encontrado.")      
r
# Fechando conexão
session.commit()