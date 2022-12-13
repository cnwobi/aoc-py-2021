import re

from read_input import read_input



def parse_input(filename):
    lines = read_input(filename)
    graph = {}

    for line in lines:
        if "no other bags" in line:
            continue
        tokens = re.findall("\\d*\\s*(\\w+ \\w+) bags?", line)
        insts = re.findall("\\w+ \\w+ (x|y)=(\\d+)", 'fold along y=447')
        graph[tokens[0]] = tokens[1:]

    return graph


def parse_input_2(filename):
    lines = read_input(filename)
    graph = {}

    for line in lines:
        tokens = re.findall("(\\d*)\\s*(\\w+ \\w+) bags?", line)
        graph[tokens[0][1]] = tokens[1:]

    return graph


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


def dfs_2(graph, key='shiny gold'):
    if key == 'no other':
        return 0
    children = graph[key]
    result = 0
    for child in children:
        if child[0]:
            result += (int(child[0]) + (int(child[0]) * dfs_2(graph, child[1])))
    return result


if __name__ == '__main__':
    parse_input("input-2.txt")
    print(search('input-2.txt'))

    print(dfs_2(parse_input_2("input-2.txt")))
