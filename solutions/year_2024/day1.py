
def part1(input): 
    l0s = []
    l1s = []
    for line in input.split("\n"):
        nums = line.strip().split(" ")
        location0 = int(nums[0])
        location1 = int(nums[3])
        # print(location0, location1)
        l0s.append(location0)
        l1s.append(location1)
    
    # now got two lists

    l0s = sorted(l0s)
    l1s = sorted(l1s)

    return sum(map(lambda pair: abs(pair[0] - pair[1]), zip(l0s, l1s)))

def part2(input):
    l0s = []
    l1dict = {}
    for line in input.split("\n"):
        nums = line.strip().split(" ")
        location0 = int(nums[0])
        location1 = int(nums[3])
        # print(location0, location1)
        l0s.append(location0)

        if location1 in l1dict:
            l1dict[location1] += 1
        else:
            l1dict[location1] = 1
    
    return sum(map(lambda loc: loc * l1dict.get(loc, 0), l0s))
