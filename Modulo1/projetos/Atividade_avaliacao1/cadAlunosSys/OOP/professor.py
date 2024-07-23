from pessoa import Pessoa
from jsonHandler import JsonHandler


class Professor(Pessoa):
    """Classe para representar um professor, herda de Pessoa."""

    # Cria uma instância de JsonHandler, passando seus parâmetros obrigatórios
    # Na classe Professor a chavePrincipal sempre será "Professores"
    json_handler = JsonHandler(arquivoJson="dados.json", chavePrincipal="Professores")

    def __init__(
        self,
        matricula: None,  # Gerenciada dentro da classe JsonHandler
        nome: str,
        disciplinas: list,
        turmas: list,
        telefone: str,
        email: str,
    ):
        # Chamada do construtor + inicialização dos atributos da superclasse (Pessoa)
        super().__init__(nome, telefone, email)
        # Comando raise ValueError: "imprime" a mensagem e interrompe a continuação do código em caso de erro
        if matricula is not None and (not isinstance(matricula, int) or matricula <= 0):
            raise ValueError("Matrícula deve ser um inteiro positivo.")
        if not disciplinas or not all(
            isinstance(disciplina, str) for disciplina in disciplinas
        ):
            raise ValueError("Disciplinas deve ser uma lista de strings não vazias.")
        if not turmas or not all(isinstance(turma, str) for turma in turmas):
            raise ValueError("Turmas deve ser uma lista de strings não vazias.")

        # Inicializa atributos específicos da subclasse (Professor)
        self.matricula = matricula
        self.disciplinas = disciplinas
        self.turmas = turmas

    def __str__(self):
        """Retorna uma representação em string do professor."""
        disciplinas_str = ", ".join(self.disciplinas)
        turmas_str = ", ".join(self.turmas)
        return (
            f"Matrícula: {self.matricula}\n"
            + super().__str__()
            + f"Disciplinas: {disciplinas_str}\n"
            f"Turmas: {turmas_str}\n"
        )

    # Utiliza o método interno da classe JsonHandler para adicionar o professor no Json
    def salvar(self):
        """Salva a instância atual de Professor usando o JsonHandler."""

        professor_data = {
            # Matrícula está sendo gerenciado internamente pelo JsonHandler, só é realizado a
            # inicialização da matrícula com None quando os dados são inseridos, já que, mesmo sendo
            # gerenciado internamente, tem que ser instânciado para utilização posterior.
            "matricula": self.matricula,  # Como é novo dado, a matricula ainda é None -> Será criada na classe JsonHandler
            "nome": self.nome,
            "disciplinas": self.disciplinas,
            "turmas": self.turmas,
            "telefone": self.telefone,
            "email": self.email,
        }
        try:
            self.json_handler.create(professor_data)
            print("\nProfessor salvo com sucesso.\n")
            print("Dados do professor:")
            print(f" Matrícula: {professor_data['matricula']}")
            print(f" Nome: {professor_data['nome']}")
            print(f" Disciplinas: {', '.join(professor_data['disciplinas'])}")
            print(f" Turmas: {', '.join(professor_data['turmas'])}")
            print(f" Telefone: {professor_data['telefone']}")
            print(f" Email: {professor_data['email']}\n")
            espere = input("Pressione Enter para continuar...")
        except Exception as e:
            print(f"Erro ao salvar professor: {e}")

    # Update
    def atualizar(self):
        """Atualiza os dados do professor no arquivo JSON."""
        novos_dados = {
            "matricula": self.matricula,
            "nome": self.nome,
            "disciplinas": self.disciplinas,
            "turmas": self.turmas,
            "telefone": self.telefone,
            "email": self.email,
        }
        self.json_handler.update(self.matricula, novos_dados)

    # Delete
    def deletar(self):
        """Deleta os dados do professor do arquivo JSON."""
        self.json_handler.delete(self.matricula)

    # Pesquisar
    def pesquisar(self, matricula):
        """Busca um professor no arquivo JSON pela matrícula."""
        return self.json_handler.read(matricula)
