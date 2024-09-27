from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cliente(db.Model):
    cliente_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(1), nullable=False)
    telefone = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(40), nullable=False)


class Ficha(db.Model):
    ficha_id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    observacao = db.Column(db.Text)

    # A refência estava errada....
    # Obs: a referência é pelo nome do campo nas tabelas, não pela Classe que a gerencia,
    # pois isso é cliente.cliente_id e não Cliente.cliente_id
    cliente_id = db.Column(
        db.Integer, db.ForeignKey("cliente.cliente_id"), nullable=False
    )
