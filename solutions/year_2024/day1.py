from collections import Counter


def get_nums_from_line(line: str):
    parts = line.strip().split(" ")
    return int(parts[0]), int(parts[3])


def get_lists_from_input(input: str):
    return zip(*map(get_nums_from_line, input.splitlines()))


def part1(input):
    locations1, locations2 = get_lists_from_input(input)

    locations1 = sorted(locations1)
    locations2 = sorted(locations2)

    return sum(map(lambda pair: abs(pair[0] - pair[1]), zip(locations1, locations2)))


def part2(input: str):
    locations1, locations2 = get_lists_from_input(input)

    locations2_counts = Counter(locations2)

    return sum(map(lambda loc: loc * locations2_counts.get(loc, 0), locations1))
