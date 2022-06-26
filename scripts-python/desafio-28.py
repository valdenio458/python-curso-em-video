# Escreva um programa qwue faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
n = random.randint(0, 5)
num =int(input('Digite um número inteiro entre 0 e 5: '))
if num == n:
    print('Você venceu!')
else:
    print('Você perdeu!')