from lib.interface import menu, cabecalho
from lib.arquivo import arquivoExiste, criarArquivo, lerArquivo
from time import sleep

arq = 'cursopython.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(["Ver Cadastro", "Cadastrar Pessoas", "Sair do Sistema"])
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        cabecalho("Opção 2")
    elif resp == 3:
        cabecalho("Saindo do sistema...")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(2)
