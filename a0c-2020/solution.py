from read_input import read_input


def parse_input(filename):
    lines = read_input(filename)

    for line in lines:
        bag, rest = line.split("contain")
        print(bag)


if __name__ == '__main__':
    parse_input("input.txt")
