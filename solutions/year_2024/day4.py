import itertools as it


def diagonal(index, lines, dir="normal"):
    start_column = max(index, 0)
    start_line = -min(index, 0)
    line_length = len(lines[0])

    col_indices = range(start_column, line_length)
    if dir == "normal":
        diagonal = list((line[i] for i, line in zip(col_indices, lines[start_line:])))
    else:
        diagonal = list(
            (
                list(reversed(line))[i]
                for i, line in zip(col_indices, lines[start_line:])
            )
        )
    return "".join(diagonal)


def diagonals(lines, dir="normal"):
    num_lines = len(lines)
    num_cols = len(lines[0])
    return [diagonal(i, lines, dir) for i in range(-num_lines + 1, num_cols)]


def count_front_and_back(text):
    return text.count("XMAS") + text.count("SAMX")


def part1(input):
    lines = list(input.splitlines())

    columns = []
    for col_idx in range(len(lines)):
        column = ""
        for line in lines:
            column += line[col_idx]
        columns.append(column)

    return (
        sum(count_front_and_back(line) for line in lines)
        + sum(count_front_and_back(col) for col in columns)
        + sum(count_front_and_back(dia) for dia in diagonals(lines))
        + sum(count_front_and_back(dia) for dia in diagonals(lines, dir="reversed"))
    )


def find_indices(char_key, line):
    return [i for i, c in enumerate(line) if c == char_key]


def look(grid, x, y):
    if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
        print("XXXXXX")
        return "X"
    else:
        val = grid[y][x]
        print("Saw", val)
        return val


def look_north_west(grid, x, y):
    look_x = x - 1
    look_y = y - 1
    return look(grid, look_x, look_y)


def look_north_east(grid, x, y):
    look_x = x + 1
    look_y = y - 1
    return look(grid, look_x, look_y)


def look_south_west(grid, x, y):
    look_x = x - 1
    look_y = y + 1
    return look(grid, look_x, look_y)


def look_south_east(grid, x, y):
    look_x = x + 1
    look_y = y + 1
    return look(grid, look_x, look_y)


def is_mas_mas(grid, x, y):
    print("NW and SE")
    lr = look_north_west(grid, x, y) == "M" and look_south_east(grid, x, y) == "S"
    lr = lr or (
        look_north_west(grid, x, y) == "S" and look_south_east(grid, x, y) == "M"
    )
    print("NE and SW")
    rl = look_north_east(grid, x, y) == "M" and look_south_west(grid, x, y) == "S"
    rl = rl or (
        look_north_east(grid, x, y) == "S" and look_south_west(grid, x, y) == "M"
    )
    print("Result", lr and rl, "\n")
    return lr and rl


def part2(input):
    xmax_grid = [line for line in input.splitlines()]

    a_locations = it.chain.from_iterable(
        it.starmap(
            lambda i, line: zip(it.repeat(i), find_indices("A", line)),
            enumerate(xmax_grid),
        )
    )

    num_mas_mas = sum(it.starmap(lambda y, x: is_mas_mas(xmax_grid, x, y), a_locations))

    return num_mas_mas
