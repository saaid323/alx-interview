#!/usr/bin/python3
'''calculates island perimeter'''


def island_perimeter(grid):
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if i + 1 < len(grid) and grid[i + 1][j] != 1:
                    perimeter += 1
                if j + 1 < len(grid[0]) and grid[i][j + 1] != 1:
                    perimeter += 1
                if i - 1 > -1 and grid[i - 1][j] != 1:
                    perimeter += 1
                if j - 1 > -1 and grid[i][j - 1] != 1:
                    perimeter += 1
    return perimeter
