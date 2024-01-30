#!/usr/bin/python3
'''determines if a given data set represents a valid UTF-8 encoding'''


def validUTF8(data):
    '''method that determines if a given data set represents a
    valid UTF-8 encoding'''
    for i in data:
        if len(bin(i)) > 10:
            return False
    return True
