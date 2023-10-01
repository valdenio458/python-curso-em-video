"""Faça um mini-sistema que utilize o Interactive Help
do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra
‘FIM’, o programa se encerrará.
Importante: use cores."""
c = (
    "\033[m",
    "\033[0;30:41m",
    "\033[0;30;42m",
    "\033[0;30;43m",
    "\033[0;30;44m",
    "\033[0;30;45m",
    "\033[7;30m",
)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    print(c[cor], end="")
    print("~" * len(msg))
    print(msg)
    print("~" * len(msg))
    print(c[0], end="")


comando = ""
while True:
    titulo("SISTEMA DE AJUDA PYHELP", 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO!", 1)
