user_name = input()
number_entries = int(input())
movie_list = []
score_list = []

for i in range(0, number_entries):
    movie_score_list = input().split(" - ")
    movie_list.append(movie_score_list[0])
    score_list.append(movie_score_list[1])

for x in range(0, len(score_list)):
    score_list[x] = float(score_list[x])

sorting_number = False
while sorting_number == False:
    sorting_number = True
    for y in range(0, len(score_list) - 1):
        if score_list[y] < score_list[y + 1]:
            sorting_number = False
            score_list[y], score_list[y + 1] = score_list[y + 1], score_list[y]
            movie_list[y], movie_list[y + 1] = movie_list[y + 1], movie_list[y] 

print('Os filmes sugeridos por {} são:'.format(user_name))
for q in range(0, len(movie_list)):
    final_score_list = []
    final_score_list.append(movie_list[q])
    final_score_list.append(score_list[q])
    print("{} - {}".format(final_score_list[0], final_score_list[1]))