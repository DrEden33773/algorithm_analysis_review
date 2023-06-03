from random import randint


def quick_select(s: list, k: int):
    assert 0 <= k < len(s)
    if len(s) < 5:
        return sorted(s)[k]
    mids = []
    for i in range(0, len(s), 5):
        group = sorted(s[i : i + 5])
        mid = group[len(group) // 2]
        mids.append(mid)
    pivot = quick_select(mids, len(mids) // 2)
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
