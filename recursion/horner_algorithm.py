def calculate(coefficients: list, x):
    res = x
    for i in range(len(coefficients) - 1):
        A, B = coefficients[i], coefficients[i + 1]
        res = A * res + B
    return res


def optimal_calculation_order(upper_limit: int):
    optimal = "x"
    ns = [i for i in reversed(range(upper_limit))]
    for i in range(upper_limit - 1):
        L, R = ns[i], ns[i + 1]
        optimal = f"(A{L}·x + A{R})"
    return optimal


def demo():
    pass


# demo()
