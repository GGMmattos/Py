#Exercício classio das medias com IF

n1=float(input("\nInforme a primeira nota: "))

n2=float(input("\Informe a segunda nota: "))

media=(n1+n2)/2

print(" ")

if media < 5 :
    print("Você está REPROVADO")
elif media  >= 5.0 and media <= 6.9:
    print("Você está de RECUPERAÇÃO")
elif media >= 7:
    print("Você esta APROVADO")