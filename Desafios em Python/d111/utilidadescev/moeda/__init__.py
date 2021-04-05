def metade (n=0, formato=False):
    res = n/2
    return res if formato is False else moeda(res)


def dobro (n=0, formato=False):
    res = n*2
    return res if formato is False  else moeda(res)


def aumentar(n=0,p=0, formato=False):
    res =  n+(n * p/100)            #formula da porcentagem simplificada
    return res if formato is False else moeda(res)


def  diminuir(n=0,p=0, formato=False):
    res = n-(n * p/100)
    return res if formato is False else moeda(res)


def moeda(n=0, moeda="R$"):
    return  f'{moeda}{n:.2f}'.replace('.',',')

def resumo(n=0,p=0,taxa=0):
    print(f"Preço analizado: \t\t\t{moeda(n)}")
    print(f"Metade do preço: \t\t\t{metade(n,True)}")
    print(f"Dobro do preço: \t\t\t{dobro(n,True)}")
    print(f"Preço aumentado em {p}%: \t{ aumentar(n,p,True)}")
    print(f"Preço diminuido em {taxa}%: \t{diminuir(n,taxa,True)}")

