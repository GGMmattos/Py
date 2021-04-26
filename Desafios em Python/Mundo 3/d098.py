#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.

from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo*=-1

    if passo == 0:
        passo =1
    print(20 * "=-")
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo} ")
    if inicio < fim:
        cont = inicio

        while cont <= fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)
            cont+=passo
        print("FIM")

    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont}", end=" ", flush=True)
            sleep(0.5)
            cont-=passo
        print("FIM")
    
contador(0,10,1)

contador(10,0,2)
print(20 * "=-")

print("Agora é do seu jeito: ")

inicio = int(input("INICIO: "))
fim = int(input("FIM: "))
passo = int(input("PASSO: "))

contador(inicio, fim, passo)