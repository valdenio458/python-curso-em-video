'''nome = str(input('Digite o seu nome: ')).strip()
if nome == 'Gustavo':
    print('Seu nome é muito bonito!')
else:
    print('Seu nome é normal!')
print('Bom dia, {}!'.format(nome))''' 

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média das notas é {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
#print('PARABÉNS' if m >= 6.0 else 'ESTUDE MAIS')