distância = float(input('Qual a distância da sua viagem?'))
if distância <=200:
    preço = distância * 0.50
else:
    distância >200
    preço = distância * 0.45
print('O preço da sua viagem será de R${:.2f}'.format(preço))