"""
Faça um programa que tenha uma função chamada area(),
que receba as dimensões de um terreno retangular (
  largura e comprimento) e mostre a área do terreno.
"""


def area(larg, comp):
    a = larg * comp
    print(f'A aŕea de um terreno {larg}x{comp} é de {a} m². ')


# Programa principal:
print('-' * 20)
print('Controle de Terrenos')
print('-' * 20)
lg = float(input('Largura (m): '))
cp = float(input('Comprimento (m): '))
area(lg, cp)
