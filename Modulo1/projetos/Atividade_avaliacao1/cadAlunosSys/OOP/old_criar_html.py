# Cria o arquivo html ou o altera caso já exista
def gera_html(arquivo_html, chaveJson):
    # Cria uma instância de JsonHandler
    json_handler = JsonHandler(arquivoJson="dados.json", chavePrincipal=chaveJson)

    # Pega todos os dados e "filtra" de acordo com o retorno do chaveJson
    dados = json_handler.read()
    alunos = dados.get("Alunos", [])
    professores = dados.get("Professores", [])

    # Se tiver buscado por Alunos e não existir nenhum
    if chaveJson == "Alunos" and not alunos:
        print("\n\nNenhum Aluno cadastrado.\n\n")
        return

    # Se tiver buscado por Professores e não existir nenhum
    if chaveJson == "Professores" and not professores:
        print("\n\nNenhum Professor cadastrado.\n\n")
        return

    # Se tiver buscado por Dados e não existir nenhum
    if chaveJson == "" and not (alunos or professores):
        print("\n\nNenhum dado cadastrado.\n\n")
        return

    # Criando o arquivo HTML
    with open(arquivo_html, "w", encoding="utf-8") as html_file:
        html_file.write(
            """
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
            <meta charset="utf-8">
            <title>Relatório de Dados</title>
            <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
            header { background-color: #4CAF50; color: white; padding: 10px 0; text-align: center; }
            .container { width: 80%; margin: auto; padding: 20px; }
            .button { background-color: #4CAF50; color: white; border: none; padding: 10px 20px; margin: 10px; cursor: pointer; border-radius: 5px; }
            .button:hover { background-color: #45a049; }
            .section { display: none; margin-bottom: 20px; padding: 20px; border-radius: 5px; background-color: #f4f4f4; }
            .section.active { display: block; }
            .section h2 { color: #333; }
            .item { margin-bottom: 10px; padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: white; }
            .item p { margin: 5px 0; }
            .item hr { margin: 10px 0; }
            </style>
            <script>
            function showSection(sectionId) {
                var sections = document.querySelectorAll('.section');
                sections.forEach(function(section) {
                    section.classList.remove('active');
                });
                var section = document.getElementById(sectionId);
                if (section) {
                    section.classList.add('active');
                } else {
                    console.warn('Elemento com ID "' + sectionId + '" não encontrado.');
                }
            }
            window.onload = function() {
                var defaultSection = document.querySelector('.button').getAttribute('data-target');
                if (defaultSection) {
                    showSection(defaultSection);
                }
            }
            </script>
            </head>
            <body>
            <header>
                <h1>Relatório de Dados</h1>
            </header>
            <div class="container">
                <button class="button" data-target="alunosSection" onclick="showSection('alunosSection')">Mostrar Alunos</button>
                <button class="button" data-target="professoresSection" onclick="showSection('professoresSection')">Mostrar Professores</button>
                <button class="button" data-target="allSection" onclick="showSection('allSection')">Mostrar Todos</button>
        """
        )

        # Para alunos
        if chaveJson == "Alunos" and alunos:
            html_file.write(
                """
                <div id="alunosSection" class="section">
                    <h2>Lista de Alunos</h2>
                    <p>Total de alunos cadastrados: {}</p>
                """.format(
                    len(alunos)
                )
            )

            for aluno in alunos:
                media_notas = Aluno.calcular_media(aluno["notas"])
                html_file.write(
                    """
                    <div class="item">
                        <p><strong>Matrícula:</strong> {}</p>
                        <p><strong>Nome:</strong> {}</p>
                        <p><strong>Curso:</strong> {}</p>
                        <p><strong>Notas:</strong> {}</p>
                        <p><strong>Média das notas:</strong> {:.1f}</p>
                        <p><strong>Presenças:</strong> {}</p>
                        <p><strong>Telefone:</strong> {}</p>
                        <p><strong>Email:</strong> {}</p>
                        <hr>
                    </div>
                    """.format(
                        aluno["matricula"],
                        aluno["nome"],
                        aluno["curso"],
                        ", ".join(map(str, aluno["notas"])),
                        media_notas,
                        aluno["presencas"],
                        aluno["telefone"],
                        aluno["email"],
                    )
                )
            html_file.write("</div>")

        # Para professores
        if chaveJson == "Professores" and professores:
            html_file.write(
                """
                <div id="professoresSection" class="section">
                    <h2>Lista de Professores</h2>
                    <p>Total de Professores cadastrados: {}</p>
                """.format(
                    len(professores)
                )
            )

            for professor in professores:
                html_file.write(
                    """
                    <div class="item">
                        <p><strong>Matrícula:</strong> {}</p>
                        <p><strong>Nome:</strong> {}</p>
                        <p><strong>Disciplinas:</strong> {}</p>
                        <p><strong>Turmas:</strong> {}</p>
                        <p><strong>Telefone:</strong> {}</p>
                        <p><strong>Email:</strong> {}</p>
                        <hr>
                    </div>
                    """.format(
                        professor["matricula"],
                        professor["nome"],
                        professor["disciplinas"],
                        professor["turmas"],
                        professor["telefone"],
                        professor["email"],
                    )
                )
            html_file.write("</div>")

        # Para todos os dados
        if chaveJson == "":
            if alunos:
                html_file.write(
                    """
                    <div id="allSection" class="section">
                        <h2>Lista de Alunos</h2>
                        <p>Total de alunos cadastrados: {}</p>
                    """.format(
                        len(alunos)
                    )
                )
                for aluno in alunos:
                    media_notas = Aluno.calcular_media(aluno["notas"])
                    html_file.write(
                        """
                        <div class="item">
                            <p><strong>Matrícula:</strong> {}</p>
                            <p><strong>Nome:</strong> {}</p>
                            <p><strong>Curso:</strong> {}</p>
                            <p><strong>Notas:</strong> {}</p>
                            <p><strong>Média das notas:</strong> {:.1f}</p>
                            <p><strong>Presenças:</strong> {}</p>
                            <p><strong>Telefone:</strong> {}</p>
                            <p><strong>Email:</strong> {}</p>
                            <hr>
                        </div>
                        """.format(
                            aluno["matricula"],
                            aluno["nome"],
                            aluno["curso"],
                            ", ".join(map(str, aluno["notas"])),
                            media_notas,
                            aluno["presencas"],
                            aluno["telefone"],
                            aluno["email"],
                        )
                    )
                html_file.write("</div>")

            if professores:
                html_file.write(
                    """
                    <div id="allSection" class="section">
                        <h2>Lista de Professores</h2>
                        <p>Total de Professores cadastrados: {}</p>
                    """.format(
                        len(professores)
                    )
                )
                for professor in professores:
                    html_file.write(
                        """
                        <div class="item">
                            <p><strong>Matrícula:</strong> {}</p>
                            <p><strong>Nome:</strong> {}</p>
                            <p><strong>Disciplinas:</strong> {}</p>
                            <p><strong>Turmas:</strong> {}</p>
                            <p><strong>Telefone:</strong> {}</p>
                            <p><strong>Email:</strong> {}</p>
                            <hr>
                        </div>
                        """.format(
                            professor["matricula"],
                            professor["nome"],
                            professor["disciplinas"],
                            professor["turmas"],
                            professor["telefone"],
                            professor["email"],
                        )
                    )
                html_file.write("</div>")

        html_file.write("</div></body></html>")
