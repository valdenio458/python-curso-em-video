# O mesmo professor do desafio anterior quer sortear a ordem de apresentação do trabalhos dos alunos. Faça um programa que ajude ele, lendo o nome deles e escrevendo a ordem de apresentação.
from random import shuffle
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista) #shuffle = embaralhar
print('A ordem de apresentação será: {}'.format(lista))
#print(lista)

