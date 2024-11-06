#Quartos de hotel
matriz= [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

while True:
    andar = int (input("Qual andar fica o andar?"))
    quarto = int(input("Qual o numero do quarto?"))

    reserva = matriz[quarto-1][andar-1]

    if reserva != 0:
        print("quarto reservado")
    else:
        print("quarto disponivel")
        print("farei uma reserva")
        matriz[quarto-1][andar-1] = 1
        print("o quarto foi reservado!")

    #Debug
    print(reserva) 