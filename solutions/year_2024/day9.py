import itertools as it

### Part 1
def expand(input):
    def decode_mem(occupied: bool, num: int) -> str:
        if occupied:
            return str(num)
        else:
            return "."

    occupied_iter = it.cycle([True, False])
    return it.chain.from_iterable(
        it.starmap(
            lambda occupied, idx, num: it.repeat(
                decode_mem(occupied, int(idx)), int(num)
            ),
            zip(occupied_iter, it.count(0, 0.5), input),
        )
    )


def merge(expanded):
    i, j = 0, len(expanded) - 1
    merged = []
    while i <= j:
        if expanded[j] == ".":
            j -= 1
        elif expanded[i] == ".":
            merged.append(expanded[j])
            j -= 1
            i += 1
        else:
            merged.append(expanded[i])
            i += 1
    return merged


def part1(input):
    merged = merge(list(expand(input)))
    return sum(it.starmap(lambda i, b: i * int(b), enumerate(merged)))

## Part 2


def part2(input):
    hard_drive = listify(input)
    print(hard_drive)
    i, j = 0, len(hard_drive) - 1
    current_block = None
    size_to_find = 0
    while i <= j:
        current_block = hard_drive[j]
        if current_block[1] == True: # Is a memory block 
            size_to_find = current_block[2]

            for ii in range(j):
                possible_hole = hard_drive[ii]
                if possible_hole[1] == False:
                    if possible_hole[2] == size_to_find:
                        possible_hole[1] = True
                        possible_hole[0] = current_block[0]
                    if possible_hole[2] >= size_to_find:
                        possible_hole[1] = True
                        possible_hole[0] = current_block[0]
                        hard_drive.insert(ii, (current_block[0], False, possible_hole[2] - current_block[2]))
                        break
                    current_block[1] = False
        j -= 1
            

        

def listify(input):
    occupied_iter = it.cycle([True, False])
    block_idx = map(int, it.count(0, 0.5))
    size_iter = map(int, input)
    idx_occupied_size_iter = zip(block_idx, occupied_iter, size_iter)
    hard_drive = [(idx, occupied, size) for idx, occupied, size in idx_occupied_size_iter]
    return hard_drive





