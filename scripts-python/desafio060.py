# from math import factorial
# num = int(input('Digite um número: '))
# print(factorial(num))

num = int(input('Digite um número: '))
c = num
f = 1
while c > 0: 
  print('{}'.format(c), end=' ')
  print(' x ' if c > 1 else ' = ', end=' ')
  f *= c
  c -= 1
print(f'{f}')

# Utilizando o for: 
# num = int(input('Digite um número para calcular seu fatorial: '))
# c = num
# f = 1
# for n in range(f, c + 1):
#     print('{}'.format(c), end= ' ')
#     print('x ' if c > 1 else '=', end= '')
#     f *= c
#     c -= 1
# print('{}'.format(f))