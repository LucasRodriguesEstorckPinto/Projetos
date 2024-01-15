# receberei um arquivo no seguinte formato
    #alexandre       456123789
    #anderson        1245698456
    #antonio         123456456
    #carlos          91257581
    #cesar           987458
    #rosemary        789456125


road = 'usuarios.txt'

#FUNÇÕES

def catch_number_string(road):
    names = []
    numbers = []
    try:
        read = open(road,'r')
    except:
        print("Error to open the archive")  
    else:
        with read as file:    #método with fecha o arquivo automaticamente, mesmo em caso de excessão
            lines = file.readlines()
            for line in lines:
                part = line.split()
                if len(part) == 2:
                    name , number = part
                    names.append(name)
                    numbers.append(int(number))
                else:
                    print("Error in lists")
    
    return names , numbers

def summemory(memory):
    total = 0
    for sume in memory:
        total +=sume
    return total

def average_memory_usage(totalmemory , memory , position):
    #calculo a media de uso de acordo com o total de memoria
    return (memory[position] * 100)/totalmemory



def byte_to_megabyte(byte):
    megabyte = byte / (1024 **2)
    return megabyte


#PROGRAMA PRINCIPAL

try:
    file = open("relatorio.txt",'w')
except:
    print("Ocorreu um erro ao abrir/criar o relatorio")
else:
    file.write(f'{"ACME Inc.":<30}{"Uso do espaço em disco pelos usuários"}\n{"--"*38}\n{"Nr.":<10}{"Usuário":<20}{"Espaço utilizado":<27}{"% do uso"}\n')
    lists = catch_number_string(road)
    suma = summemory(lists[1])

    for c in range(0,len(lists[0])):
        average = average_memory_usage(suma , lists[1] , c)
        megabyted = byte_to_megabyte(lists[1][c])
        file.write(f'{c+1:<10}{lists[0][c]:<20}{f"{megabyted:.2f} MB":<27}{f"{average:.2f} %"}\n')
        average = 0
        megabyted = 0
    file.write(f"Espaço total ocupado: {byte_to_megabyte(suma):.2f} MB\nEspaço médio ocupado: {byte_to_megabyte(suma)/len(lists[1]):.2f} MB")
    file.close()
    print("RELATORIO.TXT CREATED")