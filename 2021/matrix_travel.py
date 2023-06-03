from enum import Enum


class Target(Enum):
    MinimumSum = min
    MaximumSum = max


def inplace_dp(mat: list[list[int]], target: Target = Target.MinimumSum):
    assert len(mat) > 0 and len(mat[0]) > 0, "Empty matrix"
    row, col, cmp = len(mat), len(mat[0]), target.value
    for i in range(row):
        for j in range(col):
            match (i, j):
                case (0, 0):
                    pass
                case (0, _):
                    mat[i][j] += mat[i][j - 1]
                case (_, 0):
                    mat[i][j] += mat[i - 1][j]
                case (_, _):
                    mat[i][j] += cmp(mat[i - 1][j], mat[i][j - 1])
    return mat[row - 1][col - 1]


def basic_dp(mat: list[list[int]], target: Target = Target.MinimumSum):
    assert len(mat) > 0 and len(mat[0]) > 0, "Empty matrix"
    row, col, cmp = len(mat), len(mat[0]), target.value
    dp = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            match (i, j):
                case (0, 0):
                    dp[i][j] = mat[i][j]
                case (0, _):
                    dp[i][j] = dp[i][j - 1] + mat[i][j]
                case (_, 0):
                    dp[i][j] = dp[i - 1][j] + mat[i][j]
                case (_, _):
                    dp[i][j] = cmp(dp[i - 1][j], dp[i][j - 1]) + mat[i][j]
    return dp[row - 1][col - 1]


def one_dimension_dp(mat: list[list[int]], target: Target = Target.MinimumSum):
    assert len(mat) > 0 and len(mat[0]) > 0, "Empty matrix"
    row, col, cmp = len(mat), len(mat[0]), target.value
    dp = [0 for _ in range(col)]
    for i in range(row):
        for j in range(col):
            match (i, j):
                case (0, 0):
                    dp[j] = mat[i][j]
                case (0, _):
                    dp[j] = dp[j - 1] + mat[i][j]
                case (_, 0):
                    dp[j] = dp[j] + mat[i][j]
                case (_, _):
                    dp[j] = cmp(dp[j], dp[j - 1]) + mat[i][j]
    return dp[col - 1]
