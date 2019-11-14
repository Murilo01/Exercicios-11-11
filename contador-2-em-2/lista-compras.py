i = 0
j = 0
nome = []
quantidade = []
valor = []
while i < 2:

    nome.append(input("Digite o nome do produto"))
    quantidade.append(int(input("Digite a quantidade")))
    valor.append(float(input("Digite o valor do produto")))

    lista = (valor [0]* quantidade [0] + valor [0]* quantidade [0])
    i += 1
    print("Nota Fiscal")

while j < 2:
    lista = (nome[j], quantidade[j]* valor[j])
    print(lista)
    j += 1

