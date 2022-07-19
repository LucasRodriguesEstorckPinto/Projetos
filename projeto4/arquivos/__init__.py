def verifica(arqui):
    try:
        ar = open(arqui,'rt')
        ar.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cria(arqui):
    try:
        ar = open(arqui,'wt+')
        ar.close()
    except:
        print('Ocorreu um erro desconhecido')
    else:
        print(f'Arquivo {arqui} criado com sucesso')


def escreve(arqui,conteudo):
    try:
        ar = open(arqui,'w')
        ar.write(conteudo)
        ar.close()
    except:
        print('ocorreu um erro')
    else:
        print()