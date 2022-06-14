#nome = input('Digite seu nome: ')
#print('Prazer em te conhecer {:20}!'.format(nome))
#Espaços à direita
#print('Prazer em te conhecer {:>20}!'.format(nome))
#Espaços à esquerda
#print('Prazer em te conhecer {:<20}!'.format(nome))
#Alinhamento ao centro
#print('Prazer em te conhecer {:^20}!'.format(nome))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é: {}\nO produto é: {}\nA divisão é: {:.3f}\nA divisão inteira é: {}\nA exponenciação é: {}'.format(s, m, d, di, e))

# Para quebrar linha \n
# Para não quebrar linha end=''