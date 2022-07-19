def linha(tam = 42):
    print('~'*tam)


def escolhas(lista):
    for c in range(0,len(lista)):
        print(f'\033[32m{c+1}\033[m - \033[35m{lista[c]}\033[m')


def leitura(n):
    while True:
        try:
            j = int(input(n))
        except:
            print('\033[31mDigite um número válido\033[0m')
        else:
            return j


def cabeca(msg):
    linha()
    print(msg.center(42))
    linha()


def leiturafloat(n):
    while True:
        try:
            j = float(input(n))
        except:
            print('\033[31mDigite um número válido\033[0m')
        else:
            return j


def sites(site):
    import webbrowser
    try:
        webbrowser.open(site ,new = 0 , autoraise = True )
    except:
        print('O site está inacessível, solicite ao criador uma correção :)')