input_data = [line.rstrip('\n') for line in open('input.txt')][0]


text_tmp = []
for c in input_data:
    if text_tmp and ((c.upper() == text_tmp[-1].upper()) and (c != text_tmp[-1])):
        text_tmp.pop()
    else:
        text_tmp.append(c)

print("Part 1: ", len(text_tmp))
