from functools import reduce

with open("input.txt") as f:
    input_data = [int(line.rstrip('\n')) for line in f]


print(reduce(lambda x, y: x + y, input_data))
