nome = str(input('Digite o seu nome: ')).strip()
if nome == 'Valdênio':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é tão normal!')
print(f'Tenha um bom dia, {nome}!')