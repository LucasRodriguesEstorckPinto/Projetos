from pacotes import interface
from time import sleep
from pacotes import formu

while True:
    interface.cabeca('CALCULADORA BRABA')
    interface.escolhas(['Matemática', 'Física', 'Elétrica','Arquivos complementares','Joguinho da matemática','Sair'])
    es = interface.leitura('Sua escolha: ')

    if es == 1:
        interface.cabeca('FÓRMULAS DE MATEMÁTICA')
        interface.escolhas(['Hipotenusa', 'Fatorial', 'altura de triângulo equilátero', 'Voltar'])
        mat = interface.leitura('Sua escolha: ')
        if mat == 4:
            continue
        elif mat == 1:
            interface.cabeca('HIPOTENUSA')
            a = interface.leiturafloat('Digite aqui o termo A: ')
            b = interface.leiturafloat('Digite aqui o termo B: ')
            print(f'{formu.pit(a, b)}')
            sleep(2)
        elif mat == 2:
            interface.cabeca('FATORIAL')
            h = interface.leitura('Digite aqui o número para ser fatorado: ')
            print(formu.fatorial(h))
            sleep(2)
        elif mat == 3:
            interface.cabeca('ALTURA DO TRIÂNGULO EQUILÁTERO')
            l = interface.leiturafloat('valor de um dos lados do triângulo: ')
            print(formu.triangulo(l))
            sleep(2)

    elif es == 2:
        interface.cabeca('FÓRMULAS FÍSICA')
        interface.escolhas(['Velocidade média', 'Segunda lei de Newton', 'Função horária do deslocamento', 'Voltar'])
        fis = interface.leitura('Sua escolha: ')
        if fis == 4:
            continue
        elif fis == 1:
            interface.cabeca('VELOCIDADE MÉDIA')
            s = interface.leiturafloat('Variação de espaço (M): ')
            t = interface.leiturafloat('Variação de tempo (S): ')
            print(formu.vel(s, t))
            sleep(2)
        elif fis == 2:
            interface.cabeca('SEGUNDA LEI DE NEWTON')
            m = interface.leiturafloat('Massa (Em KG): ')
            a = interface.leiturafloat('Aceleração (Em M/S²): ')
            print(formu.newton(m, a))
            sleep(2)
        elif fis == 3:
            interface.cabeca('FUNÇÃO HORÁRIA DO DESLOC.')
            so = interface.leiturafloat('Posição inicial (m): ')
            v = interface.leiturafloat('Velocidade (m/s): ')
            t = interface.leiturafloat('Variação de tempo (S): ')
            print(formu.fhd(so, v, t))
            sleep(2)

    elif es == 3:
        interface.cabeca('FÓRMULAS ELÉTRICA - CC -')
        interface.escolhas(['Potencia', 'Resistência', 'Tensão', 'Corrente', 'Voltar'])
        ele = interface.leitura('Sua escolha: ')
        if ele == 5:
            continue
        elif ele == 1:
            interface.cabeca('POTÊNCIA')
            i = interface.leiturafloat('Corrente (A): ')
            v = interface.leiturafloat('Tensão (V): ')
            print(formu.pot(i, v))
            sleep(2)
        elif ele == 2:
            interface.cabeca('RESISTÊNCIA')
            t = interface.leiturafloat('Tensão (V): ')
            i = interface.leiturafloat('Corrente (A): ')
            print(formu.res(v=t, i=i))
            sleep(2)
        elif ele == 3:
            interface.cabeca('TENSÃO')
            r = interface.leiturafloat('Resistência (Ω): ')
            i = interface.leiturafloat('Corrente (A): ')
            print(formu.res(r=r, i=i, t=True))
            sleep(2)
        elif ele ==4:
            interface.cabeca('Corrente (A)')
            v = interface.leiturafloat('Tensão (V): ')
            r = interface.leiturafloat('resistência (Ω): ')
            print(formu.corr(v,r))
    elif es==4:
        interface.cabeca('Sites de apoio')
        interface.escolhas(['Apoio elétrica CC','Apoio física', 'Apoio matemática','Voltar'])
        apoio = interface.leitura('Sua escolha: ')
        if apoio == 1:
            print('Abrindo site de apoio elétrica CC')
            interface.sites('https://www.mundodaeletrica.com.br/eletricidade-basica-tudo-que-precisa-saber/')
        elif apoio == 2:
            print('Abrindo arquivo de apoio física')
            interface.sites('http://www.paulorosa.docente.ufms.br/FisicaBasicaVol_I.pdf')
        elif apoio == 3:
            print('Abrindo site de apoio matemática')
            interface.sites('https://matematicabasica.net/ensino-medio/')
        elif apoio == 4:
            continue
    elif es == 6:
        break
    
