# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
km = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quantidade de dias alugados: '))
preco = (dias * 60) + (km * 0.15)
print('O valor a pagar é: {:.2f}'.format(preco))
