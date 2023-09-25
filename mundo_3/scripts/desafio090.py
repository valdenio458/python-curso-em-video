"""
Faça um programa que leia nome e média de um aluno,
guardando a situação em um dicionário.
Ao final mostre o conteúdo na tela.
"""
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado(a)!'
else:
    aluno['situação'] = 'Reprovado(a)'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
