#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

F=int(input("Informe o primeiro termo: "))
R=int(input("Qual é a razão? "))

decimo=F+((10-1)*R) #CALCULO DO TERMO N-1
for i in range (F,decimo+R,R):
    print('{}'.format(i), end=(' - '))
print("ACABOU")