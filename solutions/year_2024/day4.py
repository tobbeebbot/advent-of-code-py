
def diagonal(index, lines, dir="normal"):
    start_column = max(index, 0)
    start_line = -min(index, 0)
    line_length = len(lines[0])

    col_indices = range(start_column, line_length)
    if dir == "normal":
        diagonal = list((line[i] for i, line in zip(col_indices, lines[start_line:])))
    else:
        diagonal = list((list(reversed(line))[i] for i, line in zip(col_indices, lines[start_line:])))
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


def part2():
    pass
