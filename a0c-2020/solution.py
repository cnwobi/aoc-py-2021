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

    return graph


def parse_input_2(filename):
    lines = read_input(filename)
    graph = {}

    for line in lines:
        tokens = re.findall("(\\d*)\\s*(\\w+ \\w+) bags?", line)
        print(tokens)


def dfs(graph, key):
    if key == 'shiny gold':
        return True
    if key not in graph:
        return False
    values = graph[key]
    shinny_bag = False
    for bag in values:
        shinny_bag = shinny_bag or dfs(graph, bag)
    return shinny_bag


def search(filename):
    graph = parse_input(filename)
    parse_input_2(filename)
    keys = filter(lambda k: k != 'shiny gold', list(graph.keys()))
    return len(list(filter(lambda k: dfs(graph, k), keys)))


if __name__ == '__main__':
    parse_input("input-2.txt")
    print(search('input-2.txt'))
