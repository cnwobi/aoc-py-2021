from read_input import read_input


def count_increase(filename):
    count = 0
    lines = read_input(filename)

    for i in range(1,len(lines)):
        if lines[i-1] > lines[i]:
            count += 1
    return count


def count_sliding_window(filename):
    sum_window = 0
    count = 0
    lines = read_input(filename)
    for index, line in enumerate(lines):
        if index < 3:
            sum_window += int(line)
            continue
        last_window = sum_window
        sum_window += int(lines[index]) - int(lines[index - 3])
        if sum_window > last_window:
            count += 1
    return count


if __name__ == '__main__':
    print(count_sliding_window("input.txt"))
