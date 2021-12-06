from collections import Counter, defaultdict

from read_input import read_input


def next_generation(current_generation):
    next_gen = defaultdict(int)
    for day_to_reproduce, population in current_generation.items():
        if day_to_reproduce == 0:
            next_gen[6] += population
            next_gen[8] += population
            continue
        next_gen[day_to_reproduce - 1] += population
    return next_gen


def star_fish_in_days(filename, days):
    current_generation = Counter(list(map(int, read_input(filename)[0].split(","))))
    for _ in range(days):
        current_generation = next_generation(current_generation)
    return sum(v for v in current_generation.values())


if __name__ == '__main__':
    print(star_fish_in_days("input.txt", 80), star_fish_in_days("input.txt", 256))
