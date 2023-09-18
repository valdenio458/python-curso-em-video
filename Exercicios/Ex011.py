Larg = float(input('Largura da parede'))
Alt = float(input('Altura da parede'))
area = Larg * Alt
print('A parede tem a dimensão de {:.2f} * {:.2f} e sua área é de {:.2f}m2'.format(Larg, Alt, area))
tinta = area / 2
print('Para pintar essa parede você precisará de {:.2f} litros de tinta'.format(tinta))