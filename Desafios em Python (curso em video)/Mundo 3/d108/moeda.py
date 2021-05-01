def metade (n=0):
    res = n/2
    return res

def dobro (n=0):
    res = n*2
    return res

def aumentar(n=0,p=0):
    res =  n+(n * p/100)            #formula da porcentagem simplificada
    return res

def  diminuir(n=0,p=0):
    res = n-(n * p/100)
    return res

def moeda(n=0, moeda="R$"):
    return  f'{moeda}{n:.2f}'.replace('.',',')
