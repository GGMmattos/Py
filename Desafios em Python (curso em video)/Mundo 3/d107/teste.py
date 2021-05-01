#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

n= int(input("Informe um números: "))
print(f"A metade de R${n} é R${moeda.metade(n)} ")
print(f"O dobro de R${n} é R${moeda.dobro(n)} ")
print(f"aumentos 10% temos R${moeda.aumentar(n,10)}")
print(f"Diminuindo 10% temos R${moeda.diminuir(n,10)}")


