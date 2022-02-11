def fact(number):
    factorial = 1
    for i in range(1,int(number)+1):
        factorial = factorial * i
    print(factorial)
number = input("give a number")
fact(number)