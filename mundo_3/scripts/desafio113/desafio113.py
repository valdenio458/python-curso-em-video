"""Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função
leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO!Digite um número inteiro válido!\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiru não digitar o número!\033[m")
            return 0
        else:
            return n1


def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO!Digite um número inteiro válido!\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiru não digitar o número!\033[m")
            return 0
        else:
            return n2
