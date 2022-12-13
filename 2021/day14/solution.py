from collections import Counter

from read_input import read_input


def parse_input(filename):
    lines = read_input(filename)

    return lines[0], dict(map(lambda x: x.split(" -> "), lines[2:]))


def new_pairs(instructions, old_pair):
    return old_pair[0] + instructions[old_pair], instructions[old_pair] + old_pair[1]


def process(filename, steps=10):
    sequence, instructions = parse_input(filename)

    pairs_freq = Counter([a + b for a, b in zip(sequence, sequence[1:])])

    for i in range(steps):
        items = list(pairs_freq.items())
        for pair, count in items:
            new_pair1, new_pair2 = new_pairs(instructions, pair)

            pairs_freq[new_pair1] += count
            pairs_freq[new_pair2] += count
            pairs_freq[pair] -= count

    frequency = Counter('')

    for pair, count in pairs_freq.items():
        frequency[pair[1]] += count

    frequency[sequence[0]] += 1

    most_common, least_common = frequency.most_common()[0][1], frequency.most_common()[-1][1]

    return most_common - least_common


if __name__ == '__main__':
    print(process("input.txt", 40))
