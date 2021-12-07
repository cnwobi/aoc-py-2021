import re

from read_input import read_input


def parse_input(filename):
    lines = read_input(filename)
    graph = {}

    for line in lines:
        if "no other bags" in line:
            continue

        tokens = re.findall("\\d*\\s*(\\w+ \\w+) bags?", line)
        graph[tokens[0]] = tokens[1:]

    print(graph)


if __name__ == '__main__':
    parse_input("input-2.txt")
