#Programa que entre com o ano e retorne o status da pessoa referente a votação, sendo que a resposta é o retorno de uma função

def voto(ano):
    from datetime import datetime    #economizamos memoria ao importar a biblioteca que sera usada apenas na função  apenas nela
    idade = datetime.now().year - ano
    if idade < 16:
        return f"Voce tem {idade} anos: VOTO NEGADO"
    elif 16 <= idade <= 18 or idade > 64:
        return f"Voce tem {idade} anos: VOTO OPCIONAL" #Não precisamos do print
    else:
        return f"você tem {idade} anos: VOTO OBRIGATORIO"

ano = int(input("Em que ano você nasceu?"))
print(voto(ano))
