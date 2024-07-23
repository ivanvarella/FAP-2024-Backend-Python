# Testa a classe JsonHandler
from jsonHandler import JsonHandler
import json

# Define o nome do arquivo JSON e a chave principal
nome_arquivo_json = "testeClass_HandleJson.json"
chave_principal = "Alunos"

# Cria uma instância da classe JsonHandler
handler = JsonHandler(nome_arquivo_json, chave_principal)

# Cria o arquivo JSON e inicializa com dados
handler.verificar_e_inicializar_json()

# Testa a função create
novo_aluno = {
    "matricula": None,  # Somente para a matrícula ser o primeiro dado, pois é gerado dentro da Classe
    "nome": "Ana Beatriz",
    "curso": "Matemática",
    "notas": [7.5, 8.0, 9.0],
    "presencas": 22,
    "telefone": "3210-5678",
    "email": "ana.beatriz@email.com",
}

novo_aluno2 = {
    "matricula": None,
    "nome": "Gogofredo Gois",
    "curso": "Linguas estragueiras",
    "presencas": 31,
    "telefone": "654321654654",
    "email": "gogo@teste.com.br",
    "notas": [10.0, 8.0, 9.0, 8.0, 7.0, 8.0, 8.0, 9.0, 8.0, 10.0],
}

novo_aluno3 = {
    "matricula": None,
    "nome": "Raquel Dias",
    "curso": "Python Ultra Mega Avançado para Iniciantes",
    "presencas": 15,
    "telefone": "56498731",
    "email": "raquel_do_python@gmail.com",
    "notas": [10, 9.5, 9.8],
}

print("Adicionando um novo aluno...")
handler.create(novo_aluno)

print("Adicionando um novo aluno...")
handler.create(novo_aluno2)

print("Adicionando um novo aluno...")
handler.create(novo_aluno3)

# Testa a função read
print("\nLendo dados do arquivo JSON...")
dados = handler.read()

# Exibe todos os alunos
if chave_principal in dados:
    print(f"Alunos ({len(dados[chave_principal])} encontrados):")
    for aluno in dados[chave_principal]:
        print(json.dumps(aluno, indent=2, ensure_ascii=False))
else:
    print("Nenhum dado encontrado.")

# Testa a função update
print(
    "\nAtualizando dados do aluno com matrícula 2 (O segundo dado criado anteriormente)..."
)
novos_dados = {
    "nome": "Gogofredo Gogozinho Gois de Goias",
    "curso": "Física Quântica Avançada para estudantes de Letras",
}
handler.update(2, novos_dados)

# Tenta acessar um dado inexistente - Read
print("\nTentando acessar um dado inexistente (matrícula 10000)...")
dado_inexistente = handler.read(10000)

# Testa função update em um dado inexistente
print("\nTentando atualizar um dado inexistente (matrícula 10000)...")
novos_dados_inexistentes = {
    "nome": "Teste testestestes",
    "curso": "Curso de programação",
}
handler.update(10000, novos_dados_inexistentes)


# Testa a função delete
print("\nDeletando o aluno com matrícula 3...")
handler.delete(3)

# Tenta deletar um dado inexistente
print("\nTentando deletar um dado inexistente (matrícula 10000)...")
handler.delete(10000)

# Exibe os dados após as operações
print("\nDados finais no arquivo JSON...")
dados_finais = handler.read()

# Exibe todos os alunos finais
if chave_principal in dados_finais:
    print(f"Dados finais ({len(dados_finais[chave_principal])} encontrados):")
    for aluno in dados_finais[chave_principal]:
        print(json.dumps(aluno, indent=2, ensure_ascii=False))
else:
    print("Nenhum dado encontrado.")
