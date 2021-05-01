#Seno, Cosseno e Tangente 

import math
num=float(input("Informe o angulo que voce deseja: "))

seno=math.sin(math.radians(num))

print('O angulo {} tem o seno de {:.2f}'.format(num, seno))

conseno=math.cos(math.radians(num))

print('O angulo {} tem o conseno {:.2f}'.format(num, conseno))

tangente=math.tan(math.radians(num))

print('O angulo {} tem a tangente {:.2f}'.format(num,tangente))