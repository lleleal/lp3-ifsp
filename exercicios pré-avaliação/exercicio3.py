# Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.

frase = input("Escreva uma frase: ")

vogais = 0
consoantes = 0
outros = 0

for i in frase:
    if i in 'aeiouAEIOU':
        vogais += 1
    elif i in '!@#$%¨&*()_+{`^}?:><" }':
        outros += 1
    else:
        consoantes += 1

print(f"Vogais : {vogais}")
print(f"consoantes : {consoantes}")
print(f"outros: {outros}")

