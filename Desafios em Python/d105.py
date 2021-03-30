def notas(*n,sit=0):
    j=0
    maior = 0
    menor =0
    soma = 0
    for i in n:
        print(f"\n{i}")
        if j==0:
            maior=i
            menor=i
        elif  i > maior:
            maior =i
        elif i < menor:
            menor = i
        j+=1
        soma +=i
    media = soma/j
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"medias das notas: {media}")





    dici = dict()
    sit =False




notas(65,2,10,3,100)