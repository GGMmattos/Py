#Procurando uma string dentro de outra

nome=str(input('Informe seu nome')).strip()

print("Seu nome tem silva ?  {}".format('silva' in nome.lower()))