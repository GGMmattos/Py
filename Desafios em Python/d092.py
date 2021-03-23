from datetime import datetime
pessoas = dict()

pessoas['nome'] = str(input("Nome: "))
nasc = int(input("Informe o ano de nascimento: "))
pessoas['idade'] = datetime.now().year - nasc
pessoas['ctps'] = int(input("Carteira de trabalho (0 se não tem): "))

if pessoas['ctps'] != 0:
    pessoas['contratação'] = int(input("Informe o ano de contrato: "))
    pessoas['Salario'] = float(int(input("Qual o seu salário?R$ ")))
    pessoas['aposentadoria'] = pessoas['idade'] + ((pessoas['contratação'] + 35) - datetime.now().year)

print(20*"=-")
for k,v in pessoas.items():
    print(f'{k} tem o valor de {v}')



