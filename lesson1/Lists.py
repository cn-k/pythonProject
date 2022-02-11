squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
cubes = [1, 8, 27, 65, 125]
cubes[3] = 4 ** 3
print(cubes)
cubes.append(216)
print(cubes)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
def upperList(list):
    for i in list:
        yield i.upper()
letters[2:5] = upperList(letters[2:5])
print(letters)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)