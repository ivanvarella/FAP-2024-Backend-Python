# Importando as classes do arquivo alunos.py
from alunos import Pessoa, Aluno
from jsonHandler import JsonHandler

# Criar uma instância de JsonHandler
json_handler = JsonHandler(arquivoJson="alunos.json", chavePrincipal="Alunos")


def testar_pessoa():
    print("Testando Pessoa:")
    try:
        p = Pessoa(nome="João", telefone="123456789", email="joao@example.com")
        print(p)

        # Testando exceções - criando uma instância de Pessoa sem o nome
        try:
            p = Pessoa(nome="", telefone="123456789", email="joao@example.com")
        except ValueError as e:
            print(f"Erro esperado ao criar Pessoa: {e}")

    except Exception as e:
        print(f"Erro ao testar Pessoa: {e}")


def testar_aluno():
    print("\nTestando Aluno:")
    try:
        a = Aluno(
            matricula=None,
            nome="Maria",
            curso="Matemática",
            notas=[9.5, 8.0, 7.5],
            presencas=15,
            telefone="987654321",
            email="maria@example.com",
            json_handler=json_handler,  # Passando a instância de JsonHandler
        )
        print(a)

        # Testando o cálculo da média
        print(f"Média das notas: {a.calcular_media()}")

        # Testando exceções
        try:
            a = Aluno(
                matricula=None,
                nome="Maria",
                curso="Matemática",
                notas=[9.5, 8.0, 7.5],
                presencas=15,
                telefone="987654321",
                email="maria@example.com",
                json_handler=json_handler,  # Passando a instância de JsonHandler
            )
        except ValueError as e:
            print(f"Erro esperado ao criar Aluno: {e}")

        try:
            a = Aluno(
                matricula=None,
                nome="Maria",
                curso="",
                notas=[9.5, "8.0", 7.5],  # nota inválida
                presencas=15,
                telefone="987654321",
                email="maria@example.com",
                json_handler=json_handler,  # Passando a instância de JsonHandler
            )
        except ValueError as e:
            print(f"Erro esperado ao criar Aluno: {e}")

        try:
            a = Aluno(
                matricula=None,
                nome="Maria",
                curso="Matemática",
                notas=[9.5, 8.0, 7.5],
                presencas=-1,  # presença inválida
                telefone="987654321",
                email="maria@example.com",
                json_handler=json_handler,  # Passando a instância de JsonHandler
            )
        except ValueError as e:
            print(f"Erro esperado ao criar Aluno: {e}")

    except Exception as e:
        print(f"Erro ao testar Aluno: {e}")


# Só executar as funções abaixo se for executado diretamente, ou seja,
# se o arquivo em si for executado diretamente
# Ou forma de visualizar: Caso esse arquivo (testeClass_Alunos.py) for
# importado em outro arquivo, o __main__ será outro e não irá executar o
# código abaixo.
if __name__ == "__main__":
    testar_pessoa()
    testar_aluno()

    # Criar uma instância de Aluno, passando a instância de JsonHandler
    aluno = Aluno(
        matricula=None,
        nome="João",
        curso="Matemática",
        notas=[9.5, 8.0, 7.5],
        presencas=15,
        telefone="987654321",
        email="joao@example.com",
        json_handler=json_handler,  # Passando a instância de JsonHandler
    )

    # Salvar o aluno usando o método salvar que utiliza JsonHandler
    aluno.salvar()
