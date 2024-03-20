# Ex04 - O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta um número 
# inteiro entre 0001 e 9999 e finaliza com o caractere X.

#Exemplos válidos:

#    BR0001X
#    BR1236X
#    BR9999X

#Exemplos inválidos:

#    br0001X
#    BR126X
#    BR99999X
#    BR9999Y
    
# Crie uma função em Python que implementa essa verificação

def funcionario(id):
    if len(id) != 7:
        return False
    if not f'{id[0]}{id[1]}' == 'BR':
        return False
    if not id[len(id) - 1] == 'X':
        return False
    if not int(id[2:6]):
        return False
    return True

print(funcionario('BR0001X'))