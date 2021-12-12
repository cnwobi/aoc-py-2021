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


def paths_in_cave_small_caves_at_most_once(graph, key='start', seen=set(), path="start", result=[]):
    if key in seen:
        return result

    if key == "end":
        result.append(path)
        return result

    if key.islower() or key == 'start':
        seen.add(key)

    for child in graph[key]:
        result = paths_in_cave_small_caves_at_most_once(graph, child, seen, path + "-" + child, result)

    if key in seen:
        seen.remove(key)

    return result


def paths_in_cave_small_caves_at_most_twice(graph, key='start', seen=defaultdict(int), path="start", result=0):
    if key in seen and (seen_twice(seen) or key == 'start'):
        return result

    if key == "end":
        result.append(path)
        return result

    if key.islower() or key == 'start':
        seen[key] += 1

    for child in graph[key]:
        result = paths_in_cave_small_caves_at_most_twice(graph, child, seen, path + "-" + child, result)

    if key in seen:
        seen[key] -= 1
        if seen[key] == 0:
            del seen[key]
    return result


if __name__ == '__main__':
    print(len(paths_in_cave_small_caves_at_most_twice(parse_line('input.txt'))))
