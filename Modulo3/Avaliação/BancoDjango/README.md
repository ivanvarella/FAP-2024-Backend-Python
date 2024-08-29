<div align="center" style="padding-top: 20px;">
  
# Projeto Django Old Bank

## Este projeto implementa uma aplicação web construída com Django simular o funcionamento simples de contas bancárias.

</div>


## Índice
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Observações](#observações)
- [Dependências](#dependências)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Telas de exemplo do projeto](#telas-de-exemplo-do-projeto)

## Funcionalidades

- **Cadastro e edição de usuários**
- **Gerenciamento de sessão dos usuários (autenticação Django)**
- **Sistema de autenticação de usuários**
- **Gerenciamento de permissões de acesso e modificações no sistema**
- **Criação de novas contas bancárias para os usuários**
- **Listagem, edição e encerramento de contas**
- **Registro das operações bancárias (Criação de contas, depósitos, saques, transferências (pendente), extratos, grafico de médias de saldos e movimentações, filtragem das operações por período e por tipo de operação)**


## Tecnologias Utilizadas

- **Python 3.x**
- **Django 5.x**
- **MySQL (WorkBench)**
- **Bootstrap 5**
- **Javascript**
- **Material UI (Ícones)**
- **Git & GitHub**

## Como Executar o Projeto

1. **Clone o repositório**  
   Este projeto não possui um repositório específico, ele está dentro de um repositório geral do curso.

2. **Crie um ambiente virtual**
   ```bash
   python3 -m venv env
   source env/bin/activate

3. **Instale as dependências**
 ```bash
 pip install -r requirements.txt
  ```

4. **Configure as configurações do banco de dados**  
    Configure as configurações do banco de dados no arquivo settings.py.

5. **Crie as tabelas do banco de dados**
   ```bash
    python manage.py makemigrations
    python manage.py migrate

6. **Inicie o servidor**
    ```bash
    python manage.py runserver

7. **Acesse a aplicação**  
   Abra o seu navegador e acesse: http://127.0.0.1:8000/tarefas/

## Observações

- Este projeto é um exemplo simples para fins de estudo.
- É importante implementar medidas de segurança adicionais para proteger os dados dos usuários em um ambiente real.
- Adapte o projeto de acordo com as suas necessidades e requisitos.

## Dependências

- `asgiref==3.8.1`: Framework ASGI para Django.
- `Django==5.1`: Framework Django para desenvolvimento web.
- `django-dump-die==0.1.7`: Ferramenta para debugging.
- `sqlparse==0.5.1`: Ferramenta para formatação e análise de SQL.
- `typing_extensions==4.12.2`: Extensões para o módulo typing.

## Estrutura do Repositório
```plaintext
Proj_Mod.1_2/
├── README.md
├── db.sqlite3
├── requirements.txt
├── manage.py
├── Info
├── core/
├── usuarios/
├── tarefas/
├── media/
├── templates/
└── venv/
```

## Telas de exemplo do projeto
<table align="center">
  <tr>
    <td>
      <a href="Info/imgSys/Login.jpg" target="_blank">
        <img src="Info/imgSys/Login.jpg" alt="Imagem 1" width="200"/>
      </a>
    </td>
    <td>
      <a href="Info/imgSys/Editar_user.jpg" target="_blank">
        <img src="Info/imgSys/Editar_user.jpg" alt="Imagem 2" width="200"/>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="Info/imgSys/listar_tarefas.jpg" target="_blank">
        <img src="Info/imgSys/listar_tarefas.jpg" alt="Imagem 3" width="200"/>
      </a>
    </td>
    <td>
      <a href="Info/imgSys/Cadastrar_tarefa.jpg" target="_blank">
        <img src="Info/imgSys/Cadastrar_tarefa.jpg" alt="Imagem 4" width="200"/>
      </a>
    </td>
  </tr>
</table>