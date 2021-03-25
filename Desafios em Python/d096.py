# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l,c):
    area=0
    area = l * c
    print(f"A área do terreno {l} x {c} é {area}m²  ")


print(20*"=-")
print("Controle de Terreno")
print(20*"=-")


largura = float(input("largura(m): "))
cumprimento = float(input("Cumprimento(c): "))

area(largura,cumprimento)