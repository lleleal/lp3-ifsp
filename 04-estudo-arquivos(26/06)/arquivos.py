# Arquivos

# Ler

file = open("dados.txt")
# print(file.read())
# conteudo= file.read()
# print(conteudo)

print(file.readlines())
file.close()

with open("dados.txt") as file:
    print(file.readlines())

with open("dados.txt", "w") as file:
    file.write("banana verde")

with open("dados.txt", "a") as file:
    file.write("\nuva verde")

#lista_produtos => lista de dict (nome, descricao, preco, imagem)

# ler produtos.csv ---> lista_produtos

def obter_produtos():
# 1. abrie o arquivo produtos.csv 
with open("produtos.csv", "r") as file:
    lista_produtos = []

# 2. ler  cada linha do arquivo (readlines())
    linhas = file.readlines()

# 3. Para cada linha criar um dicionário dict com chave-valor
    for linha in linhas:
        #valores = linha.split(",")
        #nome = valores[0]
        #descricao = valores[1]
        #preco = valores[2]
        #imagem = valores[3]
        nome, descricao, preco, imagem = linha.strip().split(",")
        produto = {
            "nome": nome,
            "descricao": descricao,
            "preco": preco,
            "imagem": imagem
        }

# 4. Colocar esse novo dict em uma lista 
lista_produtos.append(produto)
return lista_produtos

# adicionar novo produto no arquivo produtos.csv 
# entrada dict representa produto
#saída? sem saída

def adicionar_produto(p): 
    with open("produtos.csv",'a') as file:
        linha = f"\n{p['nome']},{p['descricao']},{p['preco']},{p['imagem']}"
        file.write(linha) 


p1 = {
    "nome": "Teclado Mecânico",
    "decricao": "Joga fora acorda o bairro todo",
    "preco": 250.00,
    "imagem": "teclado.jpg"
}

adicionar_produto(p1)