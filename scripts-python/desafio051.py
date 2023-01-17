primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo + razao, razao): 
    print('{}'.format(c), end=' -> ')
print('ACABOU')
5
