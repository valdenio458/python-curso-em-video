print('Gerador de PA')
print('-=' *17)
primeiro = int(input('Primeiro Termo:'))
razão = int(input('Razão:'))
termo = primeiro
cont = 1
while cont <=10:
    print('{}'.format(termo), end=' ')
    termo = termo + razão
    cont = cont + 1
print('FIM')
print('-=' *17)