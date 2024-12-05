from functools import cmp_to_key

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

def part2(input):
    def update_specific_order(ordering, update):
        """Gets a set of pages that need to have arrived before"""
        update = set(update)
        mapping = dict()
        for order in ordering.splitlines():
            parts = list(map(int, order.split("|")))
            before = parts[0]
            after = parts[1]
            if before in update and after in update:
                if after in mapping:
                    mapping[after].add(before)
                else:
                    mapping[after] = {before}
                
                if before in mapping:
                    mapping[after].update(mapping[before])
        return mapping
    
    def page_compare(comes_before_map, a, b):
        if a in comes_before_map and b in comes_before_map[a]:
            return -1
        elif b in comes_before_map and a in comes_before_map[b]:
            return 1
        else:
            return 0

    parts = input.split("\n\n")
    ordering = parts[0]
    updates = parts[1].splitlines()
    sum = 0
    for update in updates:
        update_list = list(map(int, update.split(",")))

        # Lists all parts that must come before 
        comes_before = update_specific_order(ordering, update_list)

        if has_correct_order(comes_before, update_list):
            print("Skipping")
            continue
            
        print("ORIG:" , update_list)
        
        special_key = cmp_to_key(lambda a, b: page_compare(comes_before, a, b))
        sorted_update = sorted(update_list, key=special_key)
        print("SORT:", sorted_update)
        middle = get_middle(sorted_update)
        sum += middle
    return sum


