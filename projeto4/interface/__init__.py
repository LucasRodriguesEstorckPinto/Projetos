def leitura(n):
    while True:
        try:
            val = int(input(n))
        except:
            print('DIGITE UM NÚMERO VÁLIDO!!!')
        else:
            return  val


def linhas(tam = 42):
    print('-'*tam)


def titulo(msg):
    linhas()
    print(f'\033[34m{msg.center(42)}\033[m')
    linhas()


def escolha(lista):
    for c in range(0,len(lista)):
        print(f'\033[31m{c+1} -\033[m \033[32m{lista[c]}\033[m')
    opc = leitura('Qual é a sua escolha? ')
    return opc


