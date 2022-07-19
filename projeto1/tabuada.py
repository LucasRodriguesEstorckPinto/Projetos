from pacotes import interface
escolha = 0
while True:
    interface.cabeca('Tabuada')
    escolha = interface.leitura('Qual tabuada você quer ver ? (999 para pausar):  ')
    if escolha == 999:
        break
    for c in range(1,11):
        print(f'{escolha} X {c:<2} = {escolha * c:<3}')

