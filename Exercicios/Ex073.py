times = ('Flamengo', 'Santos', 'Palmeiras', 'São Paulo', 'Corinthians', 'Atlético-MG',
         'Internacional', 'Bahia', 'Botafogo', 'Athletico-PR','Goiás', 'Grêmio',
         'Ceará', 'Vasco','Fortaleza', 'Cruzeiro',
        'Chapecoense', 'Fluminense', 'CSA', 'Avaí' )
print('-='*15)
print(f'Lista de times do Brasileirão:{times}')
print('-='*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são:{times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-='*15)