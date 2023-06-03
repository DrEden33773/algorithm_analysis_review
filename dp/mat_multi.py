from dataclasses import dataclass
from io import StringIO


@dataclass
class MatInfo:
    row: int = 1
    col: int = 1


def get_times_and_seps(mats: list[MatInfo]):
    nums = len(mats)
    if nums <= 1:
        raise Exception("At least two mats should be input!")
    for i in range(1, nums):
        assert mats[i].row == mats[i - 1].col
    dp = [[float(0)] * nums for _ in range(nums)]
    seps = [[-1] * nums for _ in range(nums)]
    for gap in range(1, nums):
        for end in range(gap, nums):
            beg = end - gap
            dp[beg][end] = float("inf")
            for sep in range(beg, end):
                cost = (
                    dp[beg][sep]
                    + dp[sep + 1][end]
                    + mats[beg].row * mats[sep].col * mats[end].col
                )
                if cost < dp[beg][end]:
                    dp[beg][end], seps[beg][end] = cost, sep
    return dp[0][nums - 1], seps


def gen_optimal_parens(seps: list[list[int]]):
    def helper(seps: list[list[int]], beg: int, end: int, out: StringIO):
        if beg == end:
            print(f"M{beg} ", file=out, end="")
        else:
            print(f"[", file=out, end="")
            helper(seps, beg, seps[beg][end], out)
            helper(seps, seps[beg][end] + 1, end, out)
            print(f"]", file=out, end="")

    optimal_parens_io = StringIO()
    helper(seps, 0, len(seps) - 1, optimal_parens_io)
    return optimal_parens_io.getvalue()


def solution(mats: list[MatInfo]):
    times, seps = get_times_and_seps(mats)
    parens = gen_optimal_parens(seps)
    print(f"Optimal Times: {times}")
    print(f"Optimal Parens: {parens}")


def demo():
    mats = [
        MatInfo(2, 3),
        MatInfo(3, 2),
        MatInfo(2, 9),
        MatInfo(9, 2),
    ]
    solution(mats)


demo()
