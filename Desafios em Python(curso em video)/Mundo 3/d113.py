#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo in válido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print("Tive um problema com o valor q você digitou, tente novamente!!! ")
            continue
        else:
           return  n

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print("Tive um problema com o valor q você digitou, tente novamente!!! ")
            continue
        else:
            return n
n1 = leiafloat("Informe um valor real: ")
n2 = leiaint("Informe um valor inteiro: ")

print(f"Numero inteiro = {n2}, numero real = {n1}")



