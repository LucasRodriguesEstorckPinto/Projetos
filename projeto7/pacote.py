from time import sleep
def titulo(texto):
    tamanho = len(texto) + 20
    linhas = '~' * tamanho
    print(linhas)
    print(f'\033[32m{texto.center(tamanho)}\033[m')
    print(linhas)


def verifica():
    try:
        open('notas.txt')
    except:
        print('Arquivo (notas.txt) não foi encontrado, portanto, será criado')
        open('notas.txt', 'a')
        arquivo = open('notas.txt','a')
        arquivo.write(f'{"nome":<10}{"Nota 1":<15}{"Nota 2":<15}{"Nota 3":<15}{"Media":<15}\n{"_"*80}\n')
        arquivo.close()
    else:
        print('Arquivo (notas.txt) foi encontrado, nada feito')


def atribui(nome, notas):
    arquivo = open('notas.txt','a')
    arquivo.write(f'{nome :<10}')
    for c in range(0, 4):
        arquivo.write(f'{notas[c]:<15}')

    arquivo.write('\n')
    arquivo.close()

def condicao(valor):
    while True:
        if valor[0] in 'Ss':
            return 1
        elif valor[0] in 'Nn':
            return 0 
        else:
            print('\033[31mPor favor, digite o que foi pedido\033[m')
            continue

def opcoes():
    sleep(1)
    print('\nO QUE DESEJA FAZER?\n')
    sleep(1)
    print('[1] CADASTRAR ALUNO E SUAS NOTAS\n[2] VER ALUNOS CADASTRADOS\n[3] SAIR DO PROGRAMA')
    print('~'*38)


def inteiro(numero):
    while True:
        try:
            valor = int(input(numero))
        except:
            print('\033[31mPor favor, digite um número\033[m')
        else:
            return int(valor)

def flutuante(numero):
    while True:
        try:
            valor = float(input(numero))
        except:
            print('\033[31mPor favor, digite um número\033[m')
        else:
            return float(valor)