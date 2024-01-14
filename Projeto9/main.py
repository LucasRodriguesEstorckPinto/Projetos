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
                    numbers.append(number)
                else:
                    print("Error in lists")
    
    return names , numbers

def summemory_average(memory):
    total = 0
    average = 0
    for sum in memory:
        total +=sum
    
