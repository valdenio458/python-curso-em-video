from random import randint
from time import sleep
computador=randint (0,5)
print('=='*30)
print('Vou pensar em um número de 0 a 5 tente adivinhar')
print('=='*30)
jogador=int(input('Em qual número eu pensei?'))
print('PROCESSANDO')
sleep(3)
if computador == jogador:
    print('Acertou')
else:
    print('Perdeu')
