from typing import List


class Board:
    def __init__(self, all_numbers, grid):
        self.all_numbers = all_numbers
        self.grid = grid
        self.already_won = False

    def contains(self, draw):
        return draw in self.all_numbers

    def is_complete_row(self, row):
        if self.grid[row][0] == 'x' and self.grid[row].count(self.grid[row][0]) == 5:
            self.already_won = True
            return True
        return False

    def is_complete_col(self, col):
        column = []
        for row in range(5):
            column.append(self.grid[row][col])
        if column[0] == 'x' and column.count(column[0]) == len(column):
            self.already_won = True
            return True
        return False

    def is_marked_and_winner(self, draw):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == draw:
                    self.grid[row][col] = 'x'
                    return self.is_complete_col(col) or self.is_complete_row(row)
        return False

    def sum_non_marked(self):
        total = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] != 'x':
                    total += int(self.grid[row][col])
        return total


def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    return lines


def generate_boards(lines):
    current_board = []
    all_numbers = set()
    boards: List[Board] = []
    for line in lines[1:]:
        if not line and not current_board:
            continue
        if not line:
            boards.append(Board(all_numbers, current_board))
            current_board = []
            all_numbers = set()
            continue
        row = line.split()
        current_board.append(row)
        all_numbers.update(row)
    boards.append(Board(all_numbers, current_board))
    return lines[0].split(','), boards


def find_bingo(filename):
    lines = read_input(filename)
    draws, boards = generate_boards(lines)
    for draw in draws:
        for board in boards:
            if board.contains(draw) and board.is_marked_and_winner(draw):
                return board.sum_non_marked() * int(draw)


def find_bingo2(filename):
    lines = read_input(filename)
    draws, boards = generate_boards(lines)
    latest = 0
    for draw in draws:
        for index, board in enumerate(boards):
            if board.already_won:
                continue
            if board.contains(draw) and board.is_marked_and_winner(draw):
                latest = board.sum_non_marked() * int(draw)
    return latest


if __name__ == '__main__':
    print(find_bingo("input.txt"), find_bingo2("input.txt"))
