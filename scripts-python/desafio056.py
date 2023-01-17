soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
tot_mulher20 = 0
for p in range(1, 5): 
    print(f'----------{p}ª PESSOSA')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    media_idade = soma_idade / p

    if p == 1 and sexo in 'Mm': 
      maior_idade_homem = idade
      nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem: 
      maior_idade_homem = idade
      nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20: 
      tot_mulher20 += 1
print(f'A média de idade do grupo é de {media_idade:.2f} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho}.')
print(f'Foram encontradas {tot_mulher20} mulheres com menos de 20 anos.')