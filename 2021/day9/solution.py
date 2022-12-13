from functools import reduce

from read_input import read_input


def is_low_point(grid, row, col):
    return ((row - 1 < 0 or grid[row][col] < grid[row - 1][col]) and (
            row + 1 >= len(grid) or grid[row][col] < grid[row + 1][col]) and (
                    col - 1 < 0 or grid[row][col] < grid[row][col - 1]) and (
                    col + 1 >= len(grid[0]) or grid[row][col] < grid[row][col + 1]))


def find_basins(grid):
    low_point = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if is_low_point(grid, row, col):
                low_point.append(dfs(grid, row, col))

    return reduce(lambda a, b: a * b, sorted(low_point, reverse=True)[:3])


def dfs(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 9 or grid[row][col] == -1:
        return 0
    grid[row][col] = -1

    return 1 + dfs(grid, row - 1, col) + dfs(grid, row + 1, col) + dfs(grid, row, col - 1) + dfs(grid, row, col + 1)


def find_low_point(grid):
    low_point = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if is_low_point(grid, row, col):
                low_point.append(grid[row][col])

    return sum(map(lambda x: x + 1, low_point))


def get_grid(filename):
    return list(map(lambda line: list(map(int, line)), read_input(filename)))


def execute(filename):
    grid = get_grid(filename)
    return find_low_point(grid), find_basins(grid)


if __name__ == '__main__':
    print(execute('small.txt'))
