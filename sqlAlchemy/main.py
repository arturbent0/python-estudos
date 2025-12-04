from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine('sqlite:///meubanco.db')
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

#coloca as tabelas aqui
class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha",String)
    ativo = Column ("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo

class Livro(Base):

    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qnt_paginas = Column("qnt_paginas", String)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, qnt_paginas, dono):
        self.titulo =  titulo
        self.qnt_paginas = qnt_paginas
        self.dono = dono

Base.metadata.create_all(bind=db)

# CRUD

# Criar
# usuario = Usuario(nome="Artur", email="blabla@email.com", senha="123123")
# session.add(usuario)
# session.commit()

# Ler
#lista_usuarios = session.query(Usuario).all()
usuario_artur = session.query(Usuario).filter_by(email="blabla@email.com").first()
print(usuario_artur)
print(usuario_artur.nome)
print(usuario_artur.email)

# livro = Livro(titulo="Book", qnt_paginas=50, dono=usuario_artur.id)
# session.add(livro)
# session.commit()

# Update
# usuario_artur.nome = "Artur Bento"
# session.add(usuario_artur)
# session.commit()

# Deletar
session.delete(usuario_artur)
session.commit()
