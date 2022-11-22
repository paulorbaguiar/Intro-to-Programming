inst = input()

if inst == "0001":
    inst = 1
elif inst == "0010":
    inst = 2
elif inst == "0011":
    inst = 3
elif inst == "0100":
    inst = 4

#print(inst) #teste instruções

for i in range(0, inst):
    obj = input()

    #Para planetas
    if obj == "0101":
        end1 = True
        beleza = False
        et = False
        water = False
        temp = False
        while end1 == True:
            desc = input()
            if desc == 'Beleza':
                value = int(input())
                if value == 1:
                    beleza = True
                else:
                    beleza = False
            elif desc == 'Possibilidade de vida extraterrestre':
                value = int(input())
                if value == 1:
                    et = True
                else:
                    et = False
            elif desc == 'Agua aparente':
                value = int(input())
                if value == 1:
                    water = True
                else:
                    water = False
            elif desc == 'Temperatura adequada':
                value = int(input())
                if value == 1:
                    temp = True
                else:
                    temp = False
            elif desc == 'Quantidade de luas':
                moonQuant = input()
                moon = 0
                if moonQuant == '0001':
                    moon = moon + 1
                elif moonQuant == '0010':
                    moon = moon + 2
                elif moonQuant == '0011':
                    moon = moon + 3
            elif desc == 'End':
                end1 = False
        
        if (water == True and temp == True and beleza == True and et == True) :
            print(f'Achamos o planeta ideal e ainda tem {moon} lua(s)!')
            print(f'Parece bom demais pra ser verdade, que tipo de vida sera que nos aguarda?')
        elif (water == True and temp == True and beleza == True and et == False) :
            print('Ainda nao sabemos se o planeta e habitavel, parece nao haver vida')
        elif (water == True and temp == True and beleza == False and et == True):
            print(f'O planeta e possivelmente habitavel porem olha essa aparencia, mesmo que tenha {moon} lua(s) vamos omitir esse do relatorio!')
        elif (water == False and temp == False and et == False) :
            print('Vish! Esse nao satisfaz nem as condicoes basicas, nao perderemos tempo')
    
    # para galaxias
    elif obj == "1101":
        planets = input()
        num = 0
        if planets == '01100100':
            num = num + 100
        elif planets == '11001000':
            num = num + 200
        elif planets == '100101100':
            num = num + 300
        
        bh = int(input())
        bhstatus = False
        if bh == 1:
            bhstatus = True
        else:
            bhstatus = False
        
        if bhstatus == True:
            print(f'Ha um buraco negro supermassivo nesta galaxia, demais! Alem da existencia de cerca de {num} milhoes de planetas')
        elif bhstatus == False:
            print(f'Aparentemente nao ha nenhum buraco negro supermassivo no centro dessa galaxia, jurava que todas tinham! Nao importa, ainda temos {num} milhoes de planetas para observar algum deve apresentar possiblidade de vida')

    # Para buracos negros supermassivos
    elif obj == '0000':
        mass = input()
        massValue = 0
        
        if mass == "0101":
            massValue += 5
        elif mass == "1010":
            massValue += 10
        elif mass == "1111":
            massValue += 15
        
        spin = int(input())

        carga = input()
        neut = False
        posi = False
        neg = False

        if carga == "0000":
            neut = True
        elif carga == '0001':
            posi = True
        else: 
            neg = True
        
        print('Conseguimos todas informacoes necessarias para classificar este buraco negro no nosso banco de dados!')
        print('De acordo com as analises, o buraco negro:')
        print(f'- Tem massa de aproximadamente {massValue} milhoes massas solares')
        print(f'- Possui em media {spin} rotacao(oes) por segundo')
        
        if neut == True:
            print('- Apresenta carga inexistente ou nula')
        elif posi == True:
            print('- Apresenta carga positiva')
        elif neg == True:
            print('- Apresenta carga negativa')