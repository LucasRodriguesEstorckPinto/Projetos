from projeto4 import interface
from projeto4 import arquivos
from time import sleep

interface.titulo('LOST ON THE ISLAND')
opc = interface.escolha(['Começar jogo', 'Sair do jogo'])
if opc == 1:
    print()
elif opc == 2:
    print('Obrigado por jogar :), tente sempre conseguir atingir todos os finais')
