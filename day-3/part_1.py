import re
import itertools

with open("input.txt") as f:
    aoc_input_data = f.readlines()

position_regex = re.compile(r'([0-9]+),([0-9]+)')
size_regex = re.compile(r'([0-9]+)x([0-9]+)')


def calculate_square_inches(input_data):
    points = set()
    common_points = set()

    for data in input_data:
        position = position_regex.search(data).groups()
        size = size_regex.search(data).groups()

        rectangle = [
            [x for x in range(int(position[0]) + 1, (int(position[0]) + 1) + int(size[0]))],
            [y for y in range(int(position[1]) + 1, (int(position[1]) + 1) + int(size[1]))]
        ]

        for point in itertools.product(rectangle[0], rectangle[1]):
            if point in points:
                common_points.add(point)
            else:
                points.add(point)

    return len(common_points)


print(calculate_square_inches(aoc_input_data))
