#!/usr/bin/python3
""" method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened.'''
    dic = {0: boxes[0]}
    keys = [boxes[0]]
    for i in keys:
        for j in i:
            if j not in dic and j < len(boxes):
                dic[j] = boxes[j]
                keys.append(boxes[j])
    if len(keys) == len(boxes):
        return True
    else:
        return False
