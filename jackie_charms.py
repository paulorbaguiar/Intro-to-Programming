#Yu Mo Gui Gwai Fai Di Za
#Talismãs tem habilidades e requisitos
#Jackie já começa com talismãs e ganha habilidade quando ganha talismã
#O chefão só é derrotado se jack possui as habilidades requisito do talismã do chefão
#Jack enfrenta cada chefão uma só vez com as habilidades que tem
#Um talismã depende de outro pra ser conquistado
#Input
    #inteiro - N talismãs
    #Nome dos N talismãs
    #Número de adversários
    #Talismãs dos adversários

#Output
    #String para cada adversário

#Basicamente, comparar talismã jack com talismã infinito

charm_dict = {
'Carneiro' : ('Adormecer', 'Imortalidade'),
'Cao' : ('Imortalidade', 'Forca descomunal'),
'Cobra' : ('Invisibilidade', 'Equilibrio espiritual'),
'Coelho' : ('Alta velocidade', 'Metamorfose animal'),
'Tigre' : ('Equilibrio espiritual', 'Adormecer'),
'Dragao' : ('Fogo', 'Cura'),
'Cavalo' : ('Cura', 'Levitacao'),
'Macaco' : ('Metamorfose animal', 'Raio laser'),
'Galo' : ('Levitacao', 'Animar objetos'),
'Porco' : ('Raio laser', 'Fogo'),
'Rato' : ('Animar objetos', 'Alta velocidade'),
'Touro' : ('Forca descomunal', 'Invisibilidade')
}

jackie_charm_number = int(input())

if jackie_charm_number == 0:
    print('Que mau dia!! Melhor pensarmos num plano de fuga.')
    plan_stop = True 
else:
    jackie_charm_list = []

    for charm in range(jackie_charm_number):
        charm = input()
        jackie_charm_list.append(charm)

    enemies_number = int(input())

    enemies_charm_list = []

    for charm in range(enemies_number):
        charm = input()
        enemies_charm_list.append(charm)

    plan_stop = False

    while plan_stop == False:
        
        for jackie_charm_select in jackie_charm_list:
            if jackie_charm_list == '0':
                break           
            elif len(enemies_charm_list) == 0:
                print('Esse plano funciona, vamos agora!')
                plan_stop = True
                break
            else:
                jackie_charm = charm_dict[jackie_charm_select]
                for enemy_charm_select in enemies_charm_list:
                    enemy_charm = charm_dict[enemy_charm_select]
                    if jackie_charm[0] == enemy_charm[1]:
                        print(f'Boa! O talisma do {enemy_charm_select} vai ser nosso!')
                        jackie_charm_list.append(enemy_charm_select)
                        enemies_charm_list.remove(enemy_charm_select)
                        break
                    elif jackie_charm[0] != enemy_charm[1]:
                        for missing_charm in charm_dict:
                            x = charm_dict[missing_charm]
                            if missing_charm != jackie_charm_select:
                                if missing_charm in jackie_charm_list:
                                    break
                            if x[0] == enemy_charm[1]:
                                print(f'Nao vai dar, melhor ir atras do talisma do {missing_charm} antes.')
                                if missing_charm not in enemies_charm_list:
                                    print('Que mau dia!! Melhor pensarmos num plano de fuga.')
                                    plan_stop = True
                                    jackie_charm_list = '0'
                                    break
                            else:
                                continue

