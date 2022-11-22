#Ataque perfeito do Kuroko

kuroko_mates = input().strip('[]').split(',') #Receber lista com o npumero dos companheiros

target_number = int(input()) #Receber o número alvo

for a in range(len(kuroko_mates)): #Transformar o número dos companheiros em inteiros
    kuroko_mates[a] = int(kuroko_mates[a]) 

target_mates = {'mate1' : 0, 'mate2': 0} #Dicionário para receber números após soma dos números de cada companheiro

counter = 1
for b in kuroko_mates: #Loop para receber o número (b) de cada companheiro
    for c in kuroko_mates[counter:]: #Loop para somar a número b com os números posteriores
        x = b + c
        if x != target_number: #Checar se a soma é diferente do alvo
            x = 0
        elif x == target_number: #Checar se a soma é igual ao alvo e adcionar ao dicionário
            target_mates['mate1'] = kuroko_mates.index(b)
            target_mates['mate2'] = kuroko_mates.index(c)
            break
    counter += 1
    if x == target_number:
        break

mates_list = [] #Lista final para receber os companheiros
mates_list.append(target_mates['mate1'])
mates_list.append(target_mates['mate2'])
print(mates_list)
