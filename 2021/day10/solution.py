from functools import reduce

from read_input import read_input


def can_close(stack, character):
    return stack and ((stack[-1] == '{' and character == '}') or
                      (stack[-1] == '[' and character == ']') or
                      (stack[-1] == '(' and character == ')') or
                      (stack[-1] == '<' and character == '>'))


def complete_line(line):
    score_symbol_map = {'(': 1, '[': 2, '{': 3, '<': 4}
    stack = []
    for character in line:
        if character in {'[', '(', '{', '<'}:
            stack.append(character)
            continue
        if can_close(stack, character):
            stack.pop()
        else:
            return 0
    return reduce(lambda x, y: x * 5 + y, map(lambda x: score_symbol_map[x], stack[::-1]))


def first_illegal_character_value(line):
    points_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    stack = []
    for character in line:
        if character in {'[', '(', '{', '<'}:
            stack.append(character)
            continue
        if can_close(stack, character):
            stack.pop()
        else:
            return points_map[character]
    return 0


def calculate_parsing_error(filename):
    return sum(map(first_illegal_character_value, read_input(filename)))


def calculate_autocomplete(filename):
    ans = sorted(list(filter(lambda x: x != 0, map(complete_line, read_input(filename)))))
    mid = len(ans) // 2
    return ans[mid]


if __name__ == '__main__':
    print(calculate_parsing_error('small.txt'))
    print(calculate_autocomplete('small.txt'))
