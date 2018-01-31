"""Counting Partitions:
The number of partitions of a positive integer n,
using parts up to size m,
is the number of ways in which
n can be expressed as
the sum of positive integer
parts up to m in increasing order."""
# count_partitions(6, 4)
"""
- Recursive decomposition: finding
simpler instances of the problem.

- Explore two possibilities:
    - use at least one 4
    - don't use any 4
- Solve two simpler problems:
    - count_partitions(2, 4)
    - count_partitions(6, 3)
- Tree recursion often involves 
exploring different choices    

"""

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        #print(with_m)
        without_m = count_partitions(n, m-1)
        #print(without_m)
        return with_m + without_m

print(count_partitions(10, 5))