from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()


# as tabelas
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


# Livros
class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono


Base.metadata.create_all(bind=db)

# CRUD

# C - Create
# usuario = Usuario(nome="Lira2", email="qlqcoisa2@email.com", senha="123123")
# session.add(usuario)
# session.commit()

# R - READ
# lista_usuarios = session.query(Usuario).all()
# usuario_lira2 = session.query(Usuario).filter_by(email="qlqcoisa2@email.com").first()
# print(usuario_lira2)
# print(usuario_lira2.nome)
# print(usuario_lira2.email)

# livro = Livro(titulo="Nome do Vento", qtde_paginas=1000, dono=usuario_lira.id)
# session.add(livro)
# session.commit()

# U - Update
# usuario_lira.nome = "Joao Lira"
# session.add(usuario_lira)
# session.commit()

# D - Delete
# session.delete(usuario_lira2)
# session.commit()
