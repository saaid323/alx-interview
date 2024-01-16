#!/usr/bin/python3
'''calculates the fewest number of operations needed to result in
exactly n H characters in the file'''


def minOperations(n):
    '''method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file'''
    store = n
    total = 0
    div = 2
    while div <= n:
        if n % div == 0:
            total += div
            n /= div
        else:
            div += 1
    if store == div and total == store:
        return 0
    return total
