import heapq
import math
from collections import defaultdict

from read_input import read_input


def get_grid(filename):
    return list(map(lambda line: list(map(int, line)), read_input(filename)))


def get_neighbours(row, col, grid, visited):
    all_neighbours = [(row + i, col + j) for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
    return [(rr, cc) for rr, cc in all_neighbours if should_visit(rr, cc, grid, visited)]


def should_visit(row, col, grid, visited):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in visited


def find_shortest_path(grid):
    best_risk = defaultdict(lambda: math.inf, {(0, 0): 0})
    visited = set()
    visited.add((0, 0))
    q = [(0, 0, 0)]
    while q:
        current_risk, row, col = heapq.heappop(q)
        visited.add((row, col))
        for rr, cc in get_neighbours(row, col, grid, visited):
            new_risk = current_risk + grid[rr][cc]
            if best_risk[(rr, cc)] > new_risk:
                best_risk[(rr, cc)] = new_risk
                heapq.heappush(q, (new_risk, rr, cc))
    return best_risk[(len(grid) - 1, len(grid[0]) - 1)]


def generate_part_2_grid(grid):
    m = len(grid)
    n = len(grid[0])
    return [
        [(grid[i % m][j % n] + j // n + i // m - 1) % 9 + 1 for j in range(n * 5)] for i in range(m * 5)]


if __name__ == '__main__':
    print(find_shortest_path(get_grid("input.txt")))
    print(find_shortest_path(generate_part_2_grid(get_grid("input.txt"))))
