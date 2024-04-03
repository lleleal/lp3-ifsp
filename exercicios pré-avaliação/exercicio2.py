# Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

numero = int(input('digite um numero para ver sua tabuada do 1 ao 10: '))

for i in range(1, 11):
    print(f'{numero} * {i} = ', numero * i)