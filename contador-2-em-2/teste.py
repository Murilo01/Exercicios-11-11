Nota1 = int(input("Digite a nota do 1º Bimestre"))
Nota2 = int(input("Digite a nota do 2º Bimestre"))
Nota3 = int(input("Digite a nota do 3º Bimestre"))
Nota4 = int(input("Digite a nota do 4º Bimestre"))
Media = (Nota1 + Nota2 + Nota3 + Nota4)/4

if Media > 7:
    print("Aprovado")
elif Media < 7:
    print("Recuperação")

