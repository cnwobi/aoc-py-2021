from read_input import read_input


def process_lines(get_relevant_bit, lines):
    n = len(lines[0])
    while len(lines) > 1:
        for i in range(n):
            bit_count_at_index = [0, 0]
            for digits in lines:
                bit_count_at_index[int(digits[i])] += 1
            relevant_bit = get_relevant_bit(bit_count_at_index)
            lines = [digit for digit in lines if digit[i] == relevant_bit]
            if len(lines) == 1:
                return int(lines[0], 2)
    return int(lines[0], 2)


def oxygen_generator_rating(lines):
    return process_lines(lambda bits: "0" if bits[0] > bits[1] else "1", lines)


def CO2_scrubber_rating(lines):
    return process_lines(lambda bits: "0" if bits[0] <= bits[1] else "1", lines)


def life_support_rating(filename):
    lines = read_input(filename)
    return CO2_scrubber_rating(lines) * oxygen_generator_rating(lines)


if __name__ == '__main__':
    print(life_support_rating("input.txt"))
