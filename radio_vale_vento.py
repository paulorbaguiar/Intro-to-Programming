#Função para analise
def analysis(a):
        for b in a: 
          #separando sons de insetos em lista
            if b == 'crcrcrcrcr' or b == 'uuuuuuuoooooo' or b == 'ooooooeeeeeeee':
                insect_sounds.append(b)
          #Separando sons de avião em lista     
            if b == 'ppprrrrrooon' or b == 'tutututututututu' or b == 'eeeeeeeeoooooo':
                plane_sounds.append(b)

#Laço para analise
signal_analysis = False

while not signal_analysis:
    message = input().split(' ') #Separando a mensagem dento de um lista
    insect_sounds = []
    plane_sounds = []
    analysis(message) #Analise da lista com a mensagem utilizando a Função
    if len(insect_sounds) > 0 and len(plane_sounds) > 0:
        print('A transmissão sugere que tropas estrangeiras e as criaturas do Mar Podre irão se confrontar! Precisamos impedi-los antes que mais mortes desnecessárias ocorram!')
    elif len(insect_sounds) > 0 and len(plane_sounds) == 0:
        print('É apenas o Mar Podre se comunicando, podemos ficar tranquilos, por enquanto…')
    elif len(insect_sounds) == 0 and len(plane_sounds) > 0:
        print('São sinais de aeronaves estrangeiras! Devemos preparar nossas defesas??')
    else:
        print('Não é possível determinar a origem da transmissão… Isso deverá levar mais algum tempo.')
        signal_analysis = True
