from collections import defaultdict

from read_input import read_input


def parse_line(filename):
    graph = defaultdict(list)
    lines = read_input(filename)

    for line in lines:
        nodes = line.split("-")
        graph[nodes[0]].append(nodes[1])
        graph[nodes[1]].append(nodes[0])
    return graph


def seen_twice(seen):
    return len([x for x in seen.values() if x == 2]) > 0


def paths_in_cave_small_caves_at_most_once(graph, node='start', seen=set(), path="start", result=0):
    if node in seen:
        return result

    if node == "end":
        return result + 1

    if node.islower() or node == 'start':
        seen.add(node)

    for child in graph[node]:
        result = paths_in_cave_small_caves_at_most_once(graph, child, seen, path + "-" + child, result)

    if node in seen:
        seen.remove(node)

    return result


def paths_in_cave_small_caves_at_most_twice(graph, key='start', seen=defaultdict(int), visited_any_small_cave_twice=[False], result=0):
    if key in seen and (visited_any_small_cave_twice[0] or key == 'start'):
        return result

    if key == "end":
        return result + 1

    if key.islower():
        seen[key] += 1
        if seen[key] == 2:
            visited_any_small_cave_twice[0] = True

    for child in graph[key]:
        result = paths_in_cave_small_caves_at_most_twice(graph, child, seen, visited_any_small_cave_twice, result)

    if key in seen:
        if seen[key] == 2:
            visited_any_small_cave_twice[0] = False
        seen[key] -= 1
        if seen[key] == 0:
            del seen[key]
    return result


if __name__ == '__main__':
    print(paths_in_cave_small_caves_at_most_once(parse_line('input.txt')))
    print(paths_in_cave_small_caves_at_most_twice(parse_line('input.txt')))
