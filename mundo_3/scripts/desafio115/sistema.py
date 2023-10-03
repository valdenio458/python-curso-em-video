from lib.interface import menu, cabecalho
from time import sleep

while True:
    resp = menu(["Ver Cadastro", "Cadastrar Pessoas", "Sair do Sistema"])
    if resp == 1:
        cabecalho("Opção 1")
    elif resp == 2:
        cabecalho("Opção 2")
    elif resp == 3:
        cabecalho("Saindo do sistema...")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(2)
