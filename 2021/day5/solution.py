from collections import Counter

from read_input import read_input


def get_delta(p0, p1):
    if p1 == p0:
        return 0
    return -1 if p0 > p1 else 1


def get_coordinate_from_point(point_str):
    x, y = point_str.split(',')
    return int(x), int(y)


def points_on_line(coordinates):
    x0, y0, x1, y1 = coordinates
    delta_x = get_delta(x0, x1)
    delta_y = get_delta(y0, y1)
    points = [(x0, y0)]
    while (x0, y0) != (x1, y1):
        x0 += delta_x
        y0 += delta_y
        points.append((x0, y0))
    return points


def to_line_segment(line):
    point1, point2 = line.split("->")
    x0, y0 = get_coordinate_from_point(point1)
    x1, y1 = get_coordinate_from_point(point2)
    return x0, y0, x1, y1


def generate_vertical_and_horizontal_segments(filename):
    lines = read_input(filename)

    return list(map(points_on_line,
                    filter(lambda coord: coord[0] == coord[2] or coord[1] == coord[3], map(to_line_segment, lines))))


def generate_all_segments(filename):
    lines = read_input(filename)

    return list(map(points_on_line, map(to_line_segment, lines)))


def overlapping_points_count(filename, segment_generator):
    line_segments = segment_generator(filename)
    all_lines = []
    for line_segment in line_segments:
        all_lines.extend(line_segment)
    return len([k for k, v in Counter(all_lines).items() if v >= 2])


def execute(filename):
    return overlapping_points_count(filename, generate_vertical_and_horizontal_segments), overlapping_points_count(
        filename, generate_all_segments)


if __name__ == '__main__':
    print(execute("input (1).txt"))
