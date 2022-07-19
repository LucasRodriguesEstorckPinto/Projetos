def metade(n=0, f=False):
    v = n / 2
    if f:
        form = str(f'R${v:.2f}')
        return form
    else:
        return v


def dobro(n=0, f=False):
    v = n * 2
    if f:
        form = str(f'R${v:.2f}')
        return form
    else:
        return v


def aumentar(n=0, por=0, f=False):
    per = (por / 100) * n
    v = n + per
    if f:
        form = str(f'R${v:.2f}')
        return form
    else:
        return v


def diminuir(n=0, por=0, f=False):
    per = (por / 100) * n
    v = n - per
    if f:
        form = str(f'R${v:.2f}')
        return form
    else:
        return v


def moeda(numero):
    form = str(f'R${numero:.2f}')
    return form


def ajeita(txt):
    v = len(txt) + 20
    print('-' * v)
    print(f'         {txt}')
    print('-' * v)


def resumo(n=0, pa=0, pr=0):
    r1 = dobro(n, True)
    r2 = metade(n, True)
    r3 = aumentar(n, pa, True)
    r4 = diminuir(n, pr, True)
    di = [('Preço analisado:', moeda(n)), ('Dobro do preço:', r1), ('Metade do preço:', r2),
          (f'{pa}% do aumento:', r3), (f'{pr}% de redução:', r4)]
    ajeita('RESUMO DO VALOR')
    for c in range(0, len(di)):
        print(f'{di[c][0]:<25}{di[c][1]}')
    print('-' * 36)

