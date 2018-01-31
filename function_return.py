def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
a = int(input('First integer: '))
b = int(input('Second integer: '))
print(maximum(a, b))
