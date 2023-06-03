def recursive_solution(N: int) -> list[list[int]]:
    assert N > 0
    if N == 1:
        return [[1]]
    last = recursive_solution(N - 1)
    ans = []
    for one in last:
        for i in range(len(one) + 1):
            ans.append(one[:i] + [N] + one[i:])
    return ans


def swap_solution(N: int) -> list[list[int]]:
    def backtrack(ans: list[list[int]], nums: list[int], beg: int, end: int):
        if beg == end:
            ans.append(nums[:])
            return
        for i in range(beg, end):
            nums[i], nums[beg] = nums[beg], nums[i]
            backtrack(ans, nums, beg + 1, end)
            nums[i], nums[beg] = nums[beg], nums[i]

    ans, nums = [], [i + 1 for i in range(N)]
    backtrack(ans, nums, 0, N)
    return ans


def demo():
    N = 3
    full_permutation = swap_solution(N)
    print(full_permutation)


demo()
