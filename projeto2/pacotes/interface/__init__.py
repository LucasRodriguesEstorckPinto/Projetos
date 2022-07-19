def linha(tam=46):
    print('-' * tam)


def titulo(msg):
    linha()
    print(msg.center(46))
    linha()


def leianumero(numero):
    while True:
        try:
            val = int(input(numero))
        except:
            print('\033[31mINVÁLIDO\033[m')
        else:
            return val


def escolhas(lista):
    for c in range(0, len(lista)):
        print(f'\033[32m{c + 1} - \033[33m{lista[c]}\033[m')
