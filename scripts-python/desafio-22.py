# Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Digite o seu nome completo: ')).strip()
# O nome com todas as letras maiúsculas
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
# O nome com todas as letras minúsculas
print('Seu nome em minúsculas é {}'.format(nome.lower()))
# Quantas letras ao todo (sem considerar espaços)
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
# Quantas letras tem o primeiro nome
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
