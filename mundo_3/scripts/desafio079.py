"""
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro ele
não será adicionado. No final serão exibidos todos os valores únicos
em ordem crescente"""

valores = []

while True:
    valor = int(input('Digite um valor : '))

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Este valor já existe na lista!')

    resp = input('Deseja continuar? [S/N] : ')

    if resp.lower() != 's':
        break

valores.sort()  # Ordena a lista em ordem crescente

print('-=' * 30)
print(f'Você digitou os valores {valores}')
