
from typing import List


class Board:
    def __init__(self, grid):
        self.grid = grid
        self.already_won = False
        self.number_dict = {}
        for row in range(5):
            for col in range(5):
                self.number_dict[grid[row][col]] = [row, col]

    def contains(self, draw):
        return draw in self.number_dict

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

    def is_winner(self, draw):
        row, col = self.number_dict[draw]
        self.grid[row][col] = 'x'
        return self.is_complete_col(col) or self.is_complete_row(row)

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
    boards: List[Board] = []
    for line in lines[1:]:
        if not line and not current_board:
            continue
        if not line:
            boards.append(Board(current_board))
            current_board = []
            continue
        row = line.split()
        current_board.append(row)
    boards.append(Board(current_board))
    return lines[0].split(','), boards


def find_bingo(filename):
    lines = read_input(filename)
    draws, boards = generate_boards(lines)
    for draw in draws:
        for board in boards:
            if board.contains(draw) and board.is_winner(draw):
                return board.sum_non_marked() * int(draw)


def find_bingo2(filename):
    lines = read_input(filename)
    draws, boards = generate_boards(lines)
    latest = 0
    for draw in draws:
        for index, board in enumerate(boards):
            if not board.already_won and board.contains(draw) and board.is_winner(draw):
                latest = board.sum_non_marked() * int(draw)
    return latest


if __name__ == '__main__':
    print(find_bingo("input.txt"), find_bingo2("input.txt"))
