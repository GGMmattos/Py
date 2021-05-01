# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
#  Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará

def ajuda(com):
    return help(com)

while True:
    com=str(input("Qual o comando? "))
    if com.upper() == "FIM":
        print("Programa finalizado!!! ")
        break
    else:
        help(com)
      
        

    