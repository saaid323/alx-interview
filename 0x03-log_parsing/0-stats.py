#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''
import sys

codes = {}
size = []
store = []


try:
    for line in sys.stdin:
        code = int(line.split()[-2])
        last = line.split()[-1]
        if code not in codes:
            codes[code] = 1
        else:
            codes[code] += 1
        store.append(code)
        size.append(int(last))
        if len(store) % 10 == 0:
            print(f'File size: {sum(size)}')
            for k, v in sorted(codes.items()):
                print(f'{k}: {v}')
except KeyboardInterrupt:
    print(f'File size: {sum(size)}')
    for k, v in sorted(codes.items()):
        print(f'{k}: {v}')
