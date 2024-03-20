# Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo (ou seja, pode ser lida de frente 
# para trás e de trás para frente da mesma forma).


def verificar_palindromo(texto):
    # Remover espaços e tornar tudo minúsculo para facilitar a comparação
    texto = texto.replace(" ", "").lower()
    
    # Comparar o texto com seu reverso
    return texto == texto[::-1]

def main():
    palavra = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
    if verificar_palindromo(palavra):
        print("Sim, é um palíndromo!")
    else:
        print("Não, não é um palíndromo.")

if __name__ == "__main__":
    main()