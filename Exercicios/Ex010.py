real = float(input('Quanto dinheiro você tem na carteira?R$'))
dolar = real / 3.85
euro = real / 4.37
print('Com R${:.2f} você pode comprar U${:.2f} e {:.2f} euros'.format(real, dolar, euro))