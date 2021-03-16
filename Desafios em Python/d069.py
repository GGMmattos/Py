#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar

cont = man = woman = cad = 0
escolha = " "

while True:
    print(20*"-")
    if cad == 0:
        print("CADASTRE UMA PESSOA")
    else:
        print("CADASTRE OUTRA PESSOA")
    print(20 * "-")
    idade=int(input("Idade:"))
    genero=(str(input("Sexo(M/F): "))).strip().upper()[0]
    escolha = str(input("Deseja continuar? (SIM / NÃO): ")).strip().upper()[0]
    cad+=1
    while escolha not in "SN":
        escolha = str(input("Deseja continuar? (SIM / NÃO): " )  ).strip().upper()[0]

    if idade > 18:
        cont+=1
        if genero == 'M':
            man += 1

    elif genero == "M":
        man+=1

    elif genero == "F" and idade < 20:
        woman+=1

    if escolha == "N":
        break
print("\n")
print(f'''{cont} pessoas de mais de 18 anos.
{man} homens foram cadastrados .   
{woman} mulheres tem menos de 20 anos.
''')