from pessoa import Pessoa
from jsonHandler import JsonHandler


class Aluno(Pessoa):
    """Classe para representar um aluno, herda de Pessoa."""

    # Cria uma instância de JsonHandler, passando seus parâmetros obrigatórios
    # Na classe Aluno a chavePrincipal sempre será "Alunos"
    json_handler = JsonHandler(arquivoJson="dados.json", chavePrincipal="Alunos")

    def __init__(
        self,
        matricula: None,  # Gerenciada dentro da classe JsonHandler
        nome: str,
        curso: str,
        notas: list,
        presencas: int,
        telefone: str,
        email: str,
    ):
        # Chamada do construtor + inicializa os atributos da superclasse (Pessoa)
        super().__init__(nome, telefone, email)
        # Comando raise ValueError: "imprime" a mensagem e interrompe a continuação do código em caso de erro
        if matricula is not None and (not isinstance(matricula, int) or matricula <= 0):
            raise ValueError("Matrícula deve ser um inteiro positivo.")
        if not curso or not isinstance(curso, str):
            raise ValueError("Curso deve ser uma string não vazia.")
        # Utilizando a "função geradora": isinstance(nota, (int, float)) for nota in notas, onde,
        # cada nota da lista é passada para o método "isinstance(nota, (int, float))", que verifica
        # se são instatâncias de int ou de float (ou seja, verificam se são um int ou um float).
        # Após a verificação de todoas as notas, é executado o método all(), que recebe o iterável retornado
        # pela "função geradora" com True ou False. Se todos forem True, é retornado True pelo all().
        if not all(isinstance(nota, (int, float)) for nota in notas):
            raise ValueError("Todas as notas devem ser números.")
        if not isinstance(presencas, int) or presencas < 0:
            raise ValueError("Presenças deve ser um inteiro não negativo.")

        # Inicializa atributos específicos da subclasse (Aluno)
        self.matricula = matricula
        self.curso = curso
        self.notas = notas
        self.presencas = presencas

    def __str__(self):
        """Retorna uma representação em string do aluno."""
        media_notas = self.calcular_media()
        notas_str = ", ".join(map(str, self.notas))
        return (
            f"Matrícula: {self.matricula}\n"
            + super().__str__()
            + f"Curso: {self.curso}\n"
            f"Notas: {notas_str}\n"
            f"Média das notas: {media_notas:.1f}\n"
            f"Presenças: {self.presencas}\n"
        )

    # É um método estático, pois não tem nenhum atributo da classe Aluno.
    # Por isso não possui o parâmetro self
    @staticmethod
    def calcular_media(notas) -> float:
        """Calcula a média das notas do aluno.

        Returns:
            float: Média das notas.
        """
        return 0.0 if len(notas) == 0 else sum(notas) / len(notas)

    # Utiliza o método interno da classe JsonHandler para adicionar o aluno no Json
    def salvar(self):
        """Salva a instância atual de Aluno usando o JsonHandler."""

        aluno_data = {
            # Matrícula está sendo gerenciado internamente pelo JsonHandler, só é realizado a
            # inicialização da matrícula com None quando os dados são inseridos, já que, mesmo sendo
            # gerenciado internamente, tem que ser instânciado para utilização posterior.
            "matricula": self.matricula,  # Como é novo dado, a matricula ainda é None -> Será criada na classe JsonHandler
            "nome": self.nome,
            "curso": self.curso,
            "notas": self.notas,
            "presencas": self.presencas,
            "telefone": self.telefone,
            "email": self.email,
        }
        try:
            self.json_handler.create(aluno_data)
            print("\nAluno salvo com sucesso.\n")
            print("Dados do aluno:")
            print(f" Matrícula: {aluno_data['matricula']}")
            print(f" Nome: {aluno_data['nome']}")
            print(f" Curso: {aluno_data['curso']}")
            print(f" Notas: {', '.join(map(str, aluno_data['notas']))}")
            print(f" Presenças: {aluno_data['presencas']}")
            print(f" Telefone: {aluno_data['telefone']}")
            print(f" Email: {aluno_data['email']}\n")
            input("Pressione Enter para continuar...")
        except Exception as e:
            print(f"Erro ao salvar aluno: {e}")

    # Update
    def atualizar(self):
        """Atualiza os dados do aluno no arquivo JSON."""
        novos_dados = {
            "matricula": self.matricula,
            "nome": self.nome,
            "curso": self.curso,
            "notas": self.notas,
            "presencas": self.presencas,
            "telefone": self.telefone,
            "email": self.email,
        }
        self.json_handler.update(self.matricula, novos_dados)

    # Delete
    def deletar(self):
        """Deleta os dados do aluno do arquivo JSON."""
        self.json_handler.delete(self.matricula)

    # Pesquisar
    def pesquisar(self, matricula):
        """Busca um aluno no arquivo JSON pela matrícula."""
        return self.json_handler.read(matricula)
