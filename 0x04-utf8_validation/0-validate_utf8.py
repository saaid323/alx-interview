#!/usr/bin/python3
'''determines if a given data set represents a valid UTF-8 encoding'''


def validUTF8(data):
    '''method that determines if a given data set represents a
    valid UTF-8 encoding'''
    remaining = 0

    for num in data:
        if remaining:
            if (num >> 6) != 0b10:
                return False
            remaining -= 1
        else:
            if num >> 7 == 0:
                remaining = 0
            elif num >> 5 == 0b110:
                remaining = 1
            elif num >> 4 == 0b1110:
                remaining = 2
            elif num >> 3 == 0b11110:
                remaining = 3
            else:
                return False
    if remaining:
        return False
    return True
