#Radar eletronico

vel = float(input('Informe sua velocidade: '))

if vel <= 80:
    print("Tenha um bom dia dirija com seguraça")
else: 
    calc=(vel-80)*7
    print('Voce esta acima do limite de velocidade e será multado no valor de R${:.2f} !!!'.format(calc))
