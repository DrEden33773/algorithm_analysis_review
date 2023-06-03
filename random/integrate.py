from random import random
from math import sin


def sinX_div_x_integrate_from_1_to_2(ITER_TIME=int(1e6)):
    cnt = 0
    for _ in range(ITER_TIME):
        x, y = random() + 1, random()
        cnt += 1 if y <= sin(x) / x else 0
    return cnt / ITER_TIME


def demo():
    print(f"sinX_div_x_integrate_from_1_to_2 = {sinX_div_x_integrate_from_1_to_2()}")


demo()
