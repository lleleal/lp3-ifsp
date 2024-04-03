# Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta 
# adivinhar a palavra, letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

import random 

words = ['abacate', 'domingos', 'palindromo', 'python', 'javascript']

word = random.choice(words)
print('Seja Bem-Vindo ao Jogo Da Forca')
shot = 0
chance = []

while shot < 5:
        hidden_word = ['_' for _ in word]
        print(" ".join(hidden_word))

        if "".join(hidden_word) == word:
            print("Você acertou!")
            break
        if chance:
            print(f"letras tentadas: {''.join(chance)}")
            wordp = input("digite uma letra: ")

        if wordp not in word:
            shot -= 1
            chance.append(wordp)
            print("letra incorreta!")
        else:
            for i in range(len(word)):
                if word[i] == wordp:
                    hidden_word[i] = wordp
else:
    print(f"Você não tem mais tentativas. A palavra era: {word}")