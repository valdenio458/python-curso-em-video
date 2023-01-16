from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de seu nascimento: '))
idade = ano_atual - ano_nascimento
print(f'O atleta tem {idade} anos.')
print('=============================')
if idade <= 9: 
  print('Categoria MIRIM')
elif idade <= 14: 
  print('Categoria INFANTIL')
elif idade <= 19: 
  print('Categoria JUNIOR')
elif idade <= 20: 
  print('Categoria SÊNIOR')
else: 
  print('Categoria MASTER')