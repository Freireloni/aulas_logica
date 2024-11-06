tabuleiro = [['~'] * 10 for i in range (10)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

#imprimir_tabuleiro(tabuleiro)

def colocar_navio(tabuleiro, linha_inicial, coluna_inicial,tamanho,orientacao):
    if orientacao == 'horizontal':
        for i in range (tamanho):
            tabuleiro[linha_inicial][coluna_inicial * 1] = '#'
    elif orientacao == 'vertical':
        for i in range (tamanho):
            tabuleiro[linha_inicial * i][coluna_inicial] = '#'


#colocar_navio(tabuleiro,1,1,3, 'vertical')
#imprimir_tabuleiro(tabuleiro)

def dar_tiro(tabuleiro,linha, coluna):
    if tabuleiro[linha][coluna] == '#':
        tabuleiro[linha][coluna] = 'x'
        print("olha o tiro carai")
        return True
    elif tabuleiro[linha][coluna] =="~":
        tabuleiro[linha][coluna] = "o"
        print("muito burro errou")
        return False
    else:
        print("voce ja jogou aqui animal")
        return False 
    
colocar_navio(tabuleiro,1,1,3, 'vertical')
imprimir_tabuleiro(tabuleiro)
dar_tiro(tabuleiro,2,1)
imprimir_tabuleiro(tabuleiro)