#!/usr/bin/python3
'''Prime Game'''


def is_prime(nums):
    '''return all prime numbers'''
    prime = [True for _ in range(nums + 1)]
    n = 2
    while n * n <= nums:
        if prime[n]:
            for i in range(n * n, nums + 1, n):
                prime[i] = False
        n += 1
    prime_list = []
    for i in range(2, nums + 1):
        if prime[i]:
            prime_list.append(i)
    return prime_list


def pick(nums):
    '''return the winners'''
    ben = 0
    maria = 0
    for i in range(len(nums)):
        if len(nums[i]) % 2 == 0:
            ben += 1
        elif len(nums[i]) % 2 != 0:
            maria += 1
    if maria > ben:
        return 'Maria'
    if ben > maria:
        return 'Ben'


def isWinner(x, nums):
    '''returns the winner'''
    i = 0
    lis = []
    while i < x:
        lis.append(is_prime(nums[i]))
        i += 1
    return pick(lis)
