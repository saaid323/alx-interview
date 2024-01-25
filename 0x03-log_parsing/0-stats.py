#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''
import sys

codes = {}
size = 0
store = []
status_code = ['200', '301', '400', '401', '403', '404', '405', '500']

try:
    for line in sys.stdin:
        code = line.split()[-2]
        last = line.split()[-1]
        if code in status_code and codes.get(code, 0) == 0:
            codes[code] = 1
        else:
            codes[code] += 1
        store.append(code)
        try:
            size += int(last)
        except (ValueError, TypeError):
            continue
        if len(store) % 10 == 0:
            print(f'File size: {size}')
            for k, v in sorted(codes.items()):
                    print(f'{k}: {v}')
    print(f'File size: {size}')
    for k, v in sorted(codes.items()):
        print(f'{k}: {v}')
except KeyboardInterrupt:
    print(f'File size: {size}')
    for k, v in sorted(codes.items()):
            print(f'{k}: {v}')
    raise
