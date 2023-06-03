"""
    Fast `Fibonacci` Algorithm, using `numpy`
"""


from numpy import matrix, identity


fib_mtx = matrix(
    [
        [1, 1],
        [1, 0],
    ]
)


@staticmethod
def mtx_pow(mtx: matrix, exp: int) -> matrix:
    if exp <= 0:
        return matrix(identity(len(mtx)))
    if exp == 1:
        return mtx
    half = mtx_pow(mtx, exp // 2)
    return half * half * (1 if exp % 2 == 0 else mtx)


@staticmethod
def fast_fib(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    mtx = mtx_pow(fib_mtx, n - 1)
    return mtx[0, 0] * fast_fib(1) + mtx[0, 1] * fast_fib(0)


def demo():
    for i in range(10):
        print(f"fib({i}) = {fast_fib(i)}")


demo()
