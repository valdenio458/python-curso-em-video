# Escreva um programa qwue faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
computador = random.randint(0, 5)
print('-=-' * 20)
print('Pensei em um número entre 0 e 5. Tente adivinhar qual foi: ')
print('-=-' * 20)
jogador =int(input('Em qual número eu pensei?: '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você venceu!')
else:
    print('Você perdeu! Eu pensei no número {} e não no {}'.format(computador, jogador))