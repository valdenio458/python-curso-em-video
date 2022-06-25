# Faça um programa que leia uma frase pelo teclado e mostre:
frase = str(input('Digite uma frase: ')).strip().upper()
# Quantas vezes aparece a letra 'A'
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
# Em que posição ela aparece a primeira vez
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
# Em que posição ela aparece a última vez
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))