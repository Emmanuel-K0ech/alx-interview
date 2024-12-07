#!/usr/bin/python3
""" island_perimeter.py  Module """


def count_border_cells(x, y, grid):
    """ counts the number of 1 cells bordering the current cell """
    border_count = 0
    rows = len(grid)
    cols = len(grid[0])

    if y + 1 < cols and grid[x][y + 1] == 1:
        border_count += 1
    if x + 1 < rows and grid[x + 1][y] == 1:
        border_count += 1
    if y - 1 >= 0 and grid[x][y - 1] == 1:
        border_count += 1
    if x - 1 >= 0 and grid[x - 1][y] == 1:
        border_count += 1

    return border_count


def island_perimeter(grid):
    """ Gets perimeter of the island grid """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for x in range(0, rows):
        for y in range(0, cols):
            if grid[x][y] == 1:
                perimeter += 4
                perimeter -= count_border_cells(x, y, grid)

    return perimeter
