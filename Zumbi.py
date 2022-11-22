# Recebe quantidade de frascos
# lista a serem preenchida
# Recebe quantidade de entradas seguintes
# While para receber elementos

vials = int(input())
element_name = []
element_quantity = []

element_entry_number = int(input())

for i in range(0, element_entry_number):
    element_split = input().split(" ")
    element = element_split
    element_name.append(element[0])
    element_quantity.append(element[1])
    

for x in range(0, len(element_quantity)):
    element_quantity[x] = int(element_quantity[x])

final_sum = 0
final_elements = []
element_range = len(element_quantity)
for z in range(0, element_range):
    for y in range(0, len(element_quantity)):
        final_sum += element_quantity[y]
        final_elements.append(element_name[y])
        if final_sum == vials:
            break
    if final_sum == vials:
        break
    elif final_sum != vials:
        element_quantity.pop(0)
        element_name.pop(0)
        final_elements *= 0
        final_sum = 0

final_elements2 = ""
for i in range(0, len(final_elements)):
    final_elements2 += final_elements[i]
    final_elements2 += " "

if final_sum == vials:
    print("Vencemos a batalha e a humanidade foi restaurada! {}foram usados para deszumbificar".format(final_elements2))
else:
    print("Estou sentido algo estranho... será que também vou virar zumbi?")

    

