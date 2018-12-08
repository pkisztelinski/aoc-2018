with open("input.txt") as f:
    input_data = [int(line.rstrip('\n')) for line in f]

result = None
tmp_add_result = 0
tmp_results = set()

while result is None:
    tmp_results.add(tmp_add_result)

    for data in input_data:
        tmp_add_result += data

        if tmp_add_result in tmp_results:
            result = tmp_add_result
            break

        tmp_results.add(tmp_add_result)

print(result)
