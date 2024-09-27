# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def inicio():
#     return "Olá pessoal com Flask"


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
from models import db, Cliente
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


# Rota inicial
@app.route("/")
def inicio():
    return "Olá pessoal com Flask"


# Rota para adicionar um cliente via POST
@app.route("/add-cliente", methods=["POST"])
def add_cliente():
    data = request.json  # Espera os dados em formato JSON
    if not data:
        return jsonify({"error": "Nenhum dado foi fornecido"}), 400

    # Verifica se o email já está cadastrado no banco de dados
    cliente_existente = Cliente.query.filter_by(email=data.get("email")).first()
    if cliente_existente:
        return jsonify({"error": "Cliente com esse email já existe!"}), 400

    # Criando um novo cliente com os dados recebidos
    try:
        novo_cliente = Cliente(
            nome=data["nome"],
            genero=data["genero"],
            telefone=data["telefone"],
            email=data["email"],
        )
        db.session.add(novo_cliente)
        db.session.commit()

        return jsonify({"message": "Cliente adicionado com sucesso!"}), 201

    except KeyError as e:
        return jsonify({"error": f"Campo ausente: {str(e)}"}), 400


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
