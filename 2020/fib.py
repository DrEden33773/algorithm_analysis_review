"""
    Fast `Fibonacci` Algorithm
        => Matrix Multiplication
        => Fast Power
"""


class FibMatrix:
    def __init__(self, e: int = 1) -> None:
        self.data = [[1, 0], [0, 1]]
        self **= e

    def __mul__(self, other):
        ret = FibMatrix()
        ret.data = [[0, 0], [0, 0]]
        for row in range(2):
            for col in range(2):
                for i in range(2):
                    ret.data[row][col] += self.data[row][i] * other.data[i][col]
        return ret

    def __pow__(self, e: int):
        if e <= 0:
            return FibMatrix()
        if e == 1:
            return self
        square = self ** (e // 2)
        return square * square if e % 2 == 0 else square * square * self

    def __getitem__(self, m: int):
        return self.data[m]


def fast_fib(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    the_mat = FibMatrix()
    the_mat.data = [[1, 1], [1, 0]]
    the_mat = the_mat ** (n - 1)
    return the_mat[0][0] * 1 + the_mat[0][1] * 0


def demo():
    a = fast_fib(10)
    print(a)


demo()
