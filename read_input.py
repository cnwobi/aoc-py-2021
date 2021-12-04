def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    return lines
