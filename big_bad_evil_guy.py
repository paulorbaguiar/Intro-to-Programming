#Big bad evil guy
#Personagens com forças e fraquezas diferentes
#Arma: Qnt dano
#Armadura: Quão rápido o grupo é derrotado
#Luta em turnos

#Bobby: grande espada / armadura media
#Diana: dardo / armadura leve
#Eric: grande espada / armadura pesada
#Hank: espada / armadura media
#Presto: cajado / armadura leve
#Sheila: espada / armadura leve
#Uni: chifre / armadura leve

#Armas:
#Chifre: 2 de dano
#Cajado: 4 de dano
#Espada: 6 de dano
#Grande espada: 8 de dano
#Dardo: 12 de dano

#Armaduras:
#Armadura pesada: não aumenta o progresso do adversário
#Armadura media: aumenta em 1 o progresso do adversário
#Armadura leve: aumenta em 3 o progresso do adversário

#Input:
    #nome do adversário Vingador: 30 Tiamat: 20 Vingador das Sombras: 14 Outro: 9
    #Número de turnos para a derrota
    #Nome do personagem que atacou

greatsword = 8
horn = 2
staff = 4
sword = 6
dart = 12

heavy_armor = 0
medium_armor = 1
light_armor = 3

characters = {
'Bobby' : (greatsword, medium_armor),
'Diana' : (dart, light_armor),
'Eric' : (greatsword, heavy_armor),
'Hank' : (sword, medium_armor),
'Presto' : (staff, light_armor),
'Sheila' : (sword, light_armor),
'Uni' : (horn, light_armor),
'Mestre dos Magos' : (light_armor, light_armor)
}

enemy = input()
enemy_lifepoints = 0
if enemy == 'Vingador':
    enemy_lifepoints = 30
elif enemy == 'Tiamat':
    enemy_lifepoints = 20
elif enemy == 'Vingador das Sombras':
    enemy_lifepoints = 14
else:
    enemy_lifepoints = 9

turns = int(input())

fight = True

while fight == True:
    try:
        character = input()
    except EOFError:
        if turns > 0:
            print(f'Oh nao, {enemy} e muito forte, este e o fim!')
            break

    character_attack = characters[character]

    enemy_lifepoints -= character_attack[0]
    turns -= character_attack[1]

    if enemy_lifepoints <= 0:
        print(f'{character} executou o ultimo golpe em {enemy}, estamos livres!')
        fight = False
    elif turns <= 0:
        print(f'Oh nao, {enemy} e muito forte, este e o fim!')
        fight = False
    elif character == 'Mestre dos Magos':
        print('Muito obrigado amigo, que nos vejamos novamente um dia')
        fight = False