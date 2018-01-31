def print_max(a, b):
   if a > b:
        print(a, 'is maximum')
   elif a == b:
        print(a, 'is equal to', b)
   else:
        print(b, 'is maximum')

x = int(input('Enter the first integer: '))
y = int(input('Now the second integer: '))

print_max(x, y)
