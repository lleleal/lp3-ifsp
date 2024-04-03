# Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. Informe ao usuário se o palpite 
# está alto ou baixo, até que ele acerte o número.

import random

randomi = random.randint(1,100)
numero = int

while True:
    numero = int(input("Digite um numero de 1 a 100: "))

    if numero > randomi:
        print("Esse número é maior que o número randômico")
    elif numero < randomi:
        print("Esse número é menor que o número randômico")
    else :
        print(f"Esse é o número escolhido, {randomi}")
        break