def analysis(list):
    if len(list) == 0:
        return '0'
    elif list[0] == '(' :
        return 'x' + analysis(list[1:])
    elif list[0] == ')' :
        return 'y' + analysis(list[1:])
    else:
        return analysis(list[1:])

math_expression_number = int(input())

post_analysis = []
for math_expressions_input in range(math_expression_number):
    math_expression = input()
    math_expression = analysis(math_expression)
    post_analysis.append(math_expression)


for exp_analysed in post_analysis:
    par_left = 0
    par_right = 0
    for i in exp_analysed:
        if i == "x":
            par_left += 1
        elif i == "y":
            par_right += 1
        else:
            par_right += 0

    if par_left == par_right:
        print('Essa sentença está com os parênteses balanceados, HOORAY!')
    elif par_left > par_right:
        print("A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la")
    else:
        print ("A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la")
