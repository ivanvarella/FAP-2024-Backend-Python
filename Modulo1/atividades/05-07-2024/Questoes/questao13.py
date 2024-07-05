# Questão 13(Questão 4 da parte 2):
# 4. Implemente uma função que receba uma string contendo números e operações
# matemáticas básicas (+, -, *, /) e retorne o resultado da expressão.


import funcoesSuporte as func

def trataExecutaExpressao(expressao):
    # Só executa os comandos se funcionar, caso contrário faz o except (implementado da forma genérica)
    try:
        # Retira os espaços da expressão matemática
        expressao = ''.join(expressao.split())

        # Usa a função eval (função interna do Python) para avaliar a expressão matemática
        resultado = eval(expressao)
        print(f"\nResultado: {resultado}\n\n")
        return resultado
    except Exception as e:
        print(e)
        return f"Erro ao avaliar a expressão: {e}."

expressao, erroTipoExpressao, erroVazioExpressao, erroMsgExpressao = func.isValidInput("\n\nDigite a expressão matemática: ", "string")

resultado = trataExecutaExpressao(expressao)


#print(resultado)


# Função eval - interna do Python:

# Sintaxe: eval(expression, globals=None, locals=None)
# 	• expression: A string contendo a expressão a ser avaliada.
# 	• globals (opcional): Um dicionário que define o escopo global onde a expressão será avaliada.
# 	• locals (opcional): Um dicionário que define o escopo local onde a expressão será avaliada.


# A função eval recebe uma string como argumento e avalia essa string como uma expressão Python. O resultado da avaliação é retornado.

# Exemplo:
# # Avalia uma expressão matemática
# result = eval("3 + 4 * 2")
# print(result)  # Saída: 11

# Usos Comuns
# 	• Avaliar expressões matemáticas.
# 	• Executar código dinâmico gerado em tempo de execução.

# Perigos do Uso de eval
# A função eval pode ser perigosa se a entrada não for devidamente sanitizada. Isso porque eval executa qualquer código Python, o que pode levar a problemas de segurança, especialmente se a entrada vier de usuários ou fontes não confiáveis.

# Exemplo:
# # Nunca use eval com entradas não confiáveis
# user_input = "__import__('os').system('rm -rf /')"
# eval(user_input)  # Isso pode apagar arquivos do sistema!