soccer_matches = input().split(" ")
frog_int = input().split(" ")

for a in range(0, 12):
    if frog_int[a] == '1':
        if soccer_matches[a] == 'V':
            soccer_matches[a] = 'E'
            print('O maldito sapo interferiu no resultado! O que parecia uma vitória garantida terminou em um empate.')
        elif soccer_matches[a] == 'E':
            soccer_matches[a] = 'D'
            print('O anfíbio da maldição interferiu no resultado! Um empate tranquilo virou uma frustrante derrota.')
        elif soccer_matches[a] == 'D':
            print('O que já era ruim, se tornou uma humilhante derrota. Desgraçado desse sapo!')
    else:
        continue

first_third = []
second_third = []
final_third = []
counter = 0
for b in soccer_matches:
    if counter <= 3:
        first_third.append(b)
        counter += 1
    elif counter <= 7:
        second_third.append(b)
        counter += 1
    else:
        final_third.append(b)
        counter += 1

match_thirds =[]
match_thirds.append(first_third)
match_thirds.append(second_third)
match_thirds.append(final_third)

