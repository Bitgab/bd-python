import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# Criando uma conexão com banco de dados
Session = sessionmaker(bind=db)
session = Session()

# I/O
# I = input   (Entrada)
# O = outout (saída)

# Criando tabelas.
Base = declarative_base()

class Usuario(Base): 
    # Definindo nome da tabela. 
    __tablename__ = "usuarios"
    # Definindo atributos da tabela,
    id    = Column("id", Integer, primary_key=True, autoincrement=True)
    nome  = Column("nome" , String)
    email = Column("email",String)
    senha = Column("senha", String) 

    # Definindo  atributos da classe.
    def __init__(self,nome: str, email: str, senha: str) -> None:
        self.nome  = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco
Base.metadata.create_all(bind=db)

# Salvar no banco de dados.
# usuario = Usuario("Maria", "maria@gmail.com", "123")
usuario = Usuario("Samir Fuboca","fuboca@gmaiol.com","123")
session.add(usuario)
session.commit()

# Mostrando conteúdo de banco de dados.
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")








# Persistir - no Banco de Dados.    
# SGBD Sistema   
# Liguagem do Banco de Dados SQL - Relacionais
# Comando para criar Banco de Dados, Tabelas...
# SELECT * FROM CLIENTES = Linguagem de consulta
# INSERT, CREATE TABLE, CRETE DATABASE....
# Posso colocar dentro do código
# BACKEND - SQL posso colocar dentro do código
# ORM
#pip instal sqlalchemy - Feramenta  ORM que pertimte fazer banco
# Códido legado que usa mais de 10 anos.  

# Chave primaria 
#bind uma conexão com alguma coisa, no exemplo aqui ele está conectado o database.1