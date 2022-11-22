#A senha perdida

def fib(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    else:
        return fib(a-1) + fib(a-2)

def fact(b):
    if b == 0:
        return 1
    else:
        return b * fact(b-1)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lost_password = input()

word_number = int(input())
words = []
word = ""
word_analysis = []

for i in range(word_number):
    x = input()
    words.append(x)

for q in range(0, len(alphabeth)):
    q = q % 11
    fib_seq = []
    for i in range(q):
        fib_seq.append(fib(i))

    factorial = []
    for w in range(word_number-1):
        factorial.append(fact(w))

    if (q%2) == 0:
        #how to check whether a number is odd or even in python
            

