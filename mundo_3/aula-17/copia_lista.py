a = [2, 4, 6]
b = a  # cria uma ligação entre as listas
b[2] = 8

print(f'Lista A: {a}')  # [2, 4, 8]
print(f'Lista B: {b}')  # [2, 4, 8]

print('=' * 20)

a = [2, 4, 6]
b = a[:]  # cria uma cópia de a
b[2] = 8

print(f'Lista A: {a}')  # [2, 4, 6]
print(f'Lista B: {b}')  # [2, 4, 8]
