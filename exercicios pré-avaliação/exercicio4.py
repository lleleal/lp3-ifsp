# Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. O programa deve pedir ao usuário para votar várias vezes e, no final, 
# mostrar o número de votos de cada candidato e quem foi o vencedor. 

def main():
    candidatos = ["Candidato 1", "Candidato 2", "Candidato 3"]
    votos = [0] * len(candidatos)

    print("Bem-vindo ao Simulador de Eleições!")
    num_votantes = int(input("Quantas pessoas irão votar? "))

    for _ in range(num_votantes):
        print("\nCandidatos disponíveis:")
        for index, candidato in enumerate(candidatos, start=1):
            print(f"{index}. {candidato}")
        
        voto = int(input("Digite o número do candidato escolhido: "))
        
        if 1 <= voto <= len(candidatos):
            votos[voto - 1] += 1
            print("Voto registrado com sucesso!")
        else:
            print("Opção inválida. Voto não registrado.")

    print("\nResultado da Eleição:")
    for index, candidato in enumerate(candidatos):
        print(f"{candidato}: {votos[index]} votos")

    vencedor_index = votos.index(max(votos))
    print(f"\nO vencedor é: {candidatos[vencedor_index]} com {votos[vencedor_index]} votos.")

if __name__ == "__main__":
    main()

