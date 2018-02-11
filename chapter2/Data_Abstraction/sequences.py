#def count(s, value):
#    """Count the number of occurrences of value in sequence s."""
#    total, index = 0, 0
#    while index < len(s):
#        if s[index] == value:
#            total = total + 1
#        index += 1
#    return total


def count(s, value):
    total = 0
    for elem in s:
        if elem == value:
            total += 1
    return total
