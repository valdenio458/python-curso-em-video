valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
tempo = float(input('Digite em quantos anos deseja pagar: '))

valor_prestacao = valor_casa / tempo
if valor_prestacao > salario * 0.30: 
  print('Empréstimo negado!')
else: 
  print('Empréstimo aprovado!')