n = int(input('Digite um número para calcular seu fatorial'))
c = n
f = 1
print('Calculando {}! = '. format(n), end='')
for n in range(f, c+1):
    print('{}'.format(c), end= ' ')
    print('x ' if c > 1 else '=', end= '')
    f *= c
    c -= 1
print('{}'.format(f))