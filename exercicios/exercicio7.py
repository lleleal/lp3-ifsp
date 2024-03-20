# Ex07. Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), crie uma calculadora em Python que solicita ao 
# usuário seu peso (Kg) e sua altura (m) e apresenta em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar quanto o indivíduo
# precisa perder ou ganhar de peso para chegar no peso normal (imc = 24,9).

# IMC = peso / altura * altura

# Classificação
# ----------------------------------
# IMC           Classificação
# -----------------------------------
# < 18,5         Baixo peso
# 18,5 a 24,9     Peso normal
# 25,0 a 29,9     Excesso de peso
# 30,0 a 34,9     Obesidade de Classe 1
# 35,0 a 39,9     Obesidade de Classe 2
# >= 40,00      Obesidade de Classe 3

# Utilize funções.

peso = float(input('Qual seu peso(Kg)?: '))
altura = float(input('Qual a sua altura(m)?: '))

def pesoo(peso, altura):
    imc = peso / (altura * altura)
    peso_normal = 24.9 * (altura * altura)
    peso_exigido = peso_normal - peso

    if imc < 18.5:
        print(f'Você está abaixo do peso, você precisa ganhar {peso_exigido} Kg')
    elif imc >= 18.5 and imc <= 24.9:
        print(f'Você está no peso ideal, parabéns')
    elif imc >= 25.0 and imc <= 29.9:
        print(f'Você está com excesso de peso, você precisa perder {peso_exigido} Kg')
    elif imc >= 30.0 and imc <= 34.9:
        print(f'Você está com obesidade de classe 1, você precisa {peso_exigido} Kg')
    elif imc >= 35.0 and imc <= 39.9:
        print(f'Você está com obesidade de classe 2, você precisa perder {peso_exigido} Kg')
    else:
        print(f'Você está com obesidade de classe 3, você precisa perder {peso_exigido} Kg')

pesoo(peso, altura)