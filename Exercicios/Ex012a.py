preço=float(input('Qual o preço do produto? R$'))
desconto = preço - (preço * 0.05)
print('O produto que custava R${:.2f} com desconto de 5% na promoção, passa a custar R${:.2f}'.format(preço,desconto))