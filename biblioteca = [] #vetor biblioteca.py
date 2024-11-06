biblioteca = [] #vetor biblioteca

#função de add livro
def adicionar_livro(titulo,autor,genero):
    livro = {'titulo':titulo, 'autor':autor, 'genero':genero, 'disponivel':True}
    biblioteca.append(livro)
    print(f"o livro {titulo} foi adicionado com sucesso!")

#adicionar_livro('assim que acaba', 'luiz francisco', 'drama')
#print(biblioteca)

def remover_livro(titulo):
    for livro in biblioteca:
         if livro['titulo'] == titulo:
            biblioteca.remove(livro)
            print(f"o livro {titulo} foi removido com sucesso!")

def buscar_livro(busca):
    for livro in biblioteca:
        if livro['titulo'] == busca or livro['autor'] == busca or livro['genero'] == busca:
            print("resultado da busca:\n")
            print(f"livro: {livro['titulo']} | autor: {livro['autor']} | genero: {livro['titulo']} - status {livro['disponivel']}")
            return 
        else: 
            print("livro nao encontrado")


def listar_livro():
    if not biblioteca:
        print("nenhum livro encontrado")
    else:
        print("lista de todos os livros:\n")
        for livro in biblioteca:
            if livro['disponivel'] == True:
                status = 'Disponivel'
            else:
                status = 'Indisponível'
            print(f"livro: {livro['titulo']} | autor: {livro['autor']} | genero: {livro['titulo']} - status {status}")

adicionar_livro('carros', 'neves', 'infantil')
adicionar_livro('carros 2', 'neves', 'infantil')
adicionar_livro('carros 3', 'neves', 'infantil')
adicionar_livro('carros 4', 'neves', 'infantil')
adicionar_livro('carros 5', 'neves', 'infantil')
listar_livro()

def mostrar_menu():
    print("OPÇÕES DO SISTEMA DE BIBLIOTECA:")
    print("1. Adicionar livro")
    print("2. Remover livro")
    print("3. Buscar livros")
    print("4. Listar livros")
    print("5> Verificar disponibilidade") #FUNÇÃO IMPLEMENTADA PELOS ALUNOS (EM TESTE)
    print("6. Sair")

while True:
    mostrar_menu()
    escolha = int(input("Escolha uma opção do menu: "))
 
    if escolha == 1:
        titulo = input("Digite o Titulo do Livro: \n")
        autor = input("Digite o nome do autor:\n")
        genero = input("Digite o genero do livro: \n")
        adicionar_livro(titulo, autor, genero)
    elif escolha == 2:
        titulo = input("Digite o Titulo do Livro que deseja remover: \n")
        remover_livro(titulo)
    elif escolha == 3:
        titulo = input("Digite o Titulo do Livro que deseja encontrar: \n")
        buscar_livro(titulo)
    elif escolha == 4:
        titulo = input("Listar todos os livros: \n")
        listar_livros()
    elif escolha == 5:
        titulo = input("Digite o título do livro para verificar disponibilidade:\n ")
        verificar_disponibilidade(titulo)
    elif escolha == 6:
        titulo = input("Emprestimo de livro:\n ")
        #IMPLEMENTAR ESSA FUNÇÃO
        #emprestimo_livro(titulo,autor)
    else:
        print("Fechando o Sistema...")
        break