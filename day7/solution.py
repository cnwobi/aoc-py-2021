import math
from collections import Counter

from read_input import read_input


def minimum_fuel_cost_1(input_array):
    position_frequency = Counter(input_array)
    unique_positions = list(position_frequency.keys())
    global_min = math.inf
    for anchor_position in unique_positions:
        pair_max = 0
        for current_position in unique_positions:
            pair_max += (abs(anchor_position - current_position) * position_frequency[current_position])
        global_min = min(global_min, pair_max)
    return global_min


def sum_natural_numbers(n):
    return n * (n + 1) // 2


def minimum_fuel_cost_2(input_array):
    position_frequency = Counter(input_array)
    unique_positions = list(position_frequency.keys())
    max_element = max(unique_positions)
    global_max = math.inf

    for anchor_position in range(max_element + 1):
        pair_max = 0
        for current_position in unique_positions:
            pair_max += (sum_natural_numbers(abs(current_position - anchor_position)) *
                         position_frequency[current_position])
        global_max = min(global_max, pair_max)

    return global_max


def execute(filename):
    input_array = list(map(int, read_input(filename)[0].split(',')))

    return minimum_fuel_cost_1(input_array), minimum_fuel_cost_2(input_array)


if __name__ == '__main__':
    print(execute('input.txt'))
