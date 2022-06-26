# Desenvolva um programa que pergunta a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
dist = float(input('Digite a distância da viagem em Km: '))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('O valor da passagem é R$ {:.2f}'.format(preco))
