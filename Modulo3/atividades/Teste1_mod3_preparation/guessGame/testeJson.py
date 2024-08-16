import json
import logging
import os

# Para debugg - Está salvando duplicado no Json
import logging
# Configurar logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Caminho do diretório atual
caminho = os.getcwd() + "/Modulo1/atividades/19-06-2024/guessGame/recordes.json"




# Função para gravar novo recorde
def adicionaRecorde(novoRecorde):
  logging.debug('Iniciando função adicionaRecorde...')
  # Carregar dados do arquivo JSON
  with open(caminho, 'r', encoding='utf-8') as f:
    data = json.load(f)

  # Se o campo 'Recordes' não existir, inicializa-o como uma lista vazia
  if 'Recordes' not in data:
    data['Recordes'] = []

  # Adicionar novo recorde à lista de recordes
  data['Recordes'].append(novoRecorde)

  # Escrever de volta no arquivo JSON
  with open(caminho, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

    # Forçar a escrita imediata dos dados para o arquivo
    f.flush()
  logging.debug('Registro adicionado com sucesso.')


# Teste add recorde:
novoRecorde = {
    "nome": "Nome Jogar teste",
    "tentativas": 400,
    "tempo": "05:15:37",
    "data": "18-06-2024",
    "hora": "15:30"
}

adicionaRecorde(novoRecorde)