#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

n= int(input("Informe um número: "))
print(f"A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))} ")
print(f"O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))} ")
print(f"aumentando 10% temos: {moeda.moeda(moeda.aumentar(n,10))}")
print(f"Diminuindo 10% temos:{moeda.moeda(moeda.diminuir(n,10))}")


