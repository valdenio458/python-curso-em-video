def leiaInt(num):
    while True:
        try:
            n1 = int(input(num))
        except (ValueError, TypeError):
            print("\033[31mERRO!Digite um número inteiro válido!\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiru não digitar o número!\033[m")
            return 0
        else:
            return n1


def linha(tam=42):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("\033[32mSua opção: \033[m")
    return opc
