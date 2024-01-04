#!/usr/bin/python3
""" returns a list of lists of integers representing the
Pascal’s triangle of n"""


def pascal_triangle(n):
    """function that returns a list of
    lists of integers representing the Pascal’s triangle of n """
    if n <= 0:
        return []
    original = [[1], [1, 1]]
    left_index = 1
    right_index = 1
    temp = original[-1]
    emp = []
    n = n - 2
    for i in range(n):
        for i in range(len(temp)):
            if len(temp) - 1 > i:
                emp.append(temp[i] + temp[i + 1])
        emp.append(left_index)
        emp.insert(0, right_index)
        original.append(emp)
        emp = []
        temp = original[-1]
    return original
