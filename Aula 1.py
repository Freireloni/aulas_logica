class Perfil(object):
    def __init__(self, nome, telefone, empresa):
        self.nome = nome 
        self.telefone = telefone 
        self.empresa = empresa 
        self.curtidas = 0 

    def imprimir(self):
        print(f"nome : {self.nome}, Telefone {self.telefone}, Empresa")
         
            