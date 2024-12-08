import itertools as it

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


