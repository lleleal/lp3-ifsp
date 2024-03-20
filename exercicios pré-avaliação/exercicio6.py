# Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), converta para o sistema de notas A, B, C, D, ou F, 
# seguindo os padrões de conversão comuns.

def converter_nota(nota):
    if nota >= 90:
        return 'A'
    elif nota >= 80:
        return 'B'
    elif nota >= 70:
        return 'C'
    elif nota >= 60:
        return 'D'
    else:
        return 'F'

def main():
    try:
        nota = float(input("Digite a pontuação (0 a 100): "))
        if 0 <= nota <= 100:
            nota_convertida = converter_nota(nota)
            print(f"A nota convertida é: {nota_convertida}")
        else:
            print("A pontuação inserida está fora do intervalo válido.")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número.")

if __name__ == "__main__":
    main()
