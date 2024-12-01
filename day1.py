import argparse

def solve_part1(input):
    print("solving part 1")
    
    l0s = []
    l1s = []
    for line in input:
        nums = line.strip().split(" ")
        location0 = int(nums[0])
        location1 = int(nums[3])
        # print(location0, location1)
        l0s.append(location0)
        l1s.append(location1)
    
    # now got two lists

    l0s = sorted(l0s)
    l1s = sorted(l1s)

    print(sum(map(lambda pair: abs(pair[0] - pair[1]), zip(l0s, l1s))))

def solve_part2(input):
    print("solving part 2")
    
    l0s = []
    l1dict = {}
    for line in input:
        nums = line.strip().split(" ")
        location0 = int(nums[0])
        location1 = int(nums[3])
        # print(location0, location1)
        l0s.append(location0)

        if location1 in l1dict:
            l1dict[location1] += 1
        else:
            l1dict[location1] = 1
    
    print(sum(map(lambda loc: loc * l1dict.get(loc, 0), l0s)))

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--part" , type=int, default=0)
    args = args.parse_args()

    with open("inputs/day1.txt") as file:
        input_text = file.readlines()

    if args.part == 0:
        solve_part1(input_text)
    elif args.part == 1:
        solve_part2(input_text)
    else:
        print("error")
