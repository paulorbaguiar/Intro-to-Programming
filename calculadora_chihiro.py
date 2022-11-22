#Variável para controlar o laço
stop_calculator = False

#Função para soma
def sum_cal(a, b):
    result = a + b
    return result
#Função para subtração
def sub_cal(a, b):
    result = a - b
    return result
#Função para multiplicação
def mult_cal(a, b):
    result = a * b
    return result
#Função para divisão
def div_cal(a, b):
    result = (a / b)
    return result

while stop_calculator == False:
    type_calculator = input() #recebe o tipo de operação
    numbers_entry = int(input()) #Números de entradas dos valores
    numbers = [] #lista para receber os números
    for x in range(numbers_entry):
        type_number = int(input())
        numbers.append(type_number)

    #Uso das funções, sempre operando os valores no index 0 com os valores no index 1
    if type_calculator == 'S':
        for y in range(len(numbers)):
            final_result = sum_cal(numbers[0], numbers[1])
            numbers[0] = final_result
            numbers.pop(1)
            if len(numbers) == 1:
                break
        print(final_result)
    elif type_calculator == 'sub':
        for y in range(len(numbers)):
            final_result = sub_cal(numbers[0], numbers[1])
            numbers[0] = final_result
            numbers.pop(1)
            if len(numbers) == 1:
                break
        print(final_result)
    elif type_calculator == 'M':
        for y in range(len(numbers)):
            final_result = mult_cal(numbers[0], numbers[1])
            numbers[0] = final_result
            numbers.pop(1)
            if len(numbers) == 1:
                break
        print(final_result)
    elif type_calculator == 'D':
        for y in range(len(numbers)):
            final_result = div_cal(numbers[0], numbers[1])
            numbers[0] = final_result
            numbers.pop(1)
            if len(numbers) == 1:
                break
        print(final_result)

    #parar a calculadora
    stop_calculator_entry = int(input())
    if stop_calculator_entry == 1:
        stop_calculator = False
    else:
        stop_calculator = True