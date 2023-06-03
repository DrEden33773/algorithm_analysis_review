"""

    Understand the process of `backtrack`

"""


def get_all_solution(
    score: int = 3,
    front: int = 6,
    back: int = 10,
):
    solutions = list[str]()

    def backtrack(
        score: int,
        front_times: int,
        back_times: int,
        solution: str = "",
        depth: int = 0,
    ):
        if score < 1:
            return
        if depth == front + back:
            if score == 1:
                solutions.append(solution + "B")
            return
        if front_times > 0:
            backtrack(
                score * 2,
                front_times - 1,
                back_times,
                solution + "A",
                depth + 1,
            )
        if back_times > 0:
            backtrack(
                score - 1,
                front_times,
                back_times - 1,
                solution + "B",
                depth + 1,
            )

    backtrack(score, front, back)
    return solutions


def demo():
    solutions = get_all_solution()
    num = len(solutions)
    print()
    print(f"{num} solutions have been found.")
    print()
    [print(solution) for solution in solutions]


demo()
