from random import random


def pi(ITER_TIME=int(1e6)):
    cnt = 0
    for _ in range(ITER_TIME):
        x, y = random(), random()
        cnt += 1 if x**2 + y**2 <= 1 else 0
    return 4 * cnt / ITER_TIME


def demo():
    print(f"pi = {pi()}")


demo()
