import itertools

from read_input import read_input


def count_unique_segments(filename):
    return len(list(filter(lambda x: len(x) in {2, 4, 3, 7},
                           itertools.chain(*map(lambda l: l.split("|")[1].split(),
                                                read_input(filename))))))


def parse_lines(filename):
    return list(map(lambda l: l.split("|"), read_input(filename)))


def unique_digits(signals):
    unique = {len(x): x for x in list(filter(lambda s: len(s) in {2, 4, 3, 7}, signals))}
    return unique[2], unique[3], unique[4], unique[7]


def find_zero(signals, one, four):
    return list(filter(lambda x: not four.issubset(x),
                       filter(lambda x: one.issubset(x), filter(lambda x: len(x) == 6, signals))))[0]


def find_six(zero, one, signals):
    return list(filter(lambda x: len(x) == 6 and x != zero and not one.issubset(x), signals))[0]


def find_nine(zero, six, signals):
    return list(filter(lambda x: len(x) == 6 and x != zero and x != six, signals))[0]


def decode(mapping, regular):
    return frozenset(map(lambda l: mapping[l], regular))


def generate_mapping(zero, one, four, six, seven, eight, nine):
    mapping = {'a': next(iter(seven.difference(one))),
               'd': next(iter(eight.difference(zero))),
               'e': next(iter(eight.difference(nine))),
               'g': next(iter(nine.difference(four).difference(seven)))}
    missing_in_six = next(iter(eight.difference(six)))
    mapping['c'] = missing_in_six
    mapping['f'] = next(iter(one.difference(missing_in_six)))
    mapping['b'] = next(iter(eight.difference(mapping.values())))
    return mapping


def get_digits(signals):
    one, seven, four, eight = unique_digits(signals)
    zero = find_zero(signals, one, four)
    six = find_six(zero, one, signals)
    nine = find_nine(zero, six, signals)
    eight = list(filter(lambda x: len(x) == 7, signals))[0]

    mapping = generate_mapping(zero, one, four, six, seven, eight, nine)
    five = decode(mapping, 'abdfg')
    two = decode(mapping, 'acdeg')
    three = decode(mapping, 'acdfg')
    return zero, one, two, three, four, five, six, seven, eight, nine


def process_line(line):
    digits = list(map(frozenset, line[1].split()))
    signals = list(map(frozenset, line[0].split()))
    segment_digits = {x: index for index, x in enumerate(get_digits(signals))}
    return int(''.join(list(map(lambda segment: str(segment_digits[segment]), digits))))


if __name__ == '__main__':
    print(count_unique_segments("input.txt"))
    print(sum(list(map(process_line, parse_lines('input.txt')))))
