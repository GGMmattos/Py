#Calculo de IMC com IF

altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))

imc = peso / (altura**2)

if imc < 18.5:
    print("\nSeu IMC é {:.1f}, Você está a baixo do peso".format(imc))
elif imc >= 18.5 and imc < 25:
    print("\nSeu IMC é {:.1f}, Você esta em seu peso ideal".format(imc))
elif imc >= 25 and imc <= 30:
    print("\nSeu IMC é {:.1f}, Voce esta com sobrepeso".format(imc))
elif imc > 30 and imc < 40:
    print("\nSeu IMC é {:.1f}, Voce esta obeso".format(imc))
else :
    print("\nSeu IMC é {:.1f  }, Voce esta com obesidade morbida".format(imc))

