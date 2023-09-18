salário=float(input('Valor do salário R$'))
aumento=salário + (salário *0.15)
print('O salário de R${:.2f} passa a valer R${:.2f}'.format(salário,aumento))