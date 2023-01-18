num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
  print('''
  [1] somar
  [2] multiplicar
  [3] maior
  [4] novos números
  [5] sair do programa
  ''')
  opcao = int(input('>>>>>>Qual é a sua opção? '))
  if opcao == 1: 
    soma = num1 + num2
    print(f'A soma entre {num1} + {num2} é {soma}.')
    print('=-=' * 10)

  elif opcao == 2: 
    produto = num1 * num2
    print(f'O resultado de {num1} x {num2} é {produto}.')
    print('=-=' * 10)

  elif opcao == 3: 
    maior = 0
    if num1 > num2: 
      maior = num1
    else: 
      maior = num2
    print(f'Entre {num1} e {num2} o maior valor é {maior}.')
    print('=-=' * 10)

  elif opcao == 4:     
    print(f'Digite novos números.')
    num1 = int(input('Primeiro valor: '))
    num2 = int(input('Segundo valor: ')) 
    print('=-=' * 10)
  elif opcao == 5: 
    print('Finalizando!')
    print('=-=' * 10)
  else: 
    print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
print('FIM DO PROGRAMA! VOLTE SEMPRE!')


