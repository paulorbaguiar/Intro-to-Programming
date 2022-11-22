#lista para receber suśpeitos.
#loop com for in lista.
#sequencias de if.
#if para retirar primeiro.
#elif para tirar último.
#elif para tirar do meio.
#elif para adicionar a lista.
#else para input errado.
#Print final.

suspects_entry = input().split(',')
suspects = suspects_entry
list_number = len(suspects)

while list_number > 1:
    for index_suspect in suspects:
        print(suspects)
        analysis = input()
        if analysis == 'Não encontrei nada no primeiro suspeito':
            index_suspect == 0 #Duvida - para de remover o primeiro
            suspects.remove(index_suspect)
        elif analysis =='O último da lista está limpo':
            index_suspect == -1 #Duvida - não remove o ultimo
            suspects.remove(index_suspect)
        elif analysis == 'Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita' :
            something #Duvida - bitch I mean like what?
        elif analysis == 'Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição' :
            suspect_number = int(input())
            index_suspect = suspect_number
            suspects.remove(index_suspect) #Duvida - não remove o valor atribuido
        elif analysis == 'Acho que temos mais uma opção a ser analisada…' :
            suspects.append(input())
        else:
            print('Isso não estava no combinado, a lista vai permanecer do mesmo jeito')

print('Acho que encontramos o suspeito. O seu nome é {}, vamos salvar o Sam!'.format(suspects))
print(list_number)