n1=float(input('Primeira nota:'))
n2=float(input('Segunda nota:'))
m=(n1+n2)/2
print('Sua média é {:.2f}'.format(m))
if m >= 6.0:
    print('Você foi aprovado')
else:
    print('Recuperação')