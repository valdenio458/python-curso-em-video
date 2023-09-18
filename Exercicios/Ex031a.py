distância = float(input('Qual a distância da sua viagem?'))
preço = distância * 0.50 if distância <=200 else distância * 0.45
print('O preço da sua viagem será de R${:.2f}'.format(preço))