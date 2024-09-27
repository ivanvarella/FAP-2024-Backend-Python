from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Inicializa a aplicação Flask
app = Flask(__name__)


# Configura o banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Inicializa o objeto SQLAlchemy
db = SQLAlchemy(app)


# Importa as rotas (será criado posteriormente)
from app import routes
