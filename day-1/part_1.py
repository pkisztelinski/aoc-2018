test_data = [int(line.rstrip('\n'))for line in open('input.txt')]


result = 0
for data in test_data:
    result += data

print(result)
