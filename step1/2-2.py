def print_calc_result(calc):
    print("{0} -> {1}".format(calc, eval(calc)))

print_calc_result("1.2 + 3.8") # 5.0
print_calc_result("10 // 100") # 0
print_calc_result("1 >= 0") # True
print_calc_result("'Hello World' == 'Hello World'") # True
print_calc_result("not 'Chainer' != 'Tutorial'") # True
print_calc_result("all([True, True, False])") # False
print_calc_result("any([True, True, False])") # True
print_calc_result("abs(-3)") # 3
print_calc_result("2 // 0") # Error
