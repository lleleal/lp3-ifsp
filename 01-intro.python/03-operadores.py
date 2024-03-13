# Operadores
# aritméticos
# +, -, *, /, %

nota1 = 10
nota2 = 7.5
media = (nota1 + nota2) / 2

# potenciação

numero = 2 ** 3
numero = 10 ** 2

# lógicos
# and, or, not
# acesos liberado = não bloqueado, idade > 18, horario entre 8:00 e 18:00

bloqueado = False
idade = 21
hora_atual = 10

maioridade = idade >= 18
horario_comencial = hora_atual >= 8 and hora_atual <= 18

if not bloqueado and maioridade and horario_comencial:
    print('liberado')
else:
    print('não liberado')

# operadores de comparação
# >, <, >=, <=, ==, !=

numeros = [1, 2, 3]
numeros2 = [1, 2, 3]

print(numeros == numeros2)

# is (bool)
# idêntidade
print(numeros is numeros2)

numeros3 = [1, 2]
numeros4 = numeros3
print(numeros3 is numeros4)
print(numeros3 is not numeros4)

# in (bool)
print('a' in 'python')

prontuarios = ['SP3089011', 'SP0000000', 'SP1111111', 'SP2222222']
prontuario = 'SP3333333'
print(prontuario in prontuarios)

# sim, não, talvez
opcao = ''

# menos memória, pior manutenção
if opcao == 'sim' or opcao == 'nao' or opcao == 'talvez':
    print('opção válida')
else:
    print('digite novamente')

# mais memória, melhor manutenção
opcoes_validas = ('sim', 'nao', 'talvez')
if opcao in opcoes_validas:
    print('opção válida')
else:
    print('digite novamente')