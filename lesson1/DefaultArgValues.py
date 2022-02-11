def ask_ok(promt, retries=4, reminder='Please try again !'):
    while True:
        ok = input(promt)
        if ok in ('y', 'yes', 'ye'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
#ask_ok('is it true \n')

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))