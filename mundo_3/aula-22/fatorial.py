from utils import numbers

num = int(input("Digite um valor: "))
fat = numbers.fatorial(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {numbers.dobro(num)}.")
print(f"O triplo de {num} é {numbers.triplo(num)}.")
