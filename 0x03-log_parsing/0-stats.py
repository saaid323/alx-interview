#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''
import sys

codes = {}
size = []
total = 1


for line in sys.stdin:
    try:
        code = line.split()[-2]
        last = line.split()[-1]
        if code not in codes:
            codes[code] = 1
        codes[code] += 1
        size.append(int(last))
        if total % 10 == 0:
            print(f'File size: {sum(size)}')
            for k, v in sorted(codes.items()):
                print(f'{k}: {v}')
        total += 1
    except KeyboardInterrupt:
        print('HEllo')
        print(f'File size: {sum(size)}')
        for k, v in sorted(codes.items()):
            print(f'{k}: {v}')
        continue
