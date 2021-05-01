#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#á na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

num = list()
for n in range(0,5):
    n1=(int(input(f"Digite um numero: ")))
    if n == 0 or n1 > num[-1]:
        num.append(n1)
        print("Adicionado no final da lista...")
    else:
        pos=0
        while pos < len(num):
            if n1 <= num[pos]:
                num.insert(pos, n1)
                print(f"Adicionado na posição {pos}")
                break
            pos+=1

print(f"Os valores digitados em orgem foram {num}")