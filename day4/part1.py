

def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    return lines


def generate_grids(lines):
    grids = []
    current_grid = []
    all_numbers = set()
    bingo_boards = []
    for i in range(len(lines)):
        if not lines[i] and not current_grid:
            continue
        if not lines[i]:
            grids.append(current_grid)
            # bingo_boards.append(Bingo(all_numbers, current_grid))
            current_grid = []
            all_numbers = set()
            continue
        row = lines[i].split()
        current_grid.append(row)
        all_numbers.add(row)
    # bingo_boards.append(Bingo(all_numbers, current_grid))
    grids.append(current_grid)
    return grids


def marked_field(draw, grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == draw:
                grid[row][col] = 'x'
                return True
    return False


def is_winner(grid):
    for row in grid:
        if row[0] == 'x' and row.count(row[0]) == len(row):
            return True

    for col in range(len(grid[0])):
        column = []
        for row in range(len(grid)):
            column.append(grid[row][col])
        if column[0] == 'x' and column.count(column[0]) == len(column):
            return True

    return False


def sum_non_marked(grid):
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != 'x':
                total += int(grid[row][col])
    return total


def find_bingo(draws, grids):
    for draw in draws:
        for grid in grids:
            if marked_field(draw, grid) and is_winner(grid):
                return sum_non_marked(grid) * int(draw)


def find_bingo2(draws, grids):
    already_won = set()
    latest = 0
    for draw in draws:
        for index, grid in enumerate(grids):
            if index in already_won:
                continue
            if marked_field(draw, grid) and is_winner(grid):
                latest = sum_non_marked(grid) * int(draw)
                already_won.add(index)
    return latest


def execute(filename):
    lines = read_input(filename)
    draws = lines[0].split(',')
    grids = generate_grids(lines[1:])
    return find_bingo(draws, grids), find_bingo2(draws, grids)


if __name__ == '__main__':
    print(execute("input-2.txt"))
