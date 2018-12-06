import re
from collections import defaultdict
from functools import reduce
import bisect
from operator import itemgetter

aoc_input_data = open("input.txt").readlines()

time_regex = re.compile(r'([0-9]+):([0-9]+)')
date_regex = re.compile(r'([0-9]+)-([0-9]+)-([0-9]+)')
guard_id_regex = re.compile(r'#([0-9]+)')


def calculate_asleep_time(hours):
    if hours:
        return reduce(
            (lambda x, y: x + y), [i - k for i, k in zip(hours[-1::-2], hours[-2::-2])])
    return 0


def get_all_minutes(hours):
    result = []
    for t2, t1 in zip(hours[-1::-2], hours[-2::-2]):
        result.extend([minute for minute in range(t1, t2)])
    return result


def collect_data(input_data):
    guard_shifts = defaultdict(list)
    asleep_log = defaultdict(list)

    for data in input_data:
        time_ = tuple([int(t) for t in time_regex.search(data).groups()])
        date_ = tuple([int(d) for d in date_regex.search(data).groups()])

        if "Guard" in data:
            guard_id = guard_id_regex.search(data).groups()[0]
            shift_date = (date_[0], date_[1], date_[2] + 1) if time_[0] == 23 else date_
            guard_shifts[guard_id].append(shift_date)
        else:
            bisect.insort_left(asleep_log[date_], time_[1])

    return guard_shifts, asleep_log


def lazy_dwarfs(input_data):
    guards_shifts, asleep_log = collect_data(input_data)

    guards_data = []
    for dwarf_id_, dates in guards_shifts.items():
        all_asleep_time = reduce(
            (lambda x, y: x + y), [calculate_asleep_time(asleep_log[d]) for d in dates])

        asleep_minutes = []
        for date_ in dates:
            if asleep_log[date_]:
                asleep_minutes.extend(get_all_minutes(asleep_log[date_]))

        most_asleep_minute = max(
            set(asleep_minutes), key=asleep_minutes.count) if asleep_minutes else 0

        guards_data.append((
            dwarf_id_,
            all_asleep_time,
            most_asleep_minute,
            asleep_minutes.count(most_asleep_minute)
        ))

    part_1_winner = max(guards_data, key=itemgetter(1))
    print("Part 1: ", int(part_1_winner[0]) * part_1_winner[2])

    part_2_winner = max(guards_data, key=itemgetter(3))
    print("Part 2: ", int(part_2_winner[0]) * part_2_winner[2])


lazy_dwarfs(aoc_input_data)
