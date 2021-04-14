try:
    n1 = int(input("Informe n1: "))
    n2 =  int(input("Informe n2: "))
    total = n1/n2
except(ValueError,TypeError):
    print("Tive um problema com os tipos de valores que você digitou.")
except ZeroDivisionError:
    print("Não é possivel dividir um número por zero")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados")

except Exception as erro:
    print(f"O erro encontrado foi o seguinte {erro.__cause__}") #ai da pra escolher oq mostrar, será inserido depois do erro
else:
    print((f"{n1}/{n2} = {total:.0f}"))

finally:
    print("Volte sempre, muito obrigago")