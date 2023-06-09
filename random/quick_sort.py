from random import randint


def partition(s: list, beg: int, end: int):
    last, sep = end - 1, beg - 1
    temp_rand = randint(beg, last)
    s[temp_rand], s[last] = s[last], s[temp_rand]
    for i in range(beg, end):
        if s[i] <= s[last]:
            sep += 1
            s[i], s[sep] = s[sep], s[i]
    return sep


def qs(s: list, beg: int, end: int):
    if end - beg < 2:
        return
    sep = partition(s, beg, end)
    qs(s, beg, sep)
    qs(s, sep + 1, end)


def quick_sort(s: list):
    return qs(s, 0, len(s)) if len(s) > 1 else None


def demo():
    s = [1, 7, 3, 8, 2, 5, 9, 0, -1]
    quick_sort(s)
    print(s)


demo()
