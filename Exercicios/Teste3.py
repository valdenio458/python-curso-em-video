n1=int(input('Primeira nota:'))
n2=int(input('Segunda nota:'))
média= (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é de {:.1f}'.format(n1,n2,média))
if média < 5:
    print('REPROVADO')
elif média >= 5 and média <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
