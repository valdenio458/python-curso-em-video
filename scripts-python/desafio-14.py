#Escreva um programa que converta uma temperatura digitada em graus Celsius para graus Fahrenheit.
c = float(input('Digite a temperatura em Celsius: '))
f = (9 * c) / 5 + 32  
print('A temperatura em Fahrenheit é: {:.2f}'.format(f))