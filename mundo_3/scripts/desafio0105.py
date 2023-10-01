def notas(*n, sit=False):
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n) / len(n)
    if sit:
        if r["media"] >= 7:
            r["situacao"] = "BOA"
        elif r["media"] >= 5:
            r["situacao"] = "RAZOÀVEL"
        else:
            r["situacao"] = "RUIM"

    return r


resp = notas(9, 10, 5.5, 2.5, 9, 8.5, sit=True)
print(resp)
