import random


def std_power(base, exponent: int) -> float:
    return base**exponent


def power(base, exponent: int) -> float:
    if exponent < 0:
        return 1 / power(base, -exponent)
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base
    return (
        power(base, exponent // 2)
        * power(base, exponent // 2)
        * (base if exponent % 2 != 0 else 1)
    )


def demo():
    B, E = random.randint(1, 20), random.randint(2, 4)
    print(f"B = {B}, E = {E}, B ** E = {power(B, E)}")


# demo()
