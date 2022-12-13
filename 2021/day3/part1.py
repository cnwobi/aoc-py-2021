from read_input import read_input


def epsilon(bit_counts):
    result = ["0" if b[0] > b[1] else "1" for b in bit_counts]
    return int(''.join(result), 2)


def gamma(bit_counts):
    result = ["0" if b[0] < b[1] else "1" for b in bit_counts]
    return int(''.join(result), 2)


def count_bit(lines):
    n = len(lines[0])
    # store the number of ones or zeros seen for each index
    bits = [[0, 0] for _ in range(n)]

    for line in lines:
        for i in range(n):
            # increment count accordingly
            bits[i][int(line[i])] += 1
    return bits


def power_consumption(filename):
    lines = read_input(filename)
    bit_count = count_bit(lines)
    return epsilon(bit_count) * gamma(bit_count)


if __name__ == '__main__':
    print(power_consumption("input.txt"))
