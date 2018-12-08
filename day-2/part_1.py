with open("input.txt") as f:
    input_data = [line.rstrip('\n') for line in f]

result = {2: set(), 3: set()}

for data in input_data:
    for letter in data:
        count_letter = data.count(letter)
        index = result.get(count_letter, None)

        if index is not None and data not in index:
            index.add(data)

print(len(result[2]) * len(result[3]))
