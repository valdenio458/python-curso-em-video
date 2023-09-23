"""
Aprimore o desafio anterior, mostrando ao final:
a) a soma de todos os valores pares digitados
b) a soma dos valores da terceira coluna
c) o maior valor da segunda linha
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_coluna = maior = 0
for li in range(0, 3):
    for col in range(0, 3):
        matriz[li][col] = int(input(
            f'Digite uma valor para [{li},{col}]: '))
print('-=' * 30)
for li in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[li][col]:^5}]', end='')
        # verifica pares e soma
        if matriz[li][col] % 2 == 0:
            soma_par += matriz[li][col]
        # verifica valores da terceira coluna e soma
        if matriz[li][col] == matriz[li][2]:  # ou for l in range(0, 3):
            soma_coluna += matriz[li][col]
        # verifica o maior valor da segunda linha
        if matriz[li][col] == matriz[1][col]:
            if matriz[li][col] > maior:
                maior = matriz[li][col]

    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {soma_par}')
print(f'A soma dos valores da terceira coluna é: {soma_coluna}')
print(f'O maior valor da segunda linha  é: {maior}')
