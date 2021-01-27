#Gerenciador de pagamentos

valor = float(input("Informe o valor: "))
print('''
1 - A vista no dinheiro
2 - A vista no cartão
3 - Em 2 vezes no cartãos
4 - 3x ou mais no cartão''')

op = int(input("\n\nInforme a condição de pagamento: "))  

if op == 1:
    valorfinal = valor - (valor * 0.10)  
    print("\nO preço original R${:.2f}, valor a ser pago R${:.2f}".format(valor,valorfinal ))
elif op == 2:
    valorfinal = valor - (valor * 0.05)
    print("\nO preço original R${:.2f}, valor a ser pago R${:.2f}".format(valor,valorfinal ))
elif op == 3: 
    print("\nVoce pagará R${:.2f},valor sem modificações".format(valor))
elif op == 4:
    op2 = int(input("\nEm quantas parcelas"))
    valorfinal = (valor * 0.20) + valor
    valorparcela = valorfinal/op2
    print("Sua compra será parcelada em {}X de R${:.2f} com juros".format(op2, valorparcela))
    print("\nO preço original R${:.2f}, valor a ser pago R${:.2f}".format(valor,valorfinal))
else:
    print("OPÇÃAO INVALIDA de pagamento, tente novamente ")
    