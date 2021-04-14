try:                                                      #tente isso
    n1 = int(input("Informe n1: "))
    n2 =  int(input("Informe n2: "))
    total = n1/n2
except Exception as erro:                                                   # se der errado faça isso
    print(f"Problema encontrado foi{erro.__class__}")
else:                                                      #se der certo faça isso
    print("A muleke deu bom!!!")
    print((f"{n1}/{n2} = {total:.0f}"))

finally:
    print("Volte sempre, muito obrigado!!!")