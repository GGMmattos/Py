#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(msg):
    while True:

        a =str(input(msg))
        if a.isnumeric():
            a = int(a)
        else:
            print("ERRO, digite um número inteiro válido!!!")  
    return a

n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o números: {n}")


    