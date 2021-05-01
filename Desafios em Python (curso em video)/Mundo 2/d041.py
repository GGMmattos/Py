#Classificando atletas

from datetime import date

ano = (int(input("Informe o ano que nasceu: ")))

ano_atual = date.today().year
idade = ano_atual - ano

print("\nSua idade é {}".format(idade))

if idade <= 9:
    print(" Sua categoria é Mirim")
elif idade > 9 and idade <= 14:
    print("Sua categoria é Infantil")
elif idade > 14 and idade <= 19:
    print("Sua categoria é Junior")
elif idade > 19  and idade <= 25:
    print("Sua categoria é Senior")
elif idade > 25:
    print("Sua categoria é Master")