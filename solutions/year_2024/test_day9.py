import day9

input = "2333133121414131402"
expanded = "00...111...2...333.44.5555.6666.777.888899"
merged = "0099811188827773336446555566"

def test_expand():
    output = "".join(day9.expand(input))
    assert output == expanded

def test_merge():
    assert "".join(day9.merge(expanded)) == merged

def test_part1():
    assert day9.part1(input) == 1928
    