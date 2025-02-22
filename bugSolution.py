def function_with_uncommon_error_solution(x, y):
    if x == 0:
        return 0 # Correctly handles division by zero
    else:
        return y / x