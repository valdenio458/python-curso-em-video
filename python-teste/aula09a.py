frase = 'Curso em Vídeo Python'
print(frase) # imprime a frase
print(frase[3]) # imprime o caracter da posição 3
print(frase[3:13]) # imprime os caracteres da posição 3 até a posição 12
print(frase[:13]) # imprime os caracteres da posição 0 até a posição 12
print(frase[1:15:2]) # imprime os caracteres da posição 1 até a posição 14, pulando de 2 em 2
print(frase[::2]) # imprime os caracteres da posição 0 até o final, pulando de 2 em 2
print(frase.count('o')) # imprime a quantidade de o's na frase
print(frase.upper().count('O')) # imprime a quantidade de o's na frase, convertida para maiúsculo
print(len(frase)) # imprime o tamanho da frase
print(frase.replace('Python', 'Android')) # imprime a frase, substituindo o texto Python por Android
print('Curso' in frase) # imprime True se o texto Curso estiver na frase
print(frase.find('Python')) # imprime a posição do texto Python na frase
print(frase.split()) # imprime uma lista com os caracteres da frase fatiada
