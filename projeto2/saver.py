from pacotes import interface
from pacotes import conferir
from time import sleep
import os
arquivo = f'{conferir.dia()}.txt'
if arquivo == 'Sexta-Feira.txt':
    if os.path.exists('Segunda-Feira.txt'):
        os.remove('Segunda-Feira.txt')
        os.remove('Sexta-Feira.txt')
    if os.path.exists('Terça-Feira.txt'):
        os.remove('Terça-Feira.txt')
    if os.path.exists('Quarta-Feira.txt'):
        os.remove('Quarta-Feira.txt')
    if os.path.exists('Quinta-Feira.txt'):
        os.remove('Quinta-Feira.txt')

resultado = conferir.verifica(arquivo)
if resultado:
    print(f'\033[31m{arquivo} encontrado com sucesso\033[0m')
else:
    conferir.cria(arquivo)

while True:
    interface.titulo('VISUALIZER 1.3')
    interface.escolhas(['CADASTRAR PRESENÇA', 'VER PRESENÇAS', 'SAIR'])
    escolha = interface.leianumero('Sua escolha: ')
    if escolha == 1:
        interface.titulo('CADASTRANDO NOVO ALUNO')
        a = conferir.perguntaalu(['Ana', 'Bernardo', 'Danilo', 'Carolina', 'Gabriel', 'Heitor', 'Lorrayne', 'Lucas Rodrigues'])
        conferir.escreve(arquivo,a)
        sleep(1)
    elif escolha == 2:
        interface.titulo('PRESENÇA DOS ALUNOS')
        conferir.leitura(arquivo)
        sleep(3)
    elif escolha == 3:
        break
        