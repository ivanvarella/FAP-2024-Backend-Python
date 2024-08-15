from empregado import Empregado


def main():
    print("-" * 40)

    # Criar instâncias da classe Empregado
    print("Criando empregados...")
    empregado1 = Empregado("João", 30, 5000, "Analista de Sistemas")
    empregado2 = Empregado("Maria", 28, 6000, "Desenvolvedora")
    empregado3 = Empregado("Pedro", 35, 7000, "Gerente de Projetos")

    print("-" * 40)

    # Exibir informações dos empregados
    print("Exibindo informações dos empregados:")
    print(empregado1)
    print(empregado2)
    print(empregado3)

    print("-" * 40)

    # Exibir ações dos empregados
    print("Empregado 1 realizando trabalho:")
    empregado1.trabalhar()

    print("Empregado 2 recebendo salário:")
    empregado2.receber_salario()

    print("-" * 40)

    # Testar demissão
    print("Demissão do empregado 3:")
    empregado3.demitir()
    print(empregado3)  # Após a demissão, cargo e salário devem ser None

    print("-" * 40)

    # Recontratar um empregado
    print("Recontratando o empregado 3...")
    empregado3.contratar("Consultor", 8000)
    print(empregado3)

    print("-" * 40)

    # Testar promoção
    print("Promovendo o empregado 3...")
    empregado3.promover("Gerente Sênior", 9000)
    print(empregado3)

    print("-" * 40)

    # Testar cenários de erro
    print("Tentando realizar trabalho após demissão do empregado 3:")
    empregado3.trabalhar()

    print("Tentando receber salário após demissão do empregado 3:")
    empregado3.receber_salario()

    print("-" * 40)


main()
