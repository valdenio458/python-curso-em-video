n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0: 
  print(f'Sua media foi {media} e vocẽ foi REPROVADO!')
elif media >= 5.0 and media <= 6.9: 
  print(f'Sua media foi {media} e vocẽ entrará em RECUPERAÇÂO!')
else: 
  print(f'Sua media foi {media} e vocẽ foi APROVADO!')