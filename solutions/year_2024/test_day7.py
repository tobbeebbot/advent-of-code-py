import day7
def test_equation_check():

    equation = [10, 19]
    answer = 190
    assert day7.check_equation(answer, equation) == True


    answer = 190
    equation = [10, 19]
    assert day7.check_equation(answer, equation) == True
    answer = 3267
    equation = [81, 40, 27]
    assert day7.check_equation(answer, equation) == True
    answer = 192
    equation = [17, 8, 14]
    assert day7.check_equation(answer, equation) == False
    answer = 83
    equation = [17, 5]
    assert day7.check_equation(answer, equation) == False
    answer = 156
    equation = [15, 6]
    assert day7.check_equation(answer, equation) == False
    answer = 7290
    equation = [6, 8, 6, 15]
    assert day7.check_equation(answer, equation) == False
    answer = 161011
    equation = [16, 10, 13]
    assert day7.check_equation(answer, equation) == False
    answer = 21037
    equation = [9, 7, 18, 13]
    assert day7.check_equation(answer, equation) == False
    answer = 292
    equation = [11, 6, 16, 20]
    assert day7.check_equation(answer, equation) == True