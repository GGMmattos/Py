# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as 
# seguintes informações:
#– Quantidade de notas      – A maior nota   – A menor nota     - A média da turma      - A situação (opcional)


def notas(*n,sit=False):
    dici = dict()

    dici['Total'] = len(n)
    dici['Maior nota'] = max(n)    
    dici['Menor nota'] = min(n)
    dici['Média'] = sum(n)/len(n)
    

    if sit:
        if 6 <= dici['Média'] < 7:
            dici['Situaçao'] = "razoável"
        elif dici['Média'] < 6:
             dici['Situaçao'] = "Ruim"
        else:
            dici['Situaçao'] = "Boa"
    return dici


resp = notas(5.5,2.5,10,6.5,sit=True)
print(resp)