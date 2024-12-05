
def ordering_to_map(ordering):
    mapping = dict()
    for order in ordering.splitlines():
        parts = list(map(int, order.split("|")))
        before = parts[0]
        after = parts[1]
        if after in mapping:
            mapping[after].add(before)
        else:
            mapping[after] = {before}
    return mapping

def has_correct_order(order_mapping, update):
    visited = set()
    for page in update:
        needed_before:set = order_mapping.get(page, set())
        if not needed_before.intersection(update).issubset(visited):
            return False
        visited.add(page)

    return True

def get_middle(update):
    middle = update[len(update) // 2]
    return middle


def to_int_list(update):
    str_nums = update.split(",")
    return list(map(int, str_nums))

def part1(input):
    parts = input.split("\n\n")
    ordering = parts[0]
    updates = parts[1]

    order_mapping = ordering_to_map(ordering)

    return sum(
        map(
            get_middle,
            filter(
                lambda update: has_correct_order(order_mapping, update),
                map(
                    to_int_list,
                    updates.splitlines()
                )
            )
        )
    )
