# Ex05 - Crie um programa em Python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido.

id = str(input('Digite seu id: '))

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

validacao = 'valido' if funcionario(id) else 'invalido'

print(f'{validacao}')