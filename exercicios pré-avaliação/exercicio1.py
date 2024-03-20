# Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. Informe ao usuário se o palpite 
# está alto ou baixo, até que ele acerte o número.

import random

random = random.randint(1,100)
numero = int

while True :
    numero != random 
    numero = int(input("Digite um número aleatório de de 1 a 100:"))

    if numero <= 0 and numero >= 100 :
        print("Esse número não é válido")
        continue

    if numero > random :
        print("Esse número é maior que o número surpresa")
    elif numero < random :
        print("Esse número é menor que o número surpresa")
    else :
        print("Esse é o número escolhido")
        break