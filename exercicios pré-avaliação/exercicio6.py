# Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), converta para o sistema de notas A, B, C, D, ou F, 
# seguindo os padrões de conversão comuns.

nota = float(input('digite a sua média(0 a 100): '))

if nota >= 90 and nota <= 100:
    print('Sua nota é: A')
if nota >= 80 and nota <= 89:
    print('Sua nota é: B')
if nota >= 70 and nota <= 79:
    print('Sua nota é: C')
if nota > 60 and nota <= 69:
    print('Sua nota é: D')
else:
    print('Sua nota é: F')