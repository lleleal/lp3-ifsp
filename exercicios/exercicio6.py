# Ex06. Crie um programa em Python que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.

#    O volume do aquário em litros;
#    A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
#    A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.

#    Volume é dado por (comprimento * altura * largura) / 1000
#    A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
#    A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

# Utilize funções.

comprimento = float(input('Digite o comprimento do seu: '))
altura = float(input('Digite a altura do seu: '))
largura = float(input('Digite a altura do seu: '))
temperatura_ambiente = int(input('Digite a temperatura ambiente: '))
temperatura_desejada = int(input('Digite a temperatura desejada: '))

def volume_aquario(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def potencia_termostato(volume, temperatura_ambiente, temperatura_desejada):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)

def filtragem(volume):
    return volume * 2, volume * 3

volume = volume_aquario(comprimento, altura, largura)
print(f'{volume}')
print(f'{potencia_termostato(volume, temperatura_ambiente, temperatura_desejada)}')
print(f'{filtragem(volume)}')