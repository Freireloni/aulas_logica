#Classe Imovel
class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def get_endereco(self):
        return self.endereco

    def get_preco(self):
        return self.preco

    def imprime_detalhes(self):
        print(f"Endereço: {self.endereco}, Preço: R$ {self.preco:.2f}")

class Novo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super()._init_(endereco, preco)
        self.adicional = adicional
    def get_adicional(self):
        return self.adicional
    def imprime_adicional(self):
        print(f"Adicional para imóvel novo: R$ {self.adicional:.2f}")
    def get_preco_total(self):
        return self.preco + self.adicional
    def imprime_detalhes(self):
        print(f"Endereço: {self.endereco}, Preço base: R$ {self.preco:.2f}, Preço total com adicional: R$ {self.get_preco_total():.2f}")

class Velho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super()._init_(endereco, preco)
        self.desconto = desconto
    def get_desconto(self):
        return self.desconto
    def imprime_desconto(self):
        print(f"Desconto para imóvel velho: R$ {self.desconto:.2f}")
    def get_preco_total(self):
        return self.preco - self.desconto
    def imprime_detalhes(self):
        print(f"Endereço: {self.endereco}, Preço base: R$ {self.preco:.2f}, Preço total com desconto: R$ {self.get_preco_total():.2f}")

imovel_novo = Novo("Rua cesar augusto, 263", 500000, 50000)
imovel_novo.imprime_detalhes()
imovel_novo.imprime_adicional()

imovel_velho = Velho("Av. galeao coutinho, 1236", 300000, 30000)
imovel_velho.imprime_detalhes()
imovel_velho.imprime_desconto()