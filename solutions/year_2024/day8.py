import itertools as it
import math

def get_antennas(input) -> dict:
    antennas = dict()
    for y, line in enumerate(input.splitlines()):
        for x, antenna_type in enumerate(line):
            if antenna_type == ".":
                continue
            if antenna_type in antennas:
                antennas[antenna_type].append((x, y))
            else:
                antennas[antenna_type] = [(x, y)]
    return antennas

def get_antinodes(antennas):
    antinodes = []
    for antennas in antennas.values():
       for pair in it.permutations(antennas, 2):
           a = pair[0]
           b = pair[1]
           x_diff = a[0] - b[0]
           y_diff = a[1] - b[1]
           antinodes.append((b[0] - x_diff, b[1] - y_diff))
    return antinodes



def in_field(max_x, max_y, node):
    return (
        0 <= node[0] < max_x and
        0 <= node[1] < max_y
    )

def part1(input):
   max_y = len(input.splitlines())
   max_x = len(input.splitlines()[0]) 

   antennas = get_antennas(input)
   antinodes = get_antinodes(antennas)

   in_field_antinodes = filter(lambda node: in_field(max_x, max_y, node), antinodes)
   return len(set(in_field_antinodes))

def part2(input):
    max_y = len(input.splitlines())
    max_x = len(input.splitlines()[0]) 
    in_field_lambda = lambda node: in_field(max_x, max_y, node)

    def get_harmonics_antinodes(antennas):
        antinodes = set()
        for antennas in antennas.values():
            for pair in it.permutations(antennas, 2):
                a = pair[0]
                b = pair[1]

                antinodes.update(harmonics_line(a, b))
        return antinodes
                

    def harmonics_line(a, b):
        x_diff = a[0] - b[0]
        y_diff = a[1] - b[1]
        lgd = math.gcd(x_diff, y_diff)
        x_diff, y_diff = x_diff / lgd, y_diff / lgd

        above = it.takewhile(in_field_lambda, zip(it.count(a[0], x_diff), it.count(a[1], y_diff)))
        below = it.takewhile(in_field_lambda, zip(it.count(a[0], -x_diff), it.count(a[1], -y_diff)))

        return set(above).union(set(below))

    antennas = get_antennas(input)
    antinodes = get_harmonics_antinodes(antennas)
    return len(antinodes)

