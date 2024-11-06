import math
import statistics
import random

def raiz(value):
    return math.sqrt(value)

def fatorial(value):
    return math.factorial(value)

def potencial(value):
    return math.pow(value, 18)

def main():
    numero = random.randint(0,100)
    print("O numero sorteado foi", numero)
    print("A raiz desse numero é", raiz(numero))
    print("O fatorial do numero é", fatorial(numero))
    print("A potencia (10) do numero é:", potencial (numero))
main( )