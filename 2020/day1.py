from read_input import read_input


def three_sum(filename):
    years = sorted(map(int, read_input(filename)))
    for i in range(len(years)):
        if i > 0 and years[i] == years[i - 1]:
            continue
        j = i + 1
        k = len(years) - 1

        while j < k:
            if k == len(years) - 2 and years[k] == years[k + 1]:
                continue
            total = years[i] + years[j] + years[k]
            if total == 2020:
                return years[i] * years[j] * years[k]
            if total > 2020:
                k -= 1
            else:
                j += 1


if __name__ == '__main__':
    print(three_sum("day1.txt"))
