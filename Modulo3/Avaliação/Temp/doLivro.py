# Como o programa do Banco Tatu vai ficar maior que os programas que já trabalhamos até aqui,
# vamos gravar cada classe em um arquivo .py separado.

# Como estou usando o Jupyter Notebook, manterei todo o código em um só bloco, fazendo as
# devidas alterações para o programa funcione.


# Listagem 10.4 – Classe Clientes (clientes.py)
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


# Listagem 10.6 – Classe Conta (contas.py)
class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.número = número
        self.operações = []
        if saldo > 0:
            self.operações.append(["DEPÓSITO INICIAL", saldo])

    def resumo(self):
        print("CC Número: %s Saldo: R$%10.2f" % (self.número, self.saldo))
        for cliente in self.clientes:
            print(f"Cliente: {cliente.nome} - Telefone: {cliente.telefone}")

    def verifica_se_pode_sacar(self, valor):
        return self.saldo >= valor

    def saque(self, valor):
        pode_sacar = self.verifica_se_pode_sacar(valor)
        if pode_sacar:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print(
                f"Tentativa de saque no valor de R${valor} sem sucesso, o saldo é insuficiente."
            )
            print(f"O saldo atual é de R${self.saldo} reais.")

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])
        print(f"Depósito de R${valor} realizado com sucesso.")

    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s R$%10.2f" % (o[0], o[1]))
        print("\nSaldo atual: R$%10.2f\n" % self.saldo)


# Listagem 10.9 – Classe Banco (bancos.py)
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abre_conta(self, conta):
        self.contas.append(conta)

    def lista_contas(self):
        for c in self.contas:
            c.resumo()


# Listagem 10.11 – Uso de herança para definir ContaEspecial
class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        super().__init__(clientes, número, saldo)
        self.limite = limite

    def verifica_se_pode_sacar(self, valor):
        return self.saldo + self.limite >= valor

    def saque(self, valor):
        pode_sacar = self.verifica_se_pode_sacar(valor)
        if pode_sacar:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True
        else:
            print(
                f"Tentativa de saque no valor de R${valor} sem sucesso, o saldo é insuficiente."
            )
            print(f"O saldo atual é de R${self.saldo} reais.")
            return False

    def extrato(self):
        print(f"Extrato CC N° {self.número}\n")
        for o in self.operações:
            print(f"{o[0]:10} R${o[1]:10.2f}")
        print(f"\nSaldo atual: R${self.saldo:10.2f}")
        print(f"Limite da conta especial (cheque-especial): R${self.limite:10.2f}")
        print(
            f"Total disponível para saque (saldo + limite): R${(self.saldo + self.limite):10.2f}\n"
        )


# Listagem 10.13 – Classe ListaÚnica (listaunica.py)
class ListaÚnica:
    def __init__(self, elem_class):
        self.lista = []
        self.elem_class = elem_class

    def __len__(self):
        return len(self.lista)

    def __iter__(self):
        return iter(self.lista)

    def _getitem__(self, p):
        return self.lista[p]

    def indiceVálido(self, i):
        return i >= 0 and i < len(self.lista)

    def adiciona(self, elem):
        if self.pesquisa(elem) == -1:
            self.lista.append(elem)

    def remove(self, elem):
        self.lista.remove(elem)

    def pesquisa(self, elem):
        self.verifica_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError:
            return -1

    def verifica_tipo(self, elem):
        if type(elem) != self.elem_class:
            raise TypeError("Tipo inválido")

    def ordena(self, chave=None):
        self.lista.sort(key=chave)


# Listagem 10.14 – Classe Nome (nome.py)
# class Nome:
#     def __init__(self, nome):
#         if nome == None or not nome.strip():
#             raise ValueError("Nome não pode ser nulo nem em branco")
#         self.nome = nome
#         self.chave = nome.strip().lower()

#     def __str__(self):
#         return self.nome

#     def __repr__(self):
#         return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(
#             id(self),
#             self.nome,
#             self.chave,
#             type(self).__name__
#         )

#     def __eq__(self, outro):
#         print("__eq__ Chamado")
#         return self.nome == outro.nome

#     def __lt__(self, outro):
#         print("__lt__ Chamado")
#         return self.nome < outro.nome


# Listagem 10.15 – Usando anotações (nome.py)
# from functools import total_ordering
# @total_ordering
# class Nome:
#     def __init__(self, nome):
#         if nome == None or not nome.strip():
#             raise ValueError("Nome não pode ser nulo nem em branco")
#         self.nome = nome
#         self.chave = Nome.CriaChave(nome)

#     def __str__(self):
#         return self.nome

#     def __repr__(self):
#         return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(
#             id(self),
#             self.nome,
#             self.chave,
#             type(self).__name__
#         )

#     def __eq__(self, outro):
#         print("__eq__ Chamado")
#         return self.nome == outro.nome

#     def __lt__(self, outro):
#         print("__lt__ Chamado")
#         return self.nome < outro.nome

#     @staticmethod
#     def CriaChave(nome):
#         return nome.strip().lower()


# Listagem 10.16 – Classe Nome com propriedades (nome.py)
# from functools import total_ordering
# @total_ordering
# class Nome:
#     def __init__(self, nome):
#         self.nome = nome

#     def __str__(self):
#         return self.nome

#     def __repr__(self):
#         return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(
#             id(self), self.__nome, self.__chave, type(self).__name__
#         )

#     def __eq__(self, outro):
#         return self.nome == outro.nome

#     def __lt__(self, outro):
#         return self.nome < outro.nome

#     @property
#     def nome(self):
#         return self.__nome

#     @nome.setter
#     def nome(self, valor):
#         if valor == None or not valor.strip():
#             raise ValueError("Nome não pode ser nulo nem em branco")
#         self.__nome = valor
#         self.__chave = Nome.CriaChave(valor)

#     @staticmethod
#     def CriaChave(nome):
#         return nome.strip().lower()


# Listagem 10.17 – Chave como propriedade apenas para leitura (nome.py)
from functools import total_ordering


@total_ordering
class Nome:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(
            id(self), self.__nome, self.__chave, type(self).__name__
        )

    def __eq__(self, outro):
        return self.nome == outro.nome

    def __lt__(self, outro):
        return self.nome < outro.nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if valor == None or not valor.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)

    @property
    def chave(self):
        return self.__chave

    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()


# Listagem 10.18 – A classe TipoTelefone
from functools import total_ordering


@total_ordering
class TipoTelefone:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return "({0})".format(self.tipo)

    def __eq__(self, outro):
        if outro is None:
            return False
        return self.tipo == outro.tipo

    def __lt__(self, outro):
        return self.tipo < outro.tipo


# Listagem 10.19 – A classe Telefone
class Telefone:
    def __init__(self, número, tipo=None):
        self.número = número
        self.tipo = tipo

    def __str__(self):
        if self.tipo != None:
            tipo = self.tipo
        else:
            tipo = ""
        return "{0} {1}".format(self.número, tipo)

    def __eq__(self, outro):
        return self.número == outro.número and (
            (self.tipo == outro.tipo) or (self.tipo == None or outro.tipo == None)
        )

    @property
    def número(self):
        return self.__número

    @número.setter
    def número(self, valor):
        if valor == None or not valor.strip():
            raise ValueError("Número não pode ser None ou em branco")
        self.__número = valor


# Listagem 10.20 – Classe DadoAgenda
# import listaunica # Está lá em cima!!!!


class Telefones(ListaÚnica):
    def __init__(self):
        super().__init__(Telefone)


class DadoAgenda:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = Telefones()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if type(valor) != Nome:
            raise TypeError("nome deve ser uma instância da classe Nome")
        self.__nome = valor

    def pesquisaTelefone(self, telefone):
        posição = self.telefones.pesquisa(Telefone(telefone))
        if posição == -1:
            return None
        else:
            return self.telefones[posição]


# Listagem 10.21 – Listagem parcial do programa da agenda
class TiposTelefone(ListaÚnica):
    def __init__(self):
        super().__init__(TipoTelefone)


class Agenda(ListaÚnica):
    def __init__(self):
        super().__init__(DadoAgenda)
        self.tiposTelefone = TiposTelefone()

    def adicionaTipo(self, tipo):
        self.tiposTelefone.adiciona(TipoTelefone(tipo))

    def pesquisaNome(self, nome):
        if type(nome) == str:
            nome = Nome(nome)
        for dados in self.lista:
            if dados.nome == nome:
                return dados
        else:
            return None

    def ordena(self):
        super().ordena(lambda dado: str(dado.nome))


# Listagem 10.22 – Listagem parcial da agenda: classe Menu
class Menu:
    def __init__(self):
        self.opções = [["Sair", None]]

    def adiciona_opção(self, nome, função):
        self.opções.append([nome, função])

    def exibe(self):
        print("====")
        print("Menu")
        print("====\n")
        for i, opção in enumerate(self.opções):
            print("[{0}] - {1}".format(i, opção[0]))
        print()

    def execute(self):
        while True:
            self.exibe()
            escolha = valida_faixa_inteiro(
                "Escolha uma opção: ", 0, len(self.opções) - 1
            )
            if escolha == 0:
                break
            self.opções[escolha][1]()


# joão=Cliente("João da Silva", "777-1234")
# conta1=Conta([joão], 1, 1000)
# conta2=ContaEspecial([joão], 2, 500, 1000) # Conta especial -> Limite = 1000
# conta2.deposito(300)
# sacou2 = conta1.saque(190)
# conta2.deposito(95.15)
# sacou3 = conta2.saque(2000)
# print(f"Return do saque: {sacou3}")
# conta1.extrato()
# conta2.extrato()
