preço = float(input('Qual o preço do produto? R$'))
desconto = preço - (preço * 0.05)
print('O produto que custava {:.2f}, com desconto de 5% na promoção, vai custar {:.2f}'.format(preço,desconto))