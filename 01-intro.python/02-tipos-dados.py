# Tipos de dados

# Numérico

# int 
idade = 10

# float
altura = 1.85

# boolean 

ligado = True
frete_gratis = False

# str
nome = "José"
letra = 'a'

# multilinhas
frase = """
Hello, 
world
"""

# Interpolação de string
nome = "Latorre"
idade = 35

# f-string
mensagem = f"Bom dia, {nome}. Você tem {idade} anos."

print(nome[2])
print(nome[-1])
print(nome[0:5])

# strings são objetos
# métodos
print(nome.upper())

# list
# pode conter valores de tipos diferentes
habilidades = ["Java", "HTML", "CSS", "SQL", 77]
print(habilidades[0])

habilidades[0] = "JavaScript"
print(habilidades[0])

# adicionar no final da lista
habilidades.append("Python")
print(habilidades)

# adicionar em uma posição
habilidades.insert(0, "Kotlin")
print(habilidades)

# remover um elemento
habilidades.remove(77)

# remove, sort, clear, copy...

# tupla
# lista de valores sem alteração
opcoes = ("sim", "não", "talvez")
racas_rpg = ("anão", "humano", "elfo", "draconato")

print(racas_rpg[3])

# função que retorna estatísticas sobre as notas de um aluno
# saída: média, menor, maior
# entrada: n1, n2, n3 ou notas (list)

def estatisticas_notas(notas):
    media = sum(notas) / len(notas)
    menor = min(notas)
    maior = max(notas)

    return media, menor, maior

notas = [10.0, 7.5, 6.9, 1.3]
estatistica = estatisticas_notas(notas)
print(estatistica)
print(type(estatistica))

# desempacotamento de tupla
media, menor, maior = estatisticas_notas(notas)
print(media, menor, maior)

# set 
# conjuntos de valores
# não permite valores duplicados
# não é indexado
habilidades = {"Java", "Python", "C#"}
habilidades.add("Java")
print(habilidades)

for habilidade in habilidades:
    print(habilidade)

# dict
# palavra: definição
# key: value

pessoa = {
    "nome": "Silvio",
    "sobrenome": "Cruzatto",
    "idade": 120,
    "casado": True,
}

print(pessoa["nome"])
print(pessoa["sobrenome"])

pessoa["rico"] = True

print(pessoa)

# None
nulo = None