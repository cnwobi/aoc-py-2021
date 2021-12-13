import itertools
import re

from read_input import read_input


def print_grid(grid):
    for row in grid:
        for i in range(len(row)):
            to_print = row[i]
            print(to_print, end="")
        print()


def parse_instructions(line):
    insts = re.findall("\\w+ \\w+ (x|y)=(\\d+)", line)[0]
    return insts[0], int(insts[1])


def parse_input(filename):
    lines = read_input(filename)
    space = 0

    for index, line in enumerate(lines):
        if not line:
            space = index

    lines_coord = lines[:space]
    instructions = list(map(parse_instructions, lines[space + 1:]))

    coordinates = list(map(lambda line: (int(line[0]), int(line[1])),
                           map(lambda line: line.split(','), lines_coord)))

    max_x = max(map(lambda coord: coord[0], list(coordinates))) + 1
    max_y = max(map(lambda coord: coord[1], list(coordinates))) + 1
    grid = [["." for _ in range(max_x)] for _ in range(max_y)]

    for x, y in coordinates:
        grid[y][x] = "#"

    return grid, instructions


def fold_y(y, grid):
    new_y = max(y - 1, len(grid[0]) - y)

    new_grid = [["." for _ in range(len(grid[0]))] for _ in range(new_y + 1)]
    new_grid_row = len(new_grid) - 1
    top_half = y - 1
    bottom_half = y + 1

    while new_grid_row >= 0:
        for col in range(len(new_grid[0])):
            cell = '.'
            if 0 <= top_half < len(grid) and grid[top_half][col] == "#":
                cell = "#"
            if 0 <= bottom_half < len(grid) and grid[bottom_half][col] == "#":
                cell = "#"
            new_grid[new_grid_row][col] = cell
        new_grid_row -= 1
        top_half -= 1
        bottom_half += 1

    return new_grid


def fold_x(x, grid):
    new_x = max(x, len(grid) - x)

    new_grid = [["." for _ in range(new_x)] for _ in range(len(grid))]

    for row in range(len(grid)):
        new_grid_col = 0
        left = x - 1
        right = x + 1
        while new_grid_col < len(new_grid[0]):
            cell = '.'
            if 0 <= right < len(grid[0]) and grid[row][right] == "#":
                cell = "#"
            if 0 <= left < len(grid[0]) and grid[row][left] == "#":
                cell = "#"
            new_grid[row][new_grid_col] = cell
            new_grid_col += 1
            left -= 1
            right += 1

    return new_grid


def count_dot(grid):
    return len(list(filter(lambda x: x == "#", itertools.chain(*grid))))


def process_1(filename):
    grid, instructions = parse_input(filename)
    instruction = instructions[0]
    grid = fold_x(instruction[1], grid) if instruction[0] == 'x' else fold_y(instruction[1], grid)
    return count_dot(grid)


def process(filename):
    grid, instructions = parse_input(filename)

    for instruction in instructions:

        if instruction[0] == "x":
            grid = fold_x(instruction[1], grid)
        else:
            grid = fold_y(instruction[1], grid)

        print()

    print_grid(grid)
    print()

    grid = fold_y(2, grid)

    print_grid(grid)
    print()
    grid = fold_y(5, grid)
    print_grid(grid)

    return grid


if __name__ == '__main__':
    process("small.txt")
