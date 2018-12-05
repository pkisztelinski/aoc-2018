import re

aoc_input_data = open("input.txt").readlines()

index_regex = re.compile(r'#([0-9]+)')
position_regex = re.compile(r'([0-9]+),([0-9]+)')
size_regex = re.compile(r'([0-9]+)x([0-9]+)')


def check_overlap(rec_1, rec_2):
    if (rec_1[0] > rec_2[1] or rec_1[1] < rec_2[0]) \
            or (rec_1[2] > rec_2[3] or rec_1[3] < rec_2[2]):
        return False
    return True


def search_rectangle_doesnt_overlap(input_data):
    rectangles = {}

    for data in input_data:
        index = index_regex.search(data).groups()
        position = position_regex.search(data).groups()
        size = size_regex.search(data).groups()

        rectangle = (
            int(position[0]) + 1, int(position[0]) + int(size[0]),  # x
            int(position[1]) + 1, int(position[1]) + int(size[1]),  # y
            index[0]
        )

        rectangles[rectangle] = False

        for other_rectangle in rectangles.keys():
            if other_rectangle == rectangle:
                continue

            if check_overlap(rectangle, other_rectangle) is True:
                rectangles[rectangle] = True
                rectangles[other_rectangle] = True
                continue

    return [rect_data[4] for rect_data, is_overlap in rectangles.items() if not is_overlap]


print(search_rectangle_doesnt_overlap(input_data=aoc_input_data))
