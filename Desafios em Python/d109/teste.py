#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda

n= int(input("Informe um números: "))
print(f"A metade de {moeda.moeda(n)} é {moeda.metade(n,True)} ")
print(f"O dobro de {moeda.moeda(n)} é {moeda.dobro(n,True)} ")
print(f"aumentos 10% temos {moeda.aumentar(n,10),True}")
print(f"Diminuindo 10% temos{moeda.diminuir(n,10,True)}")


