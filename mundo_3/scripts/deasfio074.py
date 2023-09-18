"""Crie um programa que vai gerar cinco númers aleatórios e
colocar em uma tupla. Depois disso, mostre a listagens
dos números e também indique o menor e o maior valor que estão na tupla
"""
from random import randint
num = (
  randint(1, 5), randint(1, 5), randint(1, 5),
  randint(1, 5), randint(1, 5))
print(f'Os valores sorteados foram: {num}')
print(f'O maior número sorteado foi {max(num)}')
print(f'O menor número sorteado foi {min(num)}')
