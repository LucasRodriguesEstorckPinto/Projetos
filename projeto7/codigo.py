from time import sleep

def titulo(texto):
    tamanho = len(texto) + 15
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
    else:
        print('Arquivo (notas.txt) foi encontrado, nada feito')


def atribui(nome, notas, arquivo):
    arquivo.write(f'{nome :<10}')
    for c in range(0, 3):
        arquivo.write(f'{notas[c][0]:<5}')
        arquivo.write(f'{notas[c][1]:<5}')

    arquivo.write('\n')

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
    print('~'*33)


def inteiro(numero):
    while True:
        try:
            valor = int(input(numero))
        except:
            print('\033[31mPor favor, digite um número\033[m')
        else:
            return int(valor)
            


verifica()
titulo('CADASTRO DE ALUNOS')
while True: 
    opcoes()
    escolha = inteiro('Digite aqui sua escolha: ')
    if escolha == 1:
        print(' AQUI VAI CHAMAR FUNÇÕES PARA CADASTRO')    
    if escolha == 2:
        print('AQUI VAI CHAMAR A FUNÇÃO PARA MOSTRAR O ARQUIVO DE ALUNOS')
    if escolha == 3:
        break
    elif  escolha >3 or escolha <1:
        print('\033[31mPOR FAVOR DIGITE UMA DAS OPÇÕES\033[m')
    
    
