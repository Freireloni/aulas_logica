Artista = ["Billie Eilish", "Lana Del Rey", "Melanie Martinez", "Taylor Swift"]

print(Artista)
antigo=input("Qual artista deseja substituir?")
outro_artista = input("Quem vai substituir o artista? ")
indice = Artista.index(antigo)
Artista[indice] = outro_artista


print("Artista substituido. A lista agora é: ", Artista )