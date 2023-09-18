from random import randint
from time import sleep
computador = randint (0,5)# Faz o compuador pensar
print('-==-'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar')
print ('-==-' *20)
jogador = int(input('Em que número eu pensei?')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS!Você me venceu')
else:
    print('EU GANHEI. Pensei no número {} e não no {}'.format(computador,jogador))