#A nova dimensão de ricky and morty
#Rastrear dimensão para que possa viver
#Dimensõe representadas por um CHAR-NUM. Char é uma letra maiúscula ou minúscula. Num é um número inteiro.
#Receberá string aleatória contendo letras do alfabeto (letras não se repetem. Maiúsculo e minusculos são diferentes um do outro)
#o NUM é a qnt de K combinações dos N caracteres (k é a maior quantidade do tipo de caracteres) (Se ouver quantidade igual de maiúscula e minúscula, trabalha-se apenas com as maiúsculas)
#Recursão para tirar a combinatória
#função para separar maiúscula e minúscula em lista

#Função para definir fatoriais do números
def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)

#Receber o input e lista com as suas letras
char = input() 
char = list(char)

#Listas com letras divididas em maiúscula e minúscula
lower_case = []
upper_case = []

for letter in char:
    x = letter.islower()
    if x == True:
        lower_case.append(letter)
    else:
        upper_case.append(letter)

#Fatorial com número de letras em cada lista previamente definidas
n = len(char)
n1 = factorial(n)
k_lower = len(lower_case)
k1 = factorial(k_lower)
k_upper = len(upper_case)
k2 = factorial(k_upper)

#Definir o NUM requerido
num = 0
if k_lower > k_upper:
    k_n = n - k_lower
    k_n = factorial(k_n)
    num = int(n1 / (k1 * k_n))
elif k_lower < k_upper:
    k_n = n - k_upper
    k_n = factorial(k_n)
    num = int(n1 / (k2 * k_n))
elif k_lower == k_upper:
    k_n = n - k_upper
    k_n = factorial(k_n)
    num = int(n1 / (k2 * k_n))

#Definir o CHAR requerido
if k_lower > k_upper:
    r = int((num % k_lower))
else:
    r = int((num % k_upper))

if k_lower > k_upper:
    final_char = lower_case[r]    
else:
    final_char = upper_case[r]


#Print
if k_lower > k_upper:
    print('Oh geez, Rick!!! Eu não sei se ir pra dimensão {}-{} é uma boa ideia... Eu estou com medo, Rick!!! Oh geez!!!'.format(final_char, num))
    
else:
    print('Morty!!! Morty!!! Vamos para a dimensão {}-{}, Morty!!! Vai ser legal, Morty!!! Rick e Morty na dimensão {}-{} para sempre, Morty!!! Wubba lubba dub dub!!!'.format(final_char, num, final_char, num))
