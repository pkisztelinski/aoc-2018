input_data = [line.rstrip('\n') for line in open('input.txt')]

while len(input_data) > 0:
    id_ = input_data.pop()

    for next_id in input_data:
        differs = 0
        for i in range(len(id_)):
            if id_[i] != next_id[i]:
                differs += 1

        if differs == 1:
            print("".join([x for x, y in zip(id_, next_id) if x == y]))
