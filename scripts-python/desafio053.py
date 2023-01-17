frase = str(input('Digite uma frase: ')).strip().upper() # remove espaços (split) e força para maiúsculas (upper)
palavras = frase.split() # cria uma lista com cada palavra em um índice
junto = ''.join(palavras) # junta todas as palavras em uma única palavra
inverso = ''
for letra in range (len(junto)-1, -1 , -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('A frase digitada não é um PALÍNDROMO')
