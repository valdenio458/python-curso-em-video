soma = 0
for c in range(1, 7): 
  num = int(input('Digite um número: '))
  if num % 2 == 0:
      soma += num
print(soma)