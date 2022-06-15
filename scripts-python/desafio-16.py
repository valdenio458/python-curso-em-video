# Crie um programa que leia um número Real qialquer pelo teclado e mostre na tela a sua porção inteira.
# Ex:
# Entrada: 6.127
# Saída: 6
from math import trunc
num = float(input('Digite um número: '))
print('A porção inteira de {} é: {}'.format(num,trunc(num)))


