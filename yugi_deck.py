#Ajudar yugi organizar baralho
#Receber baralho e entregar infos sobre o mesmo.
#Salvar todas as cartas e retorna a com maior ataque e defesa 
#Obrigatório usar Tuplas e Dicionarios
#Input
    #Receber inteiro N, quantidade de cartas
    #Receber Nome Ataque Defesa
#Output
    #Carta com maior poder de ataque: {nome_da_carta_ataque}, Ataque: {ataque_da_carta}
    #Carta com maior poder de defesa: {nome_da_carta_defesa} Defesa: {defesa_da_carta}

card_numbers = int(input())

deck = {}


for card in range(1, card_numbers+1):
    x = 'card'
    x += str(card)
    deck[x] = ""

for card in deck:
    analysed_card = input().split(' ')
    analysed_card[-2] = int(analysed_card[-2])
    analysed_card[-1] = int(analysed_card[-1])
    deck[card] = analysed_card

max_attack = 0
card_attack_name = ""
for card in deck:
    card_analysis = deck[card]
    if card_analysis[-2] > max_attack:
        card_attack_name = ""
        max_attack = card_analysis[-2]
        card_analysis.pop(-2)
        deck[card] = card_analysis
        x = tuple(deck[card])
        for name in x[0:-1]:
            card_attack_name += name
            card_attack_name += ' '
    else:
        card_analysis.pop(-2)
        deck[card] = card_analysis

max_defense = 0
card_defense_name = ""
for card in deck:
    card_analysis = deck[card]
    if card_analysis[-1] > max_defense:
        card_defense_name = ""
        max_defense = card_analysis[-1]
        card_analysis.pop(-1)
        deck[card] = card_analysis
        x = tuple(deck[card])
        for name in x:
            card_defense_name += name
            card_defense_name += ' '
    else:
        card_analysis.pop(-1)
        deck[card] = card_analysis

card_attack_name = card_attack_name.strip()
card_defense_name = card_defense_name.strip()

print(f'Carta com maior poder de ataque: {card_attack_name}')
print(f'Ataque: {max_attack}\n')
print(f'Carta com maior poder de defesa: {card_defense_name}')
print(f'Defesa: {max_defense}')
