from random import randint
import interface
from time import sleep

while True:
    interface.titulo('L GAMES')
    interface.escolhas(['Jogo da adivinhação','Jokenpô','PAR OU IMPAR'])
    escolha = interface.leia('Sua escolha: ')
    if escolha == 1:
        valor = randint(0,10)
        interface.titulo('ACERTE O NÚMERO! DICA: 0-10')
        tentativas = 0
        while True:
            chute = interface.leia('Qual o seu chute? ')
            if chute == valor:
                tentativas +=1
                print(f'\033[32mPARABÉNS!! VOCÊ ACERTOU!!  tentativas: {tentativas}\033[m')
                break
            elif chute > valor:
                print('Um pouco menos...')
                tentativas +=1
            elif chute < valor:
                print('Um pouco mais...')
                tentativas +=1
        sleep(2)
    if escolha == 2:
        while True:
            interface.titulo('JOKENPÔ')
            pc = randint(0,2)
            interface.dorme()
            jogador = interface.leia('0 [PEDRA], 1 [PAPEL], 2 [TESOURA]: ')
            if jogador == 0 and pc == 0 or jogador == 1 and pc == 1 or jogador == 2 and pc == 2:
                print('\033[32mEMPATE!!\033[m')
            elif jogador == 0 and pc ==2 or jogador == 2 and pc == 1 or jogador == 1 and pc == 0:
                print('\033[32mPARABÉNS!! VITÓRIA!!\033[m')
                break
            elif jogador == 0 and pc == 1 or jogador == 1 and pc == 2 or jogador ==2 and pc ==0:
                print('\033[31mDERROTA!! TENTE NOVAMENTE ATÉ VENCER <3\033[m')
            else:
                print('\033[31mDigite algo válido\033[m')
            sleep(2)
    if escolha == 3:
        while True:
            interface.titulo('PAR OU IMPAR')
            chutepc = randint(1,10)
            jogador2 = str(input('Você quer par ou impar? ')).strip().lower().title()
            jogador = interface.leia('Seu palpite: ')
            print('\033[32mHmmmmm...Somando...\033[m')
            sleep(1)
            print('\033[33mpipi popopo calculando...\033[m')
            sleep(1)
            print('\033[35mEUREKAA!\033[m')
            sleep(1)
            if (chutepc + jogador) % 2 == 0 and jogador2 == 'Par':
                print(f'A soma de {chutepc} com {jogador} deu {chutepc + jogador}! É par !!')
                break
            elif (chutepc + jogador) % 2 == 0 and jogador2 == 'Impar':
                print(f'A soma de {chutepc} com {jogador} deu {chutepc + jogador}! É par !!')
                print('Mas você escolheu impar...Uma pena :(')
                continue
            elif (chutepc + jogador) % 2 == 1 and jogador2 == 'Impar':
                print(f'A soma de {chutepc} com {jogador} deu {chutepc + jogador}! É Impar!!')
                print('Parabéns !!')
                break
            elif (chutepc + jogador) % 2 == 1 and jogador2 == 'Par':
                print(f'A soma de {chutepc} com {jogador} deu {chutepc + jogador}! É Impar!!')
                print('Mas você escolheu Par...Uma pena :(')
                continue
            sleep(2)
