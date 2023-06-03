from typing import Sequence


def fast_min_max(seq: Sequence):
    if len(seq) == 1:
        return seq[0], seq[0]
    if len(seq) == 2:
        return min(seq), max(seq)
    mid = len(seq) // 2
    l_min, l_max = fast_min_max(seq[:mid])
    r_min, r_max = fast_min_max(seq[mid:])
    return min(l_min, r_min), max(l_max, r_max)


def min_max(seq: Sequence, could_optimize: bool = True):
    l = len(seq)
    return (
        fast_min_max(seq) if l & l - 1 == 0 and could_optimize else (min(seq), max(seq))
    )


def demo():
    seq = [1, 3, 5, 7, 8, 9, 0, 3]
    assert min_max(seq) == min_max(seq, could_optimize=False)
    the_min, the_max = min_max(seq)
    print(f"min = {the_min}, max = {the_max}")


demo()
