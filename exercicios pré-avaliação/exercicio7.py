# Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta 
# adivinhar a palavra, letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'computador', 'algoritmo', 'dados', 'inteligencia']
    return random.choice(palavras)

def main():
    palavra = escolher_palavra()
    tentativas_maximas = 6
    letras_corretas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Tente adivinhar a palavra secreta.")

    while tentativas_maximas > 0:
        palavra_oculta = ''.join(letra if letra in letras_corretas else '_' for letra in palavra)
        print("\nPalavra secreta:", palavra_oculta)
        print("Tentativas restantes:", tentativas_maximas)
        
        if palavra_oculta == palavra:
            print("\nParabéns! Você adivinhou a palavra secreta:", palavra)
            break

        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if letra in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_corretas.append(letra)
        else:
            tentativas_maximas -= 1
            print("Letra incorreta. Tente novamente.")

    else:
        print("\nVocê perdeu! A palavra secreta era:", palavra)

if __name__ == "__main__":
    main()