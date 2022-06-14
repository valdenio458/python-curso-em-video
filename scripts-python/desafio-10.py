# Crie um programa que leia qunto dinhero uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1,00 = R$ 3,27
m = float(input('Digite quanto dinheiro você tem na carteira: '))
d = m / 3.27
print('Com {:.2f} você pode comprar {:.2f} dólares'.format(m, d))

