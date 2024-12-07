import itertools as it
from dataclasses import dataclass

@dataclass
class Pos:
    x: int
    y: int

    def add_to(self, other):
        return Pos(self.x + other.x, self.y + other.y)

def get_area(input):
    return list(map(list, input.splitlines()))

def mark(area, pos, dir):
    if dir == "now":
        area[pos.y][pos.x] = "G"
    elif dir.x == 1:
        area[pos.y][pos.x] = ">"
    elif dir.x == -1:
        area[pos.y][pos.x] = "<"
    elif dir.y == 1:
        area[pos.y][pos.x] = "V"
    elif dir.y == -1:
        area[pos.y][pos.x] = "^"

def visit(area, pos):
    if pos.x < 0 or pos.y < 0:
        return None
    try:
        return area[pos.y][pos.x]
    except:
        return None

def blockade(area, pos):
    new_area = list(area)
    new_area[pos.y][pos.x] = "#"
    return new_area
    
def get_start_pos(area):
    for y, line in enumerate(area):
        for x, ch in enumerate(line):
            if ch == "^":
                return Pos(x, y)
    return None

def visualize_area(area):
    lines = ["".join(line) for line in area]
    for line in lines:
        print(len(line))
    with open("out.txt", "w+") as file:
        file.write("\n".join(lines))
    

def travel(area, start_position):
    directions = [Pos(0, -1), Pos(1, 0), Pos(0, 1), Pos(-1, 0)] # up, right, down, left

    position = start_position
    visited = {(position.x, position.y)}
    prev_turns = set()
    print(visited)
    for dir in it.cycle(directions):
        while True:
            next_pos = position.add_to(dir)
            obj = visit(area,next_pos)
            if obj == "#":
                break
            elif obj == None:
                visualize_area(area)
                return visited
            else:
                mark(area, position, dir)
                position = next_pos
                mark(area, position, "now")
                visited.add((position.x, position.y))
        # Loops around to next direction
        turn = (position.x, position.y, dir.x, dir.y)
        if turn in prev_turns:
            return None # signifies loop
        prev_turns.add(turn)
        print("Turned: ", turn)


def part1(input):
    area = get_area(input)
    start_pos = get_start_pos(area)
    visited = travel(area, start_pos)
    return len(visited)

def part2(input):
    area = get_area(input)
    start_pos = get_start_pos(area)
    start_pos_tuple = (start_pos.x, start_pos.y)
    visited: set = travel(area, start_pos)
    visited.remove(start_pos_tuple)

    count = 0
    for pos in visited:
        area = get_area(input) # Have to reread due to some overwriting issue..
        blocked_area = blockade(area, Pos(pos[0], pos[1]))
        if not travel(blocked_area, start_pos): # finished by loop
            count += 1
        visualize_area(blocked_area)
    return count
