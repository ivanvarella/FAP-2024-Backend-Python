##### FAP Backend Python - Turma 17 ####
##### Ivan Varella ####

# Observações:
# Para o funcionamento dos códigos é necessário a instalação das bibliotecas abaixo:
# Windows:
# - OpenAI: pip install openai
# - dotenv (para gerenciar variáveis de ambiente): pip install python-dotenv
# Linux: 
# - OpenAI: sudo pip3 install openai
#   Entre com a sua senha de usuário
# - dotenv (para gerenciar variáveis de ambiente): sudo pip3 install python-dotenv
#   Entre com a sua senha de usuário
#
# Além disso, é necessário criar sua conta na plataforma da OpenAI no link: https://platform.openai.com/api-keys
# Após isso, faça login, vá na seção "API Keys" e crie uma nova KEY em "Create new secret key".
# Com posse da KEY, crie um arquivo ".env" e adicione a linha de código: OPENAI_API_KEY=your_api_key_here
#
# Essa KEY é individual e não deve ser compartilhada, por isso o arquivo .env relativo a esse "projeto" foi inserido ao .gitignore e não será compartilhado.
# Mas você pode utilziar os códigos utlizando sua própria KEY como mostrado acima.


# Importação das bibliotecas
import openai
from dotenv import load_dotenv
import os

# Carrega a chave do arquivo .env:
load_dotenv()

# Chave de API da OpenAI
api_key = os.getenv("OPENAI_API_KEY")

# Verifica se a chave de API foi carregada corretamente
if api_key is None:
    raise ValueError("API Key not found. Make sure to set OPENAI_API_KEY in your .env file.")

# Configuração da chave de API no módulo openai
openai.api_key = api_key

# Função que recebe o prompt (interação) e retorna a resposta do ChatGPT
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        #model="text-davinci-003",  # Escolha o modelo adequado - descontinuado
        model="gpt-3.5-turbo-instruct", # Testar - excedi minha cota diária 
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response['choices'][0]['text'].strip()

# Gerencia a interação com o ChatGPT:
if __name__ == "__main__":
    # Loop infinito para manter o chat funcionando
    while True:
        # Pergunta para o usuário
        user_input = input("Digite sua pergunta (ou 'sair' para encerrar): ")
        if user_input.lower() == "sair":
            print("\nEncerrando o chat. Até a próxima!\n\n")
            break
        # Resposta do ChatGPT
        response = chat_with_gpt(user_input)
        # Imprime a resposta
        print("ChatGPT: ", response)


# Parametros do método Completion.create() da biblioteca openai:
#
# Exemplo:
# response = openai.Completion.create(
#     engine="text-davinci-003",
#     prompt=prompt,
#     max_tokens=150,
#     n=1,
#     stop=None,
#     temperature=0.7,
#   )
#
# model: Especifica o modelo de linguagem a ser usado. No exemplo, "text-davinci-003" refere-se ao modelo Davinci, uma versão específica do ChatGPT.
# prompt: É o texto de entrada que você fornece ao modelo para gerar uma resposta. Pode ser uma pergunta, uma declaração inicial, ou qualquer texto que você deseje que o ChatGPT continue.
# max_tokens: Define o número máximo de tokens (unidades básicas de texto) na resposta gerada. Isso controla o comprimento da resposta.
# n: Define quantas respostas diferentes o modelo deve gerar para o prompt fornecido. No caso de n=1, o modelo gera apenas uma resposta.
# stop: Um token de parada opcional que pode ser usado para indicar ao modelo quando parar de gerar texto. Se None, o modelo gera texto até atingir max_tokens.
# temperature: Controla a aleatoriedade das previsões do modelo. Um valor mais alto aumenta a aleatoriedade, enquanto um valor mais baixo torna as previsões mais previsíveis.
