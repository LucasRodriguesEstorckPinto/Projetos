from math import sqrt


def pit(a = 0, b = 0):
    j = sqrt(a**2 + b**2)
    return f'\033[32mA hipotenusa vale {j:.1f}\033[m'


def fatorial(a):
    try:
        r = 1
        for c in range(a,1,-1):
            r = r * c
    except:
        print('\033[31mOcorreu um erro :(\033[m')
    else:
        return f'\033[32mO fatorial de {a}! é {r}\033[m'


def triangulo(l):
    try:
        h = (sqrt(3)*l) / 2
    except:
        print('\033[31mOcorreu um erro desconhecido :(\033[m')
    else:
        return f'\033[32mA altura do trângulo é de {h:.2f}\033[m'


def vel(S,T):
    try:
        vm = S/T
    except:
        print('\033[31mOcorreu um erro\033[m')
    else:
        return f'\033[32mA velocidade média é {vm} m/s\033[m'


def newton(M,A):
    try:
        Fr = M * A
    except:
        print('\033[31mOcorreu um erro\033[m')
    else:
        return f'\033[32mA força resultante é: {Fr}N\033[m'


def fhd(s0,v,t):
    try:
        s = s0 + (v*t)
    except:
        print('\033[31mOcorreu um erro\033[m')
    else:
        return f'\033[32mA posição final é: {s}M\033[m'


def pot(i,v):
    try:
        p = i*v
    except:
        print('\033[31mOcorreu um erro\033[m')
    else:
        return f'\033[32mA potência em watts é {p}\033[m'


def res(v=0,i=0, t=False, r = 0):
    global ten, h
    try:
        if t:
            ten = r * i
        else:
            h = v/i
    except:
        print('Deu merda aqui')
    else:
        if t:
            return f'\033[32mO valor da tensão é {ten:1f} Volts\033[m'
        else:
            return f'\033[32mO valor da resistência é {h:1f} ohms\033[m'


def corr(v,r):
    try:
        i = v/r
    except:
        print('\033[31mOcorreu um erro\033[m')
    else:
        return f'\033[32mA corrente é igual a {i} AMPERES\033[m'
