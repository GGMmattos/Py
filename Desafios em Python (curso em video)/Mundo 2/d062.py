#Lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
#perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print("Gerador de P.A com while")

F=int(input("\ninforme o primeiro termo >"))
R=int(input('Agora Informe a razão > '))
cont = 1 
mais =10
total = 0
while mais != 0:
    total =  total + mais
    while cont <= total:
        print('{} - '.format(F), end=''  )
        F+=R
        cont= cont + 1
    print("Pausa")
    mais = int(input("Quantos termos deseja mostrar a mais? "))
print("Fim do programa com {} termos mostrados!!!".format(total))