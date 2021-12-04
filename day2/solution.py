from read_input import read_input


class Position:

    def __init__(self, commands):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        self.commands = commands

    def process_command(self, command):
        direction, val = command.split(" ")
        if direction == 'forward':
            self.horizontal += int(val)
            return
        if direction == 'up':
            self.depth -= int(val)
            return
        self.depth += int(val)

    def process_command2(self, command):
        direction, val = command.split(" ")
        if direction == 'forward':
            self.horizontal += int(val)
            self.depth += (self.aim * int(val))
            return
        if direction == 'up':
            self.aim -= int(val)
            return
        self.aim += int(val)

    def result1(self):
        for command in self.commands:
            self.process_command(command)
        return self.horizontal * self.depth

    def result2(self):
        for command in self.commands:
            self.process_command2(command)
        return self.horizontal * self.depth


def part2(filename):
    return Position(read_input(filename)).result2()


def part1(filename):
    return Position(read_input(filename)).result1()


if __name__ == '__main__':
    print(part2("input.txt"))
