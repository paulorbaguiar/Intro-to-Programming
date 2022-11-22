#A primeira pokedex
#Recebe n entradas
    #ADD + nome do Pokemon
        #Descrição
    #DESC + nome do pokemon(Entregar a descrição do pokemon)
#Usar try and except

pokedex = {} #dicionário vazio

entry_input = True

while entry_input == True:
    try:
        pokemon_entry = input().split()
        if pokemon_entry[0] == 'ADD':
            if pokemon_entry[1] not in pokedex:
                pokemon_description = input()
                pokedex[pokemon_entry[1]] = pokemon_description
                print('Pokémon adicionado com sucesso')
            else:
                print('Pokémon já adicionado na Pokédex')
        elif pokemon_entry[0] == 'DESC':
            if pokemon_entry[1] not in pokedex:
                print( 'Ainda não há registro desse Pokémon')
            else:
                print(pokedex[pokemon_entry[1]])

    except EOFError:
        entry_input = False