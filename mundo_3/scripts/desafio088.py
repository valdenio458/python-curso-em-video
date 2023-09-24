"""
Faça um programa que ajude um apostador da megasena a criar
palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep

lista = list()
jogos = list()
tot = 1
print('-' * 40)
print('         JOGA NA MEGASENA       ')
print('-' * 40)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, v in enumerate(jogos):
    print(f'Jogo {i + 1}: {v}')
    sleep(1)
print('-' * 40)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
print('-' * 40)
