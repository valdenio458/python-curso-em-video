peso = float(input('Digite seu peso (kg)'))
altura = float(input('Digite sua altura (m)'))
imc = peso / (altura**2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso')
elif imc > 18.5 and imc < 25:
    print('Você está no peso IDEAL')
elif imc > 25 and imc < 30:
    print('Você está em SOBREPESO')
elif imc > 30 and imc < 40:
    print('Você está OBESO')
else:
    print('Você está com OBESIDADE MÓRBIDA')