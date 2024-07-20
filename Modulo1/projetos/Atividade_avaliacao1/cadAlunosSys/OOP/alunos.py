# Uma classe Aluno com atributos apropriados e métodos para:
# o Adicionar notas
# o Calcular a média - Ok
# o Representar o aluno como string ->  def __str__(self): - OK

# Classe que gerencia os dados do(s) arquivo(s) Json
from jsonHandler import JsonHandler


# A classe Pessoa só serve para a utilização de Aluno ou de futuras classes,
# por exemplo, professores, funcionários...
class Pessoa:
    """Classe base para representar uma pessoa."""

    def __init__(self, nome: str, telefone: str, email: str):
        # Comando raise ValueError: "imprime" a mensagem e interrompe a continuação do código
        if not nome or not isinstance(nome, str):
            raise ValueError("Nome deve ser uma string não vazia.")
        if not telefone or not isinstance(telefone, str):
            raise ValueError("Telefone deve ser uma string não vazia.")
        if not email or not isinstance(email, str):
            raise ValueError("Email deve ser uma string não vazia.")

        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        """Retorna uma representação em string da pessoa."""
        return (
            f"Nome: {self.nome}\n"
            f"Telefone: {self.telefone}\n"
            f"Email: {self.email}\n"
        )


class Aluno(Pessoa):
    """Classe para representar um aluno, herda de Pessoa."""

    def __init__(
        self,
        matricula: None,  # Gerenciada dentro da classe JsonHandler
        nome: str,
        curso: str,
        notas: list,
        presencas: int,
        telefone: str,
        email: str,
        json_handler: JsonHandler,  # Parâmetro classe JsonHandler
    ):
        # Chamada do construtor + inicializa os atributos da superclasse (Pessoa)
        super().__init__(nome, telefone, email)
        # Comando raise ValueError: "imprime" a mensagem e interrompe a continuação do código
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

        # Validação do json_handler
        if not isinstance(json_handler, JsonHandler):
            raise ValueError("json_handler deve ser uma instância de JsonHandler.")

        # Inicializa atributos específicos da subclasse (Aluno)
        self.matricula = matricula
        self.curso = curso
        self.notas = notas
        self.presencas = presencas
        # Armazena a instância de JsonHandler de forma a permitir a utilização dos
        # métodos da classe JsonHandler para manipular os dados do arquivo Json
        self.json_handler = json_handler

    def calcular_media(self) -> float:
        """Calcula a média das notas do aluno.

        Returns:
            float: Média das notas.
        """
        if len(self.notas) == 0:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        """Retorna uma representação em string do aluno."""
        media_notas = self.calcular_media()
        notas_str = ", ".join(map(str, self.notas))
        return (
            super().__str__() + f"Matrícula: {self.matricula}\n"
            f"Curso: {self.curso}\n"
            f"Notas: {notas_str}\n"
            f"Média das notas: {media_notas:.1f}\n"
            f"Presenças: {self.presencas}\n"
        )

    # Mudar esse método para a classe: GerenciadorAlunos
    # Utiliza o método interno da classe JsonHandler para adicionar o aluno no Json
    def salvar(self):
        """Salva a instância atual de Aluno usando o JsonHandler."""

        if self.matricula is None:
            # Gerar uma nova matrícula se não estiver definida
            self.matricula = self.json_handler.gerar_matricula()

        aluno_data = {
            # Matrícula está sendo gerenciado pos JsonHandler, nesse caso eu não posso
            # mandar a matrícula dessa forma, talvez eu possa somente inicializar a matrícula
            # em Alunos como None, ou talvés seja melhor passar a criação da matrícula aqui em Alunos
            "matricula": self.matricula,
            "nome": self.nome,
            "curso": self.curso,
            "notas": self.notas,
            "presencas": self.presencas,
            "telefone": self.telefone,
            "email": self.email,
        }
        self.json_handler.create(aluno_data)


# class Professor(Pessoa):
#     """Classe para representar um professor, herda de Pessoa."""

#     def __init__(self, matricula: int, nome: str, telefone: str, email: str, departamento: str):
#         super().__init__(nome, telefone, email)
#         self.matricula = matricula
#         self.departamento = departamento

#     def __str__(self):
#         """Retorna uma representação em string do professor."""
#         return (super().__str__() +
#                 f"Matrícula: {self.matricula}\n"
#                 f"Departamento: {self.departamento}\n")

# class GerenciarAlunos:
#     """Classe para gerenciar alunos."""

#     def __init__(self):
#         self.alunos = []

#     def create_aluno(self, matricula: int, nome: str, curso: str, notas: list, presencas: int, telefone: str, email: str):
#         """Cria um novo aluno e adiciona à lista de alunos."""
#         aluno = Aluno(matricula, nome, curso, notas, presencas, telefone, email)
#         self.alunos.append(aluno)

#     def read_alunos(self):
#         """Imprime as informações de todos os alunos."""
#         for aluno in self.alunos:
#             print(aluno)

#     def update_aluno(self, matricula: int, nome=None, telefone=None, email=None, curso=None, notas=None, presencas=None):
#         """Atualiza as informações de um aluno específico."""
#         for aluno in self.alunos:
#             if aluno.matricula == matricula:
#                 aluno.atualizar_info(nome, telefone, email)
#                 if curso:
#                     aluno.curso = curso
#                 if notas is not None:
#                     aluno.notas = notas
#                 if presencas is not None:
#                     aluno.presencas = presencas
#                 break
#         else:
#             print(f"Aluno com matrícula {matricula} não encontrado.")

#     def delete_aluno(self, matricula: int):
#         """Remove um aluno da lista baseado na matrícula."""
#         self.alunos = [aluno for aluno in self.alunos if aluno.matricula != matricula]

# class GerenciarProfessores:
#     """Classe para gerenciar professores."""

#     def __init__(self):
#         self.professores = []

#     def create_professor(self, matricula: int, nome: str, telefone: str, email: str, departamento: str):
#         """Cria um novo professor e adiciona à lista de professores."""
#         professor = Professor(matricula, nome, telefone, email, departamento)
#         self.professores.append(professor)

#     def read_professores(self):
#         """Imprime as informações de todos os professores."""
#         for professor in self.professores:
#             print(professor)

#     def update_professor(self, matricula: int, nome=None, telefone=None, email=None, departamento=None):
#         """Atualiza as informações de um professor específico."""
#         for professor in self.professores:
#             if professor.matricula == matricula:
#                 professor.atualizar_info(nome, telefone, email)
#                 if departamento:
#                     professor.departamento = departamento
#                 break
#         else:
#             print(f"Professor com matrícula {matricula} não encontrado.")

#     def delete_professor(self, matricula: int):
#         """Remove um professor da lista baseado na matrícula."""
#         self.professores = [professor for professor in self.professores if professor.matricula != matricula]


# ========================================================================================================================================
# class Aluno:
#     def __init__(self, matricula: int, nome: str, curso: str, notas: list, presencas: int, telefone: str, email: str):
#         self.matricula = matricula
#         self.nome = nome
#         self.curso = curso
#         self.notas = notas
#         self.presencas = presencas
#         self.telefone = telefone
#         self.email = email

# def calcular_media(self):
#     if len(self.notas) == 0:
#         return 0
#     return sum(self.notas) / len(self.notas)

#     # Método __str__ para representar o aluno como string
#     # Quando você usa a função print() (por exemplo: print(alunoX)) em um objeto dessa classe,
#     # ou quando você converte o objeto para uma string, o método __str__
#     # é chamado para gerar uma representação legível do objeto.
#     def __str__(self):
#         media_notas = self.calcular_media()
#         notas_str = ", ".join(map(str, self.notas))
#         return (f"Matrícula: {self.matricula}\n"
#                 f"Nome: {self.nome}\n"
#                 f"Curso: {self.curso}\n"
#                 f"Notas: {notas_str}\n"
#                 f"Média das notas: {media_notas:.1f}\n"
#                 f"Presenças: {self.presencas}\n"
#                 f"Telefone: {self.telefone}\n"
#                 f"Email: {self.email}\n")


# Uma classe GerenciadorAlunos que gerencia uma coleção de objetos Aluno e
# implementa métodos para:
# o Cadastrar um novo aluno
# o Listar todos os alunos
# o Buscar um aluno por matrícula
# o Editar informações de um aluno
# o Excluir um aluno

# self.matricula = matricula
# self.nome = nome
# self.curso = curso
# self.notas = notas
# self.presencas = presencas
# self.telefone = telefone
# self.email = email

# class GerenciadorAlunos:
#     def __init__(self):
#         self.alunos = []

#     def cadastrar_aluno(self, aluno: Aluno):
#         self.alunos.append(aluno)

#     def listar_alunos(self):
#         for aluno in self.alunos:
#             aluno.exibir_informacoes()
#             print()

#     def buscar_aluno(self, matricula: int):
#         for aluno in self.alunos:
#             if aluno.matricula == matricula:
#                 return aluno

#     def editar_aluno(self, matricula: int, novos_dados: dict):
#         aluno = self.buscar_aluno(matricula)
#         if aluno:
#             aluno.nome = novos_dados.get("nome", aluno.nome)
#             aluno.idade = novos_dados.get("idade", aluno.idade)
#             aluno.curso = novos_dados.get("curso", aluno.curso)
#             print("Informações do aluno atualizadas com sucesso.")
#         else:
#             print("Aluno não encontrado.")

#     def excluir_aluno(self, matricula: int):
#         aluno = self.buscar_aluno(matricula)
#         if aluno:
#             self.alunos.remove(aluno)
#             print("Aluno excluído com sucesso.")
#         else:
#             print("Aluno não encontrado.")


# class GerenciarAlunos:
#     def __init__(self):
#         self.alunos = []


#     def create_aluno(self, nome: str, curso: str, notas: list, presencas: int, telefone: str, email: str):
#         aluno = Aluno(nome, matricula, telefone, email, aniversario)
#         self.alunos.append(aluno)
#         return aluno

#     def read_alunos(self):
#         return self.alunos

#     def update_aluno(self, matricula):
#         aluno = self.find_aluno(matricula)
#         if aluno:
#             aluno.atualizar_info(nome, telefone, email, aniversario)
#             return aluno
#         return None

#     def delete_aluno(self, matricula):
#         aluno = self.find_aluno(matricula)
#         if aluno:
#             self.alunos.remove(aluno)
#             return True
#         return False

#     def find_aluno(self, matricula):
#         for aluno in self.alunos:
#             if aluno.matricula == matricula:
#                 return aluno
#         return None
