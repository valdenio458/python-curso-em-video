"""
Faça um programa que leia nome e média de um aluno,
guardando a situação em um dicionário.
Ao final mostre o conteúdo na tela.
"""
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado(a)!'
else:
    aluno['situação'] = 'Reprovado(a)'
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situação"]}')
