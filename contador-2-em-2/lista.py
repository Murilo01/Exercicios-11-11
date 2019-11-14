Lista_notas = []
contador = 0
while contador < 4:
    contador = contador + 1
    Lista_notas.append(float(input("Digite uma nota")))

Media = (Lista_notas [0] + Lista_notas [1] + Lista_notas [2] + Lista_notas [3])/4
if Media > 7:
    print("Aprovado")
elif Media < 7 and Media >= 5.5:
    print("Testão")
else:
    print("Recuperação")
