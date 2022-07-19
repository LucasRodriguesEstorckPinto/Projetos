from time import sleep


def leia(n):
    global numero
    while True:
        try:
           numero = int(input(n))
        except:
            print(f'\033[31m{numero} NÃO é um número inteiro!!!\033[m')
        else:
            return numero


def linha(tam = 42):
    print('-'*tam)


def titulo(msg):
    linha()
    print(msg.center(42))
    linha()


def escolhas(lista):
    for c in range(0,len(lista)):
        print(f'\033[35m{c+1}-\033[m   \033[34m{lista[c]}\033[m')


def dorme():
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!')
