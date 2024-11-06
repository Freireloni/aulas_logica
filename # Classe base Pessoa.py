# Classe base Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprime_detalhes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Rica(Pessoa):
    def __init__(self, nome, idade, dinheiro):
        super()._init_(nome, idade)
        self.dinheiro = dinheiro

    def faz_compras(self):
        print(f"{self.nome} está comendo comidas caras R$ {self.dinheiro:.2f}")

class Pobre(Pessoa):
    def __init__(self, nome, idade):
        super()._init_(nome, idade)

    def trabalha(self):
        print(f"{self.nome} está trabalhando")

class Miseravel(Pessoa):
    def __init__(self, nome, idade):
        super()._init_(nome, idade)

    def mendiga(self):
        print(f"{self.nome} está mendigando")

pessoa_rica = Rica("Laura", 18, 1000000)
pessoa_rica.imprime_detalhes()
pessoa_rica.faz_compras()

pessoa_pobre = Pobre("Sofia", 25)
pessoa_pobre.imprime_detalhes()
pessoa_pobre.trabalha()

pessoa_miseravel = Miseravel("Pedro", 40)
pessoa_miseravel.imprime_detalhes()
pessoa_miseravel.mendiga()