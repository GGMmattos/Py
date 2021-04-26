#Lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("Gerador de P.A com while")

F=int(input("\ninforme o primeiro termo >"))
cont = 1
R=int(input('Agora Informe a razão > '))

while cont <=10:
    print('{} - '.format(F), end=''  )
    F+=R
    cont= cont + 1
print("FIM")