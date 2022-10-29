import webbrowser
import os 
def inteiro(n):
    while True:
        try:
            a = int(input(n))
        except:
            print('\033[31mPOR FAVOR DIGITE UM NÚMERO\033[m')
        else: 
            return a 

while True:
    print('-----O que deseja fazer?-----')
    print('1 - ENTRAR EM UM SITE\n2 - SAIR DO PROGRAMA')
    escolha = inteiro('Digite sua escolha: ')
    os.system('clear') or None
    
    if escolha == 1:
        url = str(input('Digite o nome do site: ')).strip().lower()
        try:
            os.system('clear') or None
            webbrowser.open(f'https://{url}.com.br')
        except webbrowser.Error:
            print('\033[31mOcorreu algum erro!\033[m')
    elif escolha == 2:
        os.system('clear') or None
        break
    else:
        os.system('clear') or None
        pass
