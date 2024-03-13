# for, while (break/continue)

# for
for letra in 'hello, world':
    print(letra)

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)

# range
# range(start=0, stop, step=1)
for i in range(5):
    print(i)

for i in range(0, 12, 2):
    print(i)

print(list(range(0, 10, 3)))

lista = list(range(101))
print(lista)


# while

contador = 0
while contador < 5:
    print(contador)
    contador += 1


# break

comando = ''

while True:
    comando = input('Digite o comando: ').lower()

    if comando == 'sair':
        break

    if comando == '1':
        print(comando)


# continue

numeros = [-10, 3, 0, 9, -5, 2]

for numero in numeros:
    if numero <= 0:
        continue

    print(numero)

for numero in numeros:
    if numero > 0:
        print(numero)


# compreensão de listas
# [expressão for item in lista if condição]

numeros = [1, 2, 3, 4, 5]
quadrados = [numero ** 2 for numero in numeros]

print(numeros, quadrados)

numeros = [-3, 0, -5, 1, 2, 4]
positivos = [numero for numero in numeros if numero > 0]

print(numeros, positivos)