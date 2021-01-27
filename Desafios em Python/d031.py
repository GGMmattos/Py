#Custo da Viagem

distancia=float(input('Qual é a distancia da sua viagem? '))

if distancia <= 200:
    valor = distancia*0.50
if  distancia > 200:
    valor = distancia*0.45

#print("O preço da passagem é igual a R${:.2f}".format(valor))