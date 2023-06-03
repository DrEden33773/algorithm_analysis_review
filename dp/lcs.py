def LCS(a: str, b: str) -> str:
    if len(b) > len(a):
        a, b = b, a
    dp = [["" for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + a[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(a)][len(b)]


def Optimized_LCS(a: str, b: str) -> str:
    if len(b) > len(a):
        a, b = b, a
    prev = ["" for _ in range(len(b) + 1)]
    curr = ["" for _ in range(len(b) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                curr[j] = prev[j - 1] + a[i - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev
    return prev[len(b)]


def demo():
    a = "abcde"
    b = "bcde"
    ans = Optimized_LCS(a, b)
    print(ans)


demo()
