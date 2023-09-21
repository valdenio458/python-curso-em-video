"""  Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
    No final, mostre qual foi o maior e menor valor digitado e as suas
    respectivas posições na lista.
"""
valores = []

for p, c in enumerate(range(0, 5)):
    valores.append(int(input('Digite um valor: ')))

print('-=' * 30)
print(f'Você digitou os valores {valores}')
print(f'Maior valor {max(valores)} na posição: {valores.index(max(valores))}')
print(f'Menor valor {min(valores)} na posição: {valores.index(min(valores))}')
