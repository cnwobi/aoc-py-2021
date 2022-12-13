import itertools

from read_input import read_input


def get_grid(filename):
    return list(map(lambda line: list(map(int, line)), read_input(filename)))


def increment_energy(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row][col] += 1


def search_possible_spark(grid, sparks=None):
    if sparks is None:
        sparks = [0]
    for row, _ in enumerate(grid):
        for col, _ in enumerate(grid[0]):
            if grid[row][col] > 9:
                dfs(grid, row, col, sparks)


def neighbours(row, col):
    return [(row + i, col + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]


def dfs(grid, x_coord, y_coord, sparks):
    grid[x_coord][y_coord] = 0
    sparks[0] += 1
    for row, col in neighbours(x_coord, y_coord):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 0:
            grid[row][col] += 1
            if grid[row][col] > 9:
                dfs(grid, row, col, sparks)


def total_flashes(steps, filename):
    grid = get_grid(filename)
    sparks = [0]
    for _ in range(steps + 1):
        increment_energy(grid)
        search_possible_spark(grid, sparks)
    return sparks[0]


def all_flashed(grid):
    return not any(filter(lambda x: x != 0, itertools.chain(*grid)))


def get_step_synchronized(filename):
    grid = get_grid(filename)
    times = 0
    while not all_flashed(grid):
        times += 1
        increment_energy(grid)
        search_possible_spark(grid)
    return times


if __name__ == '__main__':
    filename = 'input.txt'
    print(total_flashes(100, filename))
    print(get_step_synchronized(filename))
