"""
Crie um programa que tenha uma função chamada voto() que
vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""
from datetime import datetime


def voto(ano):
    idade = datetime.now().year - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


nasc = int(input('Ano de nascimento: '))
print(voto(nasc))
