times = (
  'Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Bragantino',
  'Fluminense', 'Athletico-PR', 'Fortaleza', 'Atlético-MG',
  'Cuiabá', 'Cruzeiro', 'Internacional', 'São Paulo',
  'Corinthians', 'Bahia', 'Goiás', 'Santos', 'Vasco da Gama',
  'América-MG', 'Coritiba'
  )

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f"O Coritiba está na {times.index('Coritiba') + 1}ª posição.")
print('-=' * 15)
