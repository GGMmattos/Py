#reajuste salarial

n1=float(input('Informe seu salario > '))

porc=n1*0.15
salario=n1+porc

print('O seu salario antes do aumento R${} - depois do aumento R${:.2f}'.format(n1, salario))