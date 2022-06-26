# Escreva um programa que leia a velocidade de um carro.
# Se a velocidade do carro for maior que 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
speed = float(input('Digite a velocidade do carro: '))
if speed > 80:
    print('Você foi multado!')
    print('O valor da multa é R$ {:.2f}'.format((speed - 80) * 7))