#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 1: "))
    media = (nota1 + nota2) /2
    alunos.append([nome, [nota1 ,nota2],media])
    esc = str(input("Deseja continuar? "))
    if esc in "Nn":
        break
print(20*'=-')
print(f'{"NUM":<4} {"NOME":<10}{"MEDIA":<8}')
for i,j in enumerate(alunos):
    print(f'{i:<4} {j[0]:<10} {j[2]:<8}')
print(20*'=-')
while True:
    opc = int(input("Mostrar nota de qual aluno?(Digite 999 para interromper) "))
    if opc == 999:
        break
        print("FINALIZANDO")
    if  opc <= len(alunos) - 1:
        print(f"A Média de {alunos[opc][0]} é {alunos[opc][2]}")



