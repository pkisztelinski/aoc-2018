import itertools
from collections import defaultdict
from functools import reduce

with open("input.txt") as file:
    input_data = set([
        tuple(int(point) for point in l.rstrip('\n').split(', '))
        for l in file.readlines()])


def calculate_distance(point, goal):
    return abs(point[0] - goal[0]) + abs(point[1] - goal[1])


def calculate_shortest_distance(point, goals):
    distance_result = None
    goals_result = set()

    for goal in goals:
        distance = calculate_distance(point, goal)

        if distance_result is None or distance < distance_result:
            distance_result = distance
            goals_result.clear()
            goals_result.add(goal)
        if distance == distance_result:
            goals_result.add(goal)

    return goals_result, distance_result


def check_if_infinite(point, x1x1, x2x2):
    if (point[0] in (x1x1[0], x2x2[0])) or (point[1] in (x1x1[1], x2x2[1])):
        return True
    return False


def get_xy_points(data):
    x1y1 = (min([p[0] for p in data]) - 1, min([p[1] for p in data]) - 1)
    x2y2 = (max([p[0] for p in data]) + 1, max([p[1] for p in data]) + 1)

    return x1y1, x2y2


def get_xy_lines(x1y1, x2y2):
    x_line = tuple([x for x in range(x1y1[0], x2y2[0] + 1)])
    y_line = tuple([x for x in range(x1y1[1], x2y2[1] + 1)])

    return x_line, y_line


def part_1(data):
    x1y1, x2y2 = get_xy_points(data)
    x_line, y_line = get_xy_lines(x1y1, x2y2)

    best_points = defaultdict(set)
    infinite_goals = set()

    for point in itertools.product(x_line, y_line):
        goals, distance = calculate_shortest_distance(point, data)

        if len(goals) > 1:
            continue

        for goal in goals:
            best_points[goal].add(point)

    finite_goals = data - infinite_goals

    return max([len(best_points[g]) for g in finite_goals])


def part_2(data):
    x1y1, x2y2 = get_xy_points(data)
    x_line, y_line = get_xy_lines(x1y1, x2y2)

    result = 0
    for point in itertools.product(x_line, y_line):
        distance = reduce(
            lambda x, y: x + y, [calculate_distance(point, goal) for goal in data])

        if distance < 10000:
            result += 1

    return result


print(part_1(input_data))
print(part_2(input_data))
