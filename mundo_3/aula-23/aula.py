import logging

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
# except Exception as erro:
#     print(f'Problema econtrado foi {erro.__class__}')
except ZeroDivisionError:
    logging.error("\033[0;31mNão é possível dividir um número por zero!\033[m")
except ValueError:
    logging.error("\033[0;31mLiteral inválido!\033[m")
except KeyboardInterrupt:
    logging.error("\033[0;31mO usuário preferiu não informar os dados!\033[m")
else:
    print(f"O resultado é {r:.2f}")
finally:
    print("Volte sempre!")
