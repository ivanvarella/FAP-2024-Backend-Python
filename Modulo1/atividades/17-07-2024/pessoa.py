import datetime

anoAtual = datetime.date.today().year

class Pessoa:
    anoAtual = datetime.date.today().year

    def __init__(self, nome, nasc, cpf, conversando = False, comendo = False, ):
        self.nome = nome
        self.nasc = nasc
        self.cpf = cpf
        self.comendo = comendo
        self.conversando = conversando
    
    def qualIdade(self):
        return anoAtual - self.nasc
    
    def comer(self, alimento):
        if self.comendo: #self.comendo == True
            print(f"{self.nome} não pode comer pois já está comendo.")
            return
        
        if self.conversando:
            print(f"{self.nome} não pode comer pois está conversando.")
            return
        
        print(f"{self.nome} está comendo {alimento}.")
        self.comendo = True
        return

    def conversar(self, assunto):
        if self.conversando:
            print(f"{self.nome} já está conversando.")
            return
        
        if self.comendo:
            print(f"{self.nome} não pode conversar pois está comendo.")
            return

        self.conversando = True
        print(f"{self.nome} está conversando sobre {assunto}.")
        return
    
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} já não estava comendo.")
            return
    
        self.comendo = False
        print(f"{self.nome} parou de comer.")
        return
    
    def parar_conversar(self):
        if not self.conversando:
            print(f"{self.nome} já não estava conversando.")
            return
        
        self.conversando = False
        print(f"{self.nome} parou de conversar.")
        return