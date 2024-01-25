#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''
import sys

codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
size = []
store = []


try:
    for line in sys.stdin:
        code = line.split()[-2]
        last = line.split()[-1]
        if code in codes.keys():
            codes[code] += 1
        store.append(code)
        size.append(int(last))
        if len(store) % 10 == 0:
            print(f'File size: {sum(size)}')
            for k, v in sorted(codes.items()):
                if v:
                    print(f'{k}: {v}')
except KeyboardInterrupt:
    print(f'File size: {sum(size)}')
    for k, v in sorted(codes.items()):
        if v:
            print(f'{k}: {v}')
