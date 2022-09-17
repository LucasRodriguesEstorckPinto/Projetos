import pacote

pacote.verifica()
pacote.titulo('CADASTRO DE ALUNOS')
while True: 
    pacote.opcoes()
    escolha = pacote.inteiro('Digite aqui sua escolha: ')
    if escolha == 1:
        pacote.titulo('CADASTRANDO ALUNO')
        lista = []
        lista.clear()
        name = str(input('Nome do aluno: ')).lower().title().strip()
        nota1 = pacote.flutuante('Digite a primeira nota: ')
        lista.append(round(nota1))
        nota2 = pacote.flutuante('digite a segunda nota:')
        lista.append(round(nota2))
        nota3 = pacote.flutuante('digite a terceira nota:')
        print('~'*37)
        lista.append(round(nota3))
        media = (nota1 + nota2 + nota3) / 3
        lista.append(round(media))
        pacote.atribui(name, lista)
        lista.clear()

    if escolha == 2:
        arqui = open('notas.txt', encoding='utf-8')
        print(arqui.read())
        arqui.close()
    if escolha == 3:
        break
    elif  escolha >3 or escolha <1:
        print('\033[31mPOR FAVOR DIGITE UMA DAS OPÇÕES\033[m')