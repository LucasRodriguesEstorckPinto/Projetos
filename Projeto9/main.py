import re


# FUNÇÕES

def byte_to_megabyte(val):
    mega = val /(1024 **2)
    return f"{mega:.2f}"

def percentual_use(totalsum , user):
    percentual = (100 * user) / totalsum
    return percentual

def sum_all_memory():
    summemory = 0
    with open('Projeto9/usuarios.txt', 'r') as file: # o bloco with fecha automaticamente o arquivo
        # Para cada linha no arquivo
        for line in file:
            # Use expressão regular para encontrar números na linha
            numbers = re.findall(r'\d+', line)
        
    return numbers

#PROGRAMA PRINCIPAL 

try: 
    open("Projeto.9/relatorio.txt" , "r")
except:
    file = open("Projeto9/relatorio.txt",'w')
    file.write(f'{"Acme Inc."<10}{"Uso do espaço em disco dos usuários"}')
    for c in range(1,7):
        pass



else:
    print("Relatório ja consta feito.")
    


