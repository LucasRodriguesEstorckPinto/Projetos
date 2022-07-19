from datetime import datetime


def verifica(arquivo):
    try:
        ar = open(arquivo, 'rt')
        ar.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cria(arquivo):
    try:
        ar = open(arquivo, 'wt+')
        ar.close()
    except:
        print('\033[31mOcorreu um erro inesperado\033[0m')
    else:
        print(f'{arquivo} criado com sucesso')


def dia():
    data = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta Feira', 'Sexta-Feira', 'Sábado']
    dia = datetime.now().isoweekday()
    return data[dia]


def escreve(arquivo, lista):
    try:
        for c in range(0, len(lista[0])):
            a = open(arquivo, 'a')
            a.write(f'{lista[0][c]:_<30}{dia():<2} - {lista[1][c]}\n')
            a.close()
    except:
        print('DEU MERDA AQUI MEU')


def leitura(arquivo):
    arqui = open(arquivo, 'r')
    print(arqui.read())
    arqui.close()


def perguntaalu(lista):
    lis = []
    pres = []
    for c in range(0, len(lista)):
        esc = leianumero(f'{lista[c]} está presente? [1]  SIM [0] NÃO:  ').replace('0', 'Falta').replace('1','Presença')
        lis.append(lista[c])
        pres.append(esc)
    return lis, pres


def leianumero(numero):
    while True:
        try:
            val = str(input(numero))
        except:
            print('\033[31mINVÁLIDO\033[m')
        else:
            if val == '1' or val == '0':
                return val
            else:
                continue

