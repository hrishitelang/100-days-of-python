def add(*args):
    sum = 0
    for i in args:
        sum += i
    return(sum)

x = add(2, 3, 4, 5, 6)
print(x)
y = add(1, 12, 13, 14, 15, 111)
print(y)
