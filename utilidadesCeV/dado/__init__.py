def leiadinheiro(valor):
    while True:
        v = str(input(valor)).strip().replace(',','.')
        if v.isalpha() or v=='':
            print(f'\033[31m"{v}" NÃO É UM PARÂMETRO VÁLIDO!!!\033[m')
        else:
            break
    return float(v)
