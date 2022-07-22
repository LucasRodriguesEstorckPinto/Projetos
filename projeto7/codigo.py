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


verifica()
while True:
    titulo('CADASTRO DE NOTAS')
    break
