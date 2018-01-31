def trace(fn):
    """Returns a version of fn that first prints before it is called.

    fn - a function of 1 grgument
    """
    def traced(x):
        print(fn, '-->', x)
        return fn(x)
    return traced

@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(10))