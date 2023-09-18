velocidade = float(input('Digite a velocidade do carro:'))
if velocidade > 80:
    preço = (velocidade - 80)* 7
    print('Você foi multado e o valor da sua multa é R${}'.format(preço))
else:
    print('Boa viagem!')