#Classe Animal
class Animal:
    def __init_(self, nome, raca):
        self.nome = nome
        self.raca = raca
    def caminha(self):
        return "O animal está caminhando"

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super()._init_(nome, raca)
    def late(self):
        return "O cachorro está latindo"

class Gato(Animal):
    def __init__(self, nome, raca):
        super()._init_(nome, raca)
    def mia(self):
        return "O gato está miando"

cachorro = Cachorro("thor", "vira lata")
print(cachorro.late())
print(cachorro.caminha())
print(cachorro.nome)
print(cachorro.raca)

gato = Gato("Frida", "Maine Coon")
print(gato.mia())
print(gato.caminha())
print(gato.nome)
print(gato.raca)