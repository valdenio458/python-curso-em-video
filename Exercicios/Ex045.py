from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)
print('''Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' *11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' *11)
if computador == 0:
    if jogador == 0:
        print('\033[31mEMPATE\033[m')
    elif jogador == 1:
        print('\033[31mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[31mEMPATE\033[m')
    elif jogador == 2:
        print('\033[31mJOGADOR VENCE\033[m')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2:
    if jogador == 0:
        print('\033[31mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[31mEMPATE\033[m')
    else:
        print('JOGADA INVÁLIDA')



