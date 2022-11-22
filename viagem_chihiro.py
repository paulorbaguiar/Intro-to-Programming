def warm_stones(a, b):
    result = (a + b)/2
    return result

def foot_massage(a):
    if (a/2) == 0:
        result = (a % 7)*6
        return result
    else:
        result = (a % 7)**2
        return result

def meal(a):
    if (a % 10) == 0:
        a += 5
        return a
    else:
        while (a % 0) != 0:
            a += 1
            return a

def massage(a):
    unit = list(a)
    for i in len(unit):
        unit[i] = int(unit[i])
    sum = 0
    for i in unit:
        sum += i
    return sum

tips = 10
int_tips = int(tips)
time_limit = 120
time_passed = 0
end = False

while not end:

    order = input()
    if order == 'pedras':
        time_limit -= 20
        time_passed += 20
        result = warm_stones(int_tips, time_passed)
        result = result
        tips += result
    elif order == 'pes':
        time_limit -= 30
        time_passed += 30
        result = foot_massage(int_tips)
        result = result
        tips += result
    elif order == 'refeicao':
        time_limit -= 15
        time_passed += 15
        result = meal(int_tips)
        result = result
        tips = result
    elif order == 'completa':
        time_limit -= 50
        time_passed += 50
        result = massage(int_tips)
        result = result
        tips += result
    else:
        time_limit -= 5
        time_passed += 5

    if tips > 50:
        end = True
    elif time_limit <= 0:
        end = True
print(tips)