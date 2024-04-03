# Ex08 - Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e retorne um dicionário onde as chaves são as 
# palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. Depois, teste a função com diferentes textos fornecidos pelo 
# usuário.

def contar_palavras(frase: str):
    contagem_palavras = {}
    
    for invalido in (".", ",", "/", "?", "!", "'", "0", "1", "2", "3", "4", "6", "7", "8", "9"):
        frase = frase.replace(invalido, "")

    frase = frase.split(" ")

    for palavra in frase:
        palavra = palavra.replace(",", "")
        palavra = palavra.replace(".", "")

        contagem_palavras[palavra] = 0
        contagem_palavras[palavra] = frase.count(palavra)

    return contagem_palavras

frase = input("Digite uma frase para contar as palavras: ")
print(contar_palavras(frase))