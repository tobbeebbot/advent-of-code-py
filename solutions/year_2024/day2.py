import itertools as it


def is_safe_increasing(report):
    return all(map(lambda pair: 1 <= pair[0] - pair[1] <= 3, it.pairwise(report)))


def is_safe_decreasing(report):
    return is_safe_increasing(reversed(report))


def is_safe(report):
    return is_safe_increasing(report) or is_safe_decreasing(report)


def is_altered_safe(report):
    return any(map(is_safe, it.combinations(report, len(report) - 1)))


def into_report(line):
    return list(map(int, line.split()))


def part1(input: str):
    return sum(1 for _ in filter(is_safe, map(into_report, input.splitlines())))


def part2(input):
    return sum(1 for _ in filter(is_altered_safe, map(into_report, input.splitlines())))
