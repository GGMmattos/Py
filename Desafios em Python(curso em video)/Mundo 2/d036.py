#Aprovando emprestimo

valor=(float(input("Informe o valor da casa: ")))
salario=(float(input("Informe o salario do comprador: ")))
tempo=(int(input("Em quantos anos irá pagar? ")))

conver=12*tempo
valor_mensal=valor/conver

print("\nValor a ser pago por mes a {} anos: R${:.2f} ".format(tempo,valor_mensal ))

porcentagem=(salario*0.30)

if valor_mensal > porcentagem:
    print('\n\nNão é possivel realizar o emprestimo')
else:
    print("\n\nO emprestimo pode ser feito :) ")