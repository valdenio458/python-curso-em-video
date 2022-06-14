# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Digite o salário do funcionário: '))
s = s + (s * 0.15)
print('O novo salário do funcionário é: {:.2f}'.format(s))