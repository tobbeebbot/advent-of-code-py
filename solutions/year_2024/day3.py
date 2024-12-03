import re

def part1(input):
    def get_muls(str_input):
        matches = re.finditer(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", str_input)
        return map(lambda match: match.groups(0), matches)

    muls = get_muls(input)
    return sum(map(lambda mul: int(mul[0]) * int(mul[1]), muls))

def part2(input):
    def get_commands(str_input):
        return re.finditer(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don't\(\)", str_input)
        
    commands: list[re.Match] = get_commands(str_input= input)
    is_do = True
    mul_sum = 0
    for command in commands:
        pattern = command.group(0)
        print(pattern)
        if pattern.startswith("mul") and is_do:
            mul_sum += int(command.group(1)) * int(command.group(2))
        elif pattern.startswith("don't"):
            is_do = False
        elif pattern.startswith("do"):
            is_do = True
        else:
            continue
    return mul_sum
