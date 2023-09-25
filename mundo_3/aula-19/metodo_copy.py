estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federaiva: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print('-=' * 30)
for e in brasil:
    for v in e.values():
        print(f' {v} - ', end=" ")
