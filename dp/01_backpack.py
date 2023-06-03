"""

01_backpack

input => costs, values, capacity
output => maximum_sum_value

"""


def basic_dp(costs: list[int], values: list[int], capacity: int):
    assert len(costs) == len(values) and len(costs) != 0 and capacity >= 0
    category = len(costs)
    dp = [[0] * (capacity + 1) for _ in range(category + 1)]
    for i in range(1, category + 1):
        for j in range(1, capacity + 1):
            dp[i][j] = dp[i - 1][j]
            cost, value = costs[i - 1], values[i - 1]
            if j >= cost:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + value)
    return dp[category][capacity]


def one_dimension_dp(costs: list[int], values: list[int], capacity: int):
    assert len(costs) == len(values) and len(costs) != 0 and capacity >= 0
    category = len(costs)
    dp = [0] * (capacity + 1)
    for i in range(1, category + 1):
        for j in reversed(range(1, capacity + 1)):
            cost, value = costs[i - 1], values[i - 1]
            if j >= cost:
                dp[j] = max(dp[j], dp[j - cost] + value)
    return dp[capacity]


def demo():
    costs, values, capacity = [3, 5, 7, 8, 9], [4, 6, 7, 9, 10], 22
    basic = basic_dp(costs, values, capacity)
    one_dimension = one_dimension_dp(costs, values, capacity)
    print(f"basic => {basic}")
    print(f"one_dimension => {one_dimension}")


demo()
