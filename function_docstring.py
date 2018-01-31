def print_max(x, y):
    ''' Prints the maximum of two numbers. 

        The two valuse must be integers.'''

    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    elif x == y: 
        print('{0} is equal to {1}'.format(x, y))
    else:
        print(y, 'is maximum')

a = int(input('First integer: '))
b = int(input('Second integer: '))

print_max(a, b)
print(print_max.__doc__)

