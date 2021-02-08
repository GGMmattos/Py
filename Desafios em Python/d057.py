#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo=str(input("Informe o seu sexo: ")).strip().upper()[0] # pega só a primeira letra 

while sexo not in 'MF': #Simplificação do if
         sexo=str(input('Dados incorretos.Por favor, informe o seu sexo: ')).strip().upper()[0]
   
print("Sexo {} Registrado com sucesso!!!".format(sexo))   


