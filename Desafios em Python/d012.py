#Calculando desconto

n1=float(input('Informe o valor do produto = '))

porc=n1*0.05
desconto=n1-porc

print('Valor antes do desconto R${} - Valor com o desconto aplicado R${}'.format(n1, desconto))