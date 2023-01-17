from datetime import date
data_atual = date.today().year

tot_maior = 0
tot_menor = 0

for c in range(1, 8): 
    data_nasc = int(input('Digite seu ano de nascimento: '))
    idade = data_atual - data_nasc
    if idade < 21: 
      tot_menor += 1
    elif idade > 21: 
      tot_maior += 1
print(f'Existem {tot_menor} pessoas menores de idade e {tot_maior} pessoas já atingiram a maioridade.')