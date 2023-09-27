"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre: A) Quantas pessoas
foram cadastradas B) A média de idade C) Uma lista com as
mulheres D) Uma lista de pessoas com idade acima da
média"""
# Leitura dos dados:
lista = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F. ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    resp = str(input('Deseja continuar? [S/N] '))
    if resp.lower() != 's':
        break

media = soma / len(lista)
print('-=' * 30)

# Resultado:
print(f'A) Foram cadastradas {len(lista)} pessoas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) As pessoas com idade acima da média são: ', end='')
for p in lista:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')
