"""
Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até dez.
O programa deverá ler um número pelo teclado (entre 0 e 10)
e mostrá-lo por extenso.
"""
cont = (
  'zero', 'um', 'dois', 'trẽs', 'quatro',
  'cinco', 'seis', 'sete', 'oito', 'nove',
  'dez'
)

while True:
    num = int(input('Digite um número entre 0 a 10: '))
    if 0 <= num <= 10:
        break
    print('Tente novamente! ', end='')
print(f'Você digitou o número {cont[num]}.')
