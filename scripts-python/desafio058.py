# Escreva um programa qwue faça o computador "pensar" em um número inteiro entre 0 e 10. O jogador deve tentar adivinhar o número até acertar, mostrando no final, quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
computador = randint(0, 10)
print('-=-' * 20)
print('Pensei em um número entre 0 e 10. Tente adivinhar qual foi: ')
print('-=-' * 20)
acertou = False
palpites = 0
while acertou == False: 
  jogador =int(input('Em qual número eu pensei?: '))
  print('PROCESSANDO...')
  sleep(1)
  palpites += 1
  if jogador == computador: 
    acertou = True
  else:
      if jogador < computador:
            print('Mais... Tente mais uma vez!')
      elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print(f'ACERTOU com {palpites} tentativa(s)!')
  

