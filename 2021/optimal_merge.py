from io import StringIO
from sys import maxsize


def get_value_and_table(data: list[int]):
    assert len(data) > 0
    length = len(data)
    dp = [[float("inf")] * length for _ in range(length)]
    table = [[-1] * length for _ in range(length)]
    for i in range(length):
        dp[i][i] = data[i]
    for gap in range(1, length):
        for end in range(gap, length):
            beg = end - gap
            for sep in range(beg, end):
                cost = dp[beg][sep] + dp[sep + 1][end]
                if cost < dp[beg][end]:
                    dp[beg][end] = cost
                    table[beg][end] = sep
    return dp[0][length - 1], table


def get_optimal_operation(table: list[list[int]]):
    def optimal_op_gen(table: list[list[int]], beg: int, end: int, out: StringIO):
        if beg == end:
            print(f"S{beg} ", file=out, end="")
        else:
            print("[", file=out, end="")
            optimal_op_gen(table, beg, table[beg][end], out)
            optimal_op_gen(table, table[beg][end] + 1, end, out)
            print("]", file=out, end="")

    out = StringIO()
    optimal_op_gen(table, 0, len(table) - 1, out)
    return out.getvalue()


def solution(data: list[int]):
    minimum_value, table = get_value_and_table(data)
    optimal_operation = get_optimal_operation(table)
    return minimum_value, optimal_operation


def show_solution(data: list[int]):
    minimum_value, optimal_operation = solution(data)
    print(f"Minimum Value: {minimum_value}")
    print(f"Optimal Operation: {optimal_operation}")


def demo():
    data = [1, 3, 5, 6, 2]
    show_solution(data)


demo()
