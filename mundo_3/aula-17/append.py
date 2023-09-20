num = []
# num = [2, 5, 9, 1]
# num.append(7)
# print(num)

for c in range(0, 5):
    num.append(int(input('Digite um valor :')))

for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}.')
