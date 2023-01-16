from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de seu nascimento: '))
idade = ano_atual - ano_nascimento
IDADE_ALISTAMENTO = 18
saldo = abs(IDADE_ALISTAMENTO - idade)


if idade < IDADE_ALISTAMENTO: 
  print(f'Você deve se alistar daqui há {saldo} anos.')
elif idade == IDADE_ALISTAMENTO: 
  print('Está na hora de você se alistar!')
else: 
  print(f'Você deveria ter se alistado há {saldo} anos!')
