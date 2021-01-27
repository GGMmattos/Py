#Conversor de bases numéricas

num=(int(input('Informe um numero inteiro:')))
print("O numero digitado foi {} ".format(num))

print("""\nQual será a base de conversão? )
     1 para binário
     2 para octal
     3 para hexadecimal""") #uso das 3 aspas para o broco

escolha=(int(input("\nEai, oque deseja? ")))

if escolha == 1:
    print("conversão Binaria do numero {} é igual a {}".format(num, bin(num )[2:]))
elif escolha == 2:    
    print("Conversão Octal do numemero {} é igual a {}".format(num, oct(num)[2:]))
elif escolha == 3:
    print("Conversão Hexadecimal do numero {} é igual a {}.".format(num, hex(num)[2:]))
else:
    print("Escolha não disponivel")    