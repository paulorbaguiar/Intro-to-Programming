#Treinamento de Gohan
#Lançamento de pedras e notar as distâncias dos arremessos
#Checar se a distância alcançada por ambos são iguais (garantir que ambos antingiram dada distânica mesma qnt de vezes)
#Usar dicinário. Sort e Count são proibídos
#A ordem das distâncias não é importante
#Input
    #Receber qnt de pedras lançadas
    #Duas sequências de N inteiros
#Output
    #Dale Gohan!
    #Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.

number_of_rocks = int(input())

piccolo_dict = {}


for i in range(1, number_of_rocks+1):
    x = 'attempt_piccolo'
    x += str(i)
    piccolo_dict
    piccolo_dict[x] = 0

attempts_piccolo = input().split(' ')

counter = 0
for i in piccolo_dict:
    piccolo_dict[i] = attempts_piccolo[counter]
    counter += 1

gohan_dict = {}

for i in range(1, number_of_rocks+1):
    x = 'attempt_gohan'
    x += str(i)
    gohan_dict
    gohan_dict[x] = 0

attempts_gohan = input().split(' ')

counter = 0
for i in gohan_dict:
    gohan_dict[i] = attempts_gohan[counter]
    counter += 1

final_counter = 0
for a in gohan_dict:
    for b in piccolo_dict:
        if gohan_dict[a] == piccolo_dict[b]:
            final_counter += 1
            piccolo_dict[b] = 'x'
            break

if final_counter == number_of_rocks:
    print('Dale Gohan!')
else:
    print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')




