número = int(input('Digite um número:'))
resultado = número % 2
if resultado == 1:
    print('O número {} é impar'.format(número))
else:
    print('O número {} é par'.format(número))