import json
import os
import funcoesSuporte as func

# Parâmetros obrigatórios:
# - arquivoJson (nome e extensão do arquivo Json)
# - chavePrincipal
# Parâmetro opcional: caminhoDirAtual (para caso o arquivo manipulado esteja em
# outro diretório que não o mesmo onde a classe foi importada)


class JsonHandler:
    def __init__(self, arquivoJson, chavePrincipal, caminhoDirJson=""):
        self.arquivoJson = arquivoJson
        self.chavePrincipal = chavePrincipal
        if caminhoDirJson == "":
            # Caminho do diretório atual
            caminhoDirJson = os.getcwd()
            self.caminho = os.path.join(
                caminhoDirJson,
                "Modulo1",
                "projetos",
                "Atividade_avaliacao1",
                "cadAlunosSys",
                "OOP",
            )
        else:
            # Caminho passado pelo parâmetro opcional
            self.caminho = caminhoDirJson

        self.caminhoCompletoJson = os.path.join(self.caminho, self.arquivoJson)

    # Verifica e inicializa o arquivo Json
    def verificar_e_inicializar_json(self):
        # Verifica se o arquivo JSON existe e o cria caso não exista
        # (só a primeira vez que rodar o programa)
        if not os.path.exists(self.caminhoCompletoJson):
            print(
                f"\nAinda não existe o Arquivo JSON ({self.arquivoJson}) no diretório: {self.caminho}."
            )
            while True:
                print("Caso deseje criar um novo arquivo digite 1 ou 0 para sair.")
                # Configuração automática do Black, criando essa tupla aí!
                # Não muda nada, pois pode-se acessar os dados da tupla diretamente
                (
                    criarNovoJson,
                    erroTipoCriarNovoJson,
                    erroVazioCriarNovoJson,
                    erroMsgCriarNovoJson,
                ) = func.isValidInput("Opção desejada: ", "int")

                if criarNovoJson == 1:
                    break
                elif criarNovoJson == 0:
                    print("Programa encerrado.")
                    return
                else:
                    print("Opção inválida. Programa encerrado.")

            # Cria um novo arquivo JSON vazio se não existir
            try:
                with open(self.caminhoCompletoJson, "w", encoding="utf-8") as f:
                    json.dump({}, f, indent=2, ensure_ascii=False)
            except IOError as e:
                print(f"Erro ao criar o arquivo JSON: {e}")
                return

    # ############################ CRUD Json ############################
    # Métodos CRUD (Create, Read, Update, Delete):

    # ---------------------------------------------------------------------------
    ## Create
    def create(self, novoData):
        # Carregar dados do arquivo JSON
        try:
            with open(self.caminhoCompletoJson, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar o arquivo JSON: {e}")
            return

        # Se o Json estiver vazio, inicializa-o conforme a chavePrincipal
        if self.chavePrincipal not in data:
            data[self.chavePrincipal] = []

        # Determinar a próxima Matrícula única e sequencial:
        matriculas = [
            item["matricula"]
            for item in data[self.chavePrincipal]
            if "matricula" in item
        ]
        nova_matricula = max(matriculas) + 1 if matriculas else 1
        novoData["matricula"] = nova_matricula

        # Adicionar novo dado ao cadastro
        data[self.chavePrincipal].append(novoData)

        # Escrever de volta no arquivo JSON
        try:
            with open(self.caminhoCompletoJson, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Erro ao salvar o arquivo JSON: {e}")

    # ---------------------------------------------------------------------------
    ## Função Read
    def read(self, matricula=None):
        # Se não foi passado a matrícula (parâmetro opcional), então retorna todo o JSON
        if matricula is None:
            # Carregar todos os dados do arquivo JSON
            try:
                with open(self.caminhoCompletoJson, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data
            except (IOError, json.JSONDecodeError) as e:
                print(f"Erro ao carregar o arquivo JSON: {e}")
                return None
        else:
            # Carrega somente os dados da matrícula especificada
            try:
                with open(self.caminhoCompletoJson, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # Busca o aluno com a matrícula fornecida
                for aluno in data.get(self.chavePrincipal, []):
                    if aluno.get("matricula") == matricula:
                        return aluno

                # Se nenhum dado for encontrado com a matrícula fornecida
                print(f"Dado com Matrícula {matricula} não encontrado.")
                return None

            except (IOError, json.JSONDecodeError) as e:
                print(f"Erro ao carregar o arquivo JSON: {e}")
                return None

    # ---------------------------------------------------------------------------
    ## Função Update
    # Fluxo: Read data -> Encontra o dado pelo id -> Atualiza o dado no dicionário obtido no Read
    # -> Salvar o novo Json com o dado atualizado (todo o Json é gravado).
    def update(self, matricula, novosDados):
        data = self.read()
        if not data or self.chavePrincipal not in data:
            print("Nenhum dado encontrado para atualizar.")
            return

        dadoEncontrado = False
        for i, item in enumerate(data[self.chavePrincipal]):
            if item.get("matricula") == matricula:
                dadoEncontrado = True
                # Método update: atualiza dados no dicionário passado na posição do index
                # como só tem uma matrícula, então só altera esta.
                data[self.chavePrincipal][i].update(novosDados)
                break

        if dadoEncontrado:
            try:
                with open(self.caminhoCompletoJson, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"\nDado com Matrícula {matricula} atualizado com sucesso.")
            except IOError as e:
                print(f"Erro ao salvar o arquivo JSON: {e}")
        else:
            print(f"Dado com Matrícula {matricula} não encontrado.")

    # ---------------------------------------------------------------------------
    ## Função Delete
    # Fluxo: Read data -> Encontra o dado pelo id -> Apaga dado no dicionário obtido no Read
    # -> Salvar o novo Json com o dado excluído.
    def delete(self, matricula):
        # Carregar dados do arquivo JSON
        data = self.read()

        # Se o Json estiver vazio, msg de "warning"
        if not data or self.chavePrincipal not in data:
            print("Nenhum dado encontrado para deletar.")
            return

        dadoEncontrado = False
        for i, item in enumerate(data[self.chavePrincipal]):
            if item.get("matricula") == matricula:
                dadoEncontrado = True
                nome = item.get("nome")
                del data[self.chavePrincipal][i]
                break

        if dadoEncontrado:
            try:
                with open(self.caminhoCompletoJson, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(
                    f"O Dado {nome} (Matrícula: {matricula}) foi deletado com sucesso."
                )
            except IOError as e:
                print(f"Erro ao salvar o arquivo JSON: {e}")
        else:
            print(f"Dado com a Matrícula {matricula} não foi encontrado.")
