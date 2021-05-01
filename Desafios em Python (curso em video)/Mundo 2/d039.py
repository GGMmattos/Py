#Alistamento militar

from datetime import date

ano=int(input("Informe seu ano de nascimento: "))


ano_atual = date.today().year

idade = ano_atual - ano

calc = ano + 18
    
print("Voce nasceu em {} e tem {}".format(ano, idade))
if idade == 18: 
    print("\n E a hora exata de se alistar")

elif idade > 18:
    passou = ano_atual - calc
    print("\n Voce ja passou da data de elistamento, esta atrasado {} anos".format(passou))

elif idade < 18:
    falta = calc - ano_atual  
    print("\n Ainda não chegou o ano de se alistar, falta {} anos".format(falta))



