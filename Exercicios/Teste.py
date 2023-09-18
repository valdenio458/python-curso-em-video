casa=float(input('Qual o valor da casa?'))
salário=float(input('Quanto você ganha?'))
tempo=int(input('Vai financiar em quantos anos? '))
prestação = casa / (tempo *12)
mínimo= salário * (30/100)
print('Para pagar uma casa no valor de {:.2f} em {} anos, a prestação é de {:.2f}'.format(casa,tempo,prestação))
if prestação<=mínimo:
    print('EMPRÉSTIMO CONCEDIDO')
else:
    print('EMPRÉSTIMO NEGADO')
#print('O valor da prestação é {:.2f}'.format(prestação))