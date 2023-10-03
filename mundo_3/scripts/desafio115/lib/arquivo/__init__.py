from lib.interface import cabecalho


def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except FileNotFoundError:
        print("Houve um erro na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except FileNotFoundError:
        print("Houve ao ler o arquivo!")
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())
