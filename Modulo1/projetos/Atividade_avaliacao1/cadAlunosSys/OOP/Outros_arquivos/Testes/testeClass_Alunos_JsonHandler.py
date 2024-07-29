# Importando as classes
from aluno import Aluno
from pessoa import Pessoa
from professor import Professor
from jsonHandler import JsonHandler

# Cria uma instância de JsonHandler
json_handler = JsonHandler(arquivoJson="testeClassAlunos.json", chavePrincipal="Alunos")


def testar_pessoa():
    print("Testando Pessoa:")
    try:
        p = Pessoa(nome="João", telefone="123456789", email="joao@example.com")
        print(p)
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
            # json_handler=json_handler,
        )
        # Testa o __str__ (representação em string da classe)
        print(a)
        print(f"Média das notas: {a.calcular_media()}")
        try:
            a = Aluno(
                matricula=None,
                nome="Maria",
                curso="Matemática",
                notas=[9.5, 8.0, 7.5],
                presencas=15,
                telefone="987654321",
                email="maria@example.com",
                # json_handler=json_handler,
            )
        except ValueError as e:
            print(f"Erro esperado ao criar Aluno: {e}")
        try:
            a = Aluno(
                matricula=None,
                nome="Maria",
                curso="",  # Erro Curso vazio
                notas=[9.5, "8.0", 7.5],
                presencas=15,
                telefone="987654321",
                email="maria@example.com",
                # json_handler=json_handler,
            )
        except ValueError as e:
            print(f"Erro esperado ao criar Aluno: {e}")
        try:
            a = Aluno(
                matricula=None,
                nome="Maria",
                curso="Matemática",
                notas=[9.5, 8.0, 7.5],
                presencas=-1,  # Erro presencas negativo
                telefone="987654321",
                email="maria@example.com",
                # json_handler=json_handler,
            )
        except ValueError as e:
            print(f"Erro esperado ao criar Aluno: {e}")
    except Exception as e:
        print(f"Erro ao testar Aluno: {e}")


if __name__ == "__main__":
    testar_pessoa()
    testar_aluno()
    aluno = Aluno(
        matricula=None,
        nome="João",
        curso="Matemática",
        notas=[9.5, 8.0, 7.5],
        presencas=15,
        telefone="987654321",
        email="joao@example.com",
        # json_handler=json_handler,
    )
    aluno2 = Aluno(
        matricula=None,
        nome="Nome Aluno 2",
        curso="Python",
        notas=[10, 5.0, 9.3],
        presencas=99,
        telefone="321654987",
        email="aluno2@example.com",
        # json_handler=json_handler,
    )
    aluno.salvar()
    aluno2.salvar()
