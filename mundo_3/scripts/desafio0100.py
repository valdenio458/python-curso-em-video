"""
Faça um programa que tenha uma lista chamada números e duas
funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista e a
segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.
"""
from random import randint

numeros = list()


def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 100))
    valores = ' '.join(map(str, numeros))
    print(f'Sorteando {len(numeros)} valores da lista: {valores} ')


def somarPar():
    sorteia()
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


somarPar()
