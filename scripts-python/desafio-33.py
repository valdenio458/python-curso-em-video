# Faça um progrma que leia três números e mostre qual é o maior e qual é o menor.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1 > num2 and num1 > num3:
    print('O maior número é {}'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O maior número é {}'.format(num2))
elif num3 > num1 and num3 > num2:
    print('O maior número é {}'.format(num3))
if num1 < num2 and num1 < num3:
    print('O menor número é {}'.format(num1))
elif num2 < num1 and num2 < num3:
    print('O menor número é {}'.format(num2))
elif num3 < num1 and num3 < num2:
    print('O menor número é {}'.format(num3))

