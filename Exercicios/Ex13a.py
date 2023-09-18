preço  = float(input('digite o preço'))
parcelado = preço - preço * .10
prazo = preço + preço * .10
print('O produto custa R${:.2f}, seu valor a vista é de R${:.2f} e a prazo é {:.2f}'.format(preço,parcelado,prazo))