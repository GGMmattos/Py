#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


numeros = ('zero', 'um','dois','tres','quatro', 'cinco','seis', 'sete', 'oito', 'nove','dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze','dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
  escolha=int(input("Digite um numero de 0 a 20: "))
  if 0 <= escolha <=20:
    break
  print("Tente novamente, ", end='')
print(f"Vocè digitou o numero {numeros[escolha]}")

