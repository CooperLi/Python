"""cascade funtion"""

def cascade1(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade1(n//10)
        print(n)


def cascade2(n):
    print(n)
    if n > 10:
        cascade2(n//10)
        print(n)