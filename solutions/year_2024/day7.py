def check_equation(answer, equation):
    try:
        prior = equation[0]
    except:
        return False

    return _check_equation(answer, equation[1:], prior)


def _check_equation(answer: int, equation: list, prior):
    try:
        head = equation[0]
    except:
        return prior == answer

    mul_prior = head * prior
    sum_prior = head + prior
    return _check_equation(answer, equation[1:], mul_prior) or _check_equation(
        answer, equation[1:], sum_prior
    )

def part1(input):
    sum = 0
    for line in input.splitlines():
        [answer, equation] = line.split(": ")
        equation = list(map(int, equation.split(" ")))
        answer = int(answer)
        if check_equation(answer, equation):
            print(answer, "OK")
            sum += answer
        else:
            print(answer, "NOK")
    return sum

def check_equation2(answer, equation):
    try:
        prior = equation[0]
    except:
        return False

    return _check_equation2(answer, equation[1:], prior)

def concatenate(a: int, b:int) -> int:
    return int(str(a) + str(b))

def _check_equation2(answer: int, equation: list, prior):
    if prior > answer:
        return False
    try:
        head = equation[0]
    except:
        return prior == answer

    mul_prior = head * prior
    sum_prior = head + prior
    concat_prior = concatenate(prior, head)
    return (
        _check_equation2(answer, equation[1:], mul_prior) or
        _check_equation2(answer, equation[1:], sum_prior) or
        _check_equation2(answer, equation[1:], concat_prior)
    )

def part2(input):
    sum = 0
    for line in input.splitlines():
        [answer, equation] = line.split(": ")
        equation = list(map(int, equation.split(" ")))
        answer = int(answer)
        if check_equation2(answer, equation):
            print(answer, "OK")
            sum += answer
        else:
            print(answer, "NOK")
    return sum


