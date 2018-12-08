with open("input.txt") as f:
    input_data = [line.rstrip('\n') for line in f][0]


def create_polymer_or_something(data):
    text_tmp = []
    for c in data:
        if text_tmp and ((c.upper() == text_tmp[-1].upper()) and (c != text_tmp[-1])):
            text_tmp.pop()
        else:
            text_tmp.append(c)
    return text_tmp


def calculate_part2(data):
    parsed_chars = set()
    results = set()
    for c in data:
        if c.upper() not in parsed_chars:
            tmp_text = data.replace(c.upper(), "")
            tmp_text = tmp_text.replace(c.lower(), "")
            results.add(len(create_polymer_or_something(tmp_text)))
            parsed_chars.add(c.upper())

    return results


print("Part 1: ", len(create_polymer_or_something(input_data)))
print("Part 2: ", min(calculate_part2(input_data)))
