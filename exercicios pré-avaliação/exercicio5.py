# Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo (ou seja, pode ser lida de frente 
# para trás e de trás para frente da mesma forma).

palavra = str(input("Digite UMA palavra: "))

if palavra == palavra[::-1]:
    print("A palavra é um Palíndromo")
else:
    print('A palavra não é um palíndromo')