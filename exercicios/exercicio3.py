# Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado 
# com base nas seguintes regras:

#    Compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
#   Compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
#   Compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
#   Compras iguais ou superiores a R$ 500,00 - 15% de desconto

valor = float(input('qual o valor da sua compra: '))

if valor >= 0.01 and valor <= 9.99:
    print(f'{valor}')
elif valor >= 10.00 and valor <= 99.99:
    valor -= (valor * 5 / 100)
    print(f'{valor}')
elif valor >= 100.00 and valor <= 499.99:
    valor -= (valor * 10 / 100)
    print(f'{valor}')
else:
    valor -= (valor * 15 / 100)
    print(f'{valor}')