#Cateto e hipotenusa

import math

oposto=float(input('Informe o cateto oposto: '))

adja=float(input('Informe o cateto adjacente: '))

h1=math.hypot(oposto, adja)   #importei o calculo de hipotenusa rsrss

print('Hipotenusa {:.2f}'.format(h1))