from random import randint


def quick_select(s: list, k: int):
    assert 0 <= k < len(s)
    pivot = s[randint(0, len(s) - 1)]
    lt = [e for e in s if e < pivot]
    eq = [e for e in s if e == pivot]
    gt = [e for e in s if e > pivot]
    if k < len(lt):
        return quick_select(lt, k)
    elif k < len(lt) + len(eq):
        return pivot
    else:
        return quick_select(gt, k - len(lt) - len(eq))


def demo():
    s = [1, 7, 3, 8, 2, 5, 9, 0, -1]
    k = randint(0, len(s) - 1)
    ans = quick_select(s, k)
    expected = sorted(s)[k]
    assert expected == ans


demo()
