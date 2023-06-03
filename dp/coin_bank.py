"""

coin_bank

input => coins(must contain `1`), target
output => minimum_num_of_coin

"""


def basic_dp(coins: list[int], target: int):
    if len(coins) == 0:
        return None
    coins = sorted(coins)
    assert coins[0] == 1 and target >= 0
    category = len(coins)
    dp = [[0] * (target + 1) for _ in range(category + 1)]
    # i, j := sub_category, sub_target
    for i in range(1, category + 1):
        for j in range(1, target + 1):
            coin = coins[i - 1]
            if i == 1:
                dp[i][j] = j
            else:
                dp[i][j] = dp[i - 1][j]
                if j - coin >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coin] + 1)
    return dp[category][target]


def one_dimension_dp(coins: list[int], target: int):
    if len(coins) == 0:
        return None
    coins = sorted(coins)
    assert coins[0] == 1 and target >= 0
    category = len(coins)
    dp = [0] * (target + 1)
    for i in range(1, category + 1):
        for j in range(1, target + 1):
            coin = coins[i - 1]
            if i == 1:
                dp[j] = j
            elif j - coin >= 0:
                dp[j] = min(dp[j], dp[j - coin] + 1)
    return dp[target]


def try_exact_exchange(coins: list[int], target: int):
    if len(coins) == 0:
        return None
    coins = sorted(coins)
    category = len(coins)
    dp = [0] + [target + 1] * target
    for i in range(1, category + 1):
        for j in range(1, target + 1):
            coin = coins[i - 1]
            if j - coin >= 0:
                dp[j] = min(dp[j], dp[j - coin] + 1)
            else:
                # dp[j] = dp[j]
                pass
    return dp[target] if dp[target] < target + 1 else None


def adjustable_exchange(coins: list[int], target: int):
    if len(coins) == 0:
        return None
    coins = sorted(coins)
    category = len(coins)
    dp = [0] + [target + 1] * target
    for i in range(1, category + 1):
        for j in range(1, target + 1):
            coin = coins[i - 1]
            dp[j] = min(dp[j], (dp[j - coin] + 1) if j - coin >= 0 else (1))
    return dp[target]


def demo():
    print()
    coins, target = [1, 2, 5, 7, 8, 10], 53
    print(f"coins = {coins}, target = {target}:")
    print("=" * 10)
    print(f"basic => {basic_dp(coins, target)}")
    print(f"one_dimension => {one_dimension_dp(coins, target)}")
    print(f"try_exact => {try_exact_exchange(coins, target)}")
    print(f"adjustable => {adjustable_exchange(coins, target)}")

    print()
    coins, target = [3], 53
    print(f"coins = {coins}, target = {target}:")
    print("=" * 10)
    print(f"try_exact => {try_exact_exchange(coins, target)}")
    print(f"adjustable => {adjustable_exchange(coins, target)}")


demo()
