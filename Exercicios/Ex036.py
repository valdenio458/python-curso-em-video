casa = float(input('Valor da casa:R$'))
salário = float(input('Valor do salário;R$'))
anos = int(input('Quantos anos de financiamento'))
prestação = casa / (anos *12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação<=mínimo:
    print('Empréstimo CONCEDIDO')
else:
    print('Empréstimo NEGADO')
