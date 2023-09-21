"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados

b) A lista de valores ordenada de forma decrescente

c) Se o valor 5 foi digitado e está ou não na lista
"""
nums = []

while True:
    nums.append(int(input('Digite uma valor: ')))

    resp = input('Deseja continuar? [S/N]: ')

    if resp.lower() != 's':
        break

print('-=' * 30)
print(f'Foram digitados {len(nums)} elementos.')
nums.sort(reverse=True)
print(f'Os valores em ordem decrescente são {nums}')
if 5 in nums:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
