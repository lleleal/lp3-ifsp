# Função 
# Modularizar o programa
# Reuso
# Manutenabilidade (correção de erros e novas funcionalidades)

# Declaração
def ola_mundo():
    print('Olá Mundo!')

# Chamada 
ola_mundo()

# Função sem retorno
def imprimir_mensagem(nome):
    print(f"Bom dia, {nome}")

imprimir_mensagem('José')

# Função com retorno
def mensagem(nome):
    return f"Bom dia, {nome}"

print(mensagem('Maria'))
# enviar_email(mensagem('Maria))

# Parãmetro e Argumento
def somar(numero1, numero2):
    return numero1 + numero2

numero = 3.0

somar(10.0, numero)
# somar(10.0, somar(2, 3))
# somar (10.0, 5)
# 15.0

# Escopo de variáveis
def media(nota1, nota2, nota3):
    total = nota1 + nota2 + nota3
    return total/3
# print(total)

#Parãmetro com valor padrão
def mensagem(nome, mensagem='Bom dia'):
    return f"{mensagem}, {nome}."

mensagem('Marcos', 'Bom dia')
mensagem('Márcia', 'Boa noite')
mensagem('Pedro')

# Argumentos Nomeados
print('Olá', '123', 'teste', sep='@', end="\n\n")
print('TESTE')

mensagem(nome='Lucas', mensagem='Boa Tarde')
mensagem(mensagem='Boa Tarde', nome='Lucas')

# docstring
# comentário de documentação
def somar(n1, n2):
    '''
    Função que soma dois números

    :param n1: primeiro número
    :param n2: segundo número
    :return: soma dos números
    '''
    return n1 + n2

# Funções built-in
# print, type, len, sum, max, min, input
# ver no python3 interativo terminal

def media(*notas):
    return sum(notas) / len(notas)

print(media(10.0, 3.5, 7.5))