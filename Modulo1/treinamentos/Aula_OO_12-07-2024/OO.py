class Animal:
  def __init__(self, nome, peso, familia):
      self.nome = nome
      self.peso = peso
      self.familia = familia
      if peso <= 50:
          self.tamanho = "Pequeno"
      elif peso <= 100:
          self.tamanho = "Médio"
      elif peso > 100:
          self.tamanho = "Grande"

      print("Animal Criado")

  # Métodos:
  def speak(self):
      print("Animal Speaking")

  def eat(self):
      print("Animal Eating")

  def sleep(self):
      print("Animal Sleeping")
  
  def apresentacao(self):
      print(f"Olá, eu sou {self.nome} da família {self.familia}")
            
  #Dunder Method (double underscore):
  def __str__(self):
      return f"Nome: {self.nome}, Peso: {self.peso}, Família: {self.familia}"

  def __len__(self):
      return self.peso

  def __del__(self):
      print("Objeto Animal Destruído")

  def __add__(self, other):
      return self.peso + other.peso
  
  def __lt__(self, other):
      return self.peso < other.peso
  
  def __gt__(self, other):
      return self.peso > other.peso
  
  def __eq__(self, other):
      return self.peso == other.peso

  def __ne__(self, other):
      return self.peso != other.peso
  
  def __le__(self, other):
      return self.peso <= other.peso
  
  def __ge__(self, other):
      return self.peso >= other.peso
  
  def __bool__(self):
      return bool(self.peso)
  
  def __contains__(self, item):
      return item in self.nome
  
  def __getitem__(self, index):
      return self.nome[index]
  
  def __setitem__(self, index, value):
      self.nome[index] = value

    
# Classe filha:
class Dog(Animal):
  def __init__(self, nome, peso):
      super().__init__(nome, peso, "Canino")
      print("Dog Criado")

  def speak(self):
      print("Dog Speaking")

animal1 = Animal("Leão", 50, "Mamifero")

animal2 = Animal("Tigre", 120, "Mamifero")

cachorro = Dog("Toby", 30)

print(animal1.nome, " - ", animal1.peso, " - ", animal1.familia, " - ", animal1.tamanho,)

animal1.speak()

cachorro.speak()

print(animal2.nome, " - ", animal2.peso, " - ", animal2.familia, " - ", animal2.tamanho)
