#três variávei para receber os inputs, separando em listas(verificar se são tudo inteiro)
#função recursiva para poder calcular a soma de cada número
#armazenar cada número em uma varável diferente para tirar o mdc
#Função para calcular o MDC. 
#print final

def sum(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum(int(n / 10))

def mdc(x, y):
    if x > y:
        x, y = y, x
    if x == 0:
        return y
    else:
        return mdc(x, y%x)
    


num1 = int(input())
num1 = sum(num1)
num2 = int(input())
num2 = sum(num2)
num3 = int(input())
num3 = sum(num3)

final_result = mdc(num3, mdc(num1, num2))

print('O MDC obtido é: {}'.format(final_result))