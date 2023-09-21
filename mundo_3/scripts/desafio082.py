"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas lsitas que vão conter apenas os valores pares
e os ímpares digitados, respectivamente.
Ao final mostre o conteúdo das três listas geradas.
"""
lista = []
lista_par = []
lista_impar = []

while True:
    lista.append(int(input('Digite um número:  ')))

    resp = input('Desaja continuar? [S/N] ')

    if resp.lower() != 's':
        break

for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print('-=' * 30)
print(f'Lista completa {lista}')
print(f'Lista com números pares {lista_par}')
print(f'Lista com números ímpares {lista_impar}')
