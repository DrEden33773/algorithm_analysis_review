from random import random


def sqrt_any(n: float, ITER_TIME=int(1e6)):
    assert n >= 0
    if n == 0:
        return 0
    cnt = 0
    for i in range(ITER_TIME):
        x = random() * n
        cnt += 1 if x**2 <= n else 0
    return n * (cnt / ITER_TIME)


def demo():
    for i in range(6):
        print({f"sqrt_any({i}) = {sqrt_any(i)}"})


demo()
