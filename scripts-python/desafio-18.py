# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
an = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(an))
print('O seno do ângulo é: {:.2f}'.format(seno))
cosseno = math.cos(math.radians(an))
print('O cosseno do ângulo é: {:.2f}'.format(cosseno))
tangente = math.tan(math.radians(an))
print('A tangente do ângulo é: {:.2f}'.format(tangente))


