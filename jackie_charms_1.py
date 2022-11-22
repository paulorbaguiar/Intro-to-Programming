charm_dict = {
'Carneiro' : ['Adormecer', 'Imortalidade'],
'Cao' : ['Imortalidade', 'Forca descomunal'],
'Cobra' : ['Invisibilidade', 'Equilibrio espiritual'],
'Coelho' : ['Alta velocidade', 'Metamorfose animal'],
'Tigre' : ['Equilibrio espiritual', 'Adormecer'],
'Dragao' : ['Fogo', 'Cura'],
'Cavalo' : ['Cura', 'Levitacao'],
'Macaco' : ['Metamorfose animal', 'Raio laser'],
'Galo' : ['Levitacao', 'Animar objetos'],
'Porco' : ['Raio laser', 'Fogo'],
'Rato' : ['Animar objetos', 'Alta velocidade'],
'Touro' : ['Forca descomunal', 'Invisibilidade']
}

jackie_charm_number = int(input())

jackie_charm_list = []
if jackie_charm_number != 0:
    for charm in range(jackie_charm_number):
        charm = input()
        jackie_charm_list.append(charm_dict[charm][0])

enemies_number = int(input())

enemies_charm_list = []

for charm in range(enemies_number):
    charm = input()
    enemies_charm_list.append(charm)

enemies = len(enemies_charm_list)

for enemy_charm in enemies_charm_list:
    enemy_req = charm_dict[enemy_charm][1]
    if enemy_req in jackie_charm_list:
        print(f'Boa! O talisma do {enemy_charm} vai ser nosso!')
        jackie_charm_list.append(charm_dict[enemy_charm][0])
        enemies -= 1
    elif enemy_req not in jackie_charm_list:
        for i in charm_dict:
            x = charm_dict[i]
            if enemy_req in x:
                if i != enemy_charm:
                    print(f'Nao vai dar, melhor ir atras do talisma do {i} antes.')

if enemies > 0:
    print('Que mau dia!! Melhor pensarmos num plano de fuga.')
elif enemies == 0:
    print('Esse plano funciona, vamos agora!')