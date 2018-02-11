def add_rationals(x,y):
    nx, dx = number(x), denom(x)
    ny, dy = number(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(number(x) * number(y), denom(x) * denom(y))

def square_rational(x):
    return mul_rationals(x, x)

def square_rational_violating_once(x):
    return rational(number(x) * number(x), denom(x) * denom(x))

def square_rational_violating_twice(x):
    return [x[0] * x[0], x[1] * x[1]]

def print_rational(x):
    print(number(x), '/', denom(x))

def rationals_are_equal(x, y):
    return number(x) * denom(y) == number(y) * denom(x)

def rational(n, d):
    tmp = gcd(n, d)
    return (n//tmp, d//tmp)

def number(x):
    return x[0]

def denom(x):
    return x[1]

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def pair(x, y):
    """Return a function that represents a pair."""
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get

def select(p, i):
    """Return the element at index i of pair p."""
    return p(i)