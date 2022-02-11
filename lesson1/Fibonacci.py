def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
fibonacci(2000)
print('')
print(sum(range(0, 5)))


for n in range(2,10):
    for i in range(2,n):
        if(n % i == 0):
            print(n, 'equals', n, '*', n//i)
            break
    else:
        print(n, ' is a prime number')

