"""
Faça um programa que tenha uma função chamada maior()
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer
qual deles é o maior.
"""
from time import sleep


def maior(* num):
    maior = 0
    print('-=' * 20)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if valor > maior:
            maior = valor
    print(f'\nForam informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}. ')


maior(2, 3, 4, 8, 12, 1, 0, 65)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
