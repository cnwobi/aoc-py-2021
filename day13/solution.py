import itertools
import re

from read_input import read_input


def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end="")
        print()


def parse_instructions(line):
    insts = re.findall("\\w+ \\w+ (x|y)=(\\d+)", line)[0]
    return insts[0], int(insts[1])


def print_dots(coordinates):
    max_x = max(map(lambda coord: coord[0], coordinates)) + 1
    max_y = max(map(lambda coord: coord[1], coordinates)) + 1
    grid = [[" " for _ in range(max_x)] for _ in range(max_y)]

    for x, y in coordinates:
        grid[y][x] = "*"

    print_grid(grid)

    return grid


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

    return coordinates, instructions


def count_dot(grid):
    return len(list(filter(lambda x: x == "#", itertools.chain(*grid))))


def process(filename):
    dots, instructions = parse_input(filename)

    print("after")
    for axis, distance in instructions:
        dots = fold(dots, axis, distance)

    print_dots(dots)


def fold(dots, axis, d):
    folded = []
    for x, y in dots:
        if axis == 'x' and x > d:
            x = 2 * d - x
        if axis == 'y' and y > d:
            y = 2 * d - y
        if (x, y) not in folded:
            folded.append((x, y))
    return folded


if __name__ == '__main__':
    process("input.txt")
