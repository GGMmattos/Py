#aumentos múltiplos

salario = float(input('Qual é o salario do funcionário? '))

if salario > 1250:
    novosalario= (salario*0.10) + salario
    print('O novo salario é R${:.2f}'.format(novosalario))
if salario <= 1250:
    novosalario = (salario*0.15) + salario
    print("O novo salário é R${:.2f}".format(novosalario))


