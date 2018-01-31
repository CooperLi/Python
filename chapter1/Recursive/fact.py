def fact(n):
    if n == 0:
        return n
    else:
        return n * fact(n-1)


    """
    >>> fact(3)
    6
    """