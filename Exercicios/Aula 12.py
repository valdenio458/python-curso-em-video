nome = str(input('Qual o seu nome?'))
if nome == 'Valdênio':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Laura Cláudia Isadora':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia,{}!'.format(nome))