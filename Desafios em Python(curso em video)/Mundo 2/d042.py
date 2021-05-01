#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1=float(input("Informe a reta 1: "))

r2=float(input('Informe a reta 1: '))

r3=float(input("Informe a reta 3: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("É possivel formar um triangulo ")
    if r1 == r2 and r2 == r3:
        print(" TIPO equilátero")
    if r1 != r2 != r3 != r1:
        print("Tipo ESCALENO")
    else:
        print("Tipo ISÓCELES")   
else:
    print("Não é possível formar um triangulo")