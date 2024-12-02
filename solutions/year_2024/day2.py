
def is_safe_increasing(nums):
    length = len(nums)
    if length == 2:
        return 1 <= (nums[1] - nums[0]) <= 3
    if length == 1:
        return True
    else:
        return is_safe_increasing(nums[:length // 2 + 1]) and is_safe_increasing(nums[length//2:])


def is_safe(nums):
    return is_safe_increasing(nums) or is_safe_increasing(list(reversed(nums)))


def part1(input:str):
    count = 0
    for line in input.splitlines():
        report = list(map(int, line.split()))
        safe = is_safe((report))
        count += safe
    return count

def part2(input):
    count = 0
    for line in input.splitlines():
        report = list(map(int, line.split()))
        for i, _ in enumerate(report):
            if is_safe(report[:i] + report[i + 1:]):
                count += 1
                break
            
    return count