# if, if/else, if/elif, ternario, match

# if
# if condição:
#     codigo
#     codigo
#
# codigo

idade = 20

if idade >= 18:
    print('maior de idade')

print('fora do if')

# if/else

if idade >= 18:
    print('maior de idade')
else:
    print('menor de idade')

# if/elif
# criança: 0 a 12, adolescente: 13 a 17, adulto: 18 a 59, idoso: 60+

if idade <= 12:
    print('criança')
elif idade <= 17:
    print('adolescente')
elif idade <= 59:
    print('adulto')
else:
    print('idoso')

# evitar alinhamento de if's
email = ''
senha = ''

if email == 'admin@email.com':
    if senha == '123admin':
        print('login...')
    else:
        print('email ou senha incorretos')
else:
    print('email ou senha incorretos')


if email == 'admin@email.com' and senha == '123admin':
    print('login...')
else:
    print('email ou senha incorretos')

# entrada: numero 1, 2, 3, ...7
# saída: dia (domingo, segunda, terça, ...sábado)

dia = 4

dias_da_semana = {
    1: 'domingo',
    2: 'segunda',
    3: 'terça',
    4: 'quarta',
    5: 'quinta',
    6: 'sexta',
    7: 'sábado',
}

if dia in dias_da_semana:
    print(dias_da_semana[dia])
else:
    print('dia inválido')


# ternário

media = 6.0

if media >= 6.0:
    situacao = 'aprovado'
else:
    situacao = 'reprovado'


situacao = 'aprovado' if media >= 6.0 else 'reprovado'

# match

match dia:
    case 1:
        print('domingo')
    case 2:
        print('segunda')
    case 3:
        print('terça')
    case 4:
        print('quarta')
    case 5:
        print('quinta')
    case 6:
        print('sexta')
    case 7:
        print('sábado')
    case _:
        print('inválido')
    
# dia útil: 2, 3, 4, 5, 6
# fds: 1, 7

match dia:
    case 1 | 7:
        print('fim de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('dia útil')
    case _:
        print('inválido')