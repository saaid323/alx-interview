#!/usr/bin/python3
'''making changes'''


def makeChange(coins, total):
    '''making change'''
    coins = sorted(coins)
    total_coins = 0
    i = len(coins) - 1
    while i >= 0 and total >= 0 and coins:
        if coins[i] > total:
            i -= 1
            continue
        else:
            total -= coins[i]
            total_coins += 1
    if total > 1:
        return -1
    return total_coins
