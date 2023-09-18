print('{:=^40}'. format(' LOJAS GUANABARA'))
preço = float(input('Qual o preço do produto?R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro ou cheque
[2] à vista no cartão
[3] 2 x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
   total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra será parcelada em 2 x vezes de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * .20)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x deR${:.2f} COM JUROS'.format(totparc,parcela))
else:
    total = preço
    print('\033[31m OPÇÃO INVÁLIDA \033[m de pagamento. Tente novamente'.format(total))
print('Sua compra de R${:.2f} vai custar R${:.2f} '.format(preço,total))
