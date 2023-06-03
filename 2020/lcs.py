from dataclasses import dataclass


@dataclass
class LCS_MAT:
    data: list[list]

    def __repr__(self) -> str:
        res = "\n"
        for row in self.data:
            res += f"{row}\n"
        return res


def GET_LCS_TABLE(a: str, b: str):
    m, n = len(a), len(b)
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = (
                dp[i - 1][j - 1] + a[i - 1]
                if a[i - 1] == b[j - 1]
                else max(dp[i - 1][j], dp[i][j - 1])
            )
    return LCS_MAT(dp)


def demo():
    a, b = "abcde", "bcde"
    mat = GET_LCS_TABLE(a, b)
    print(mat)


demo()
