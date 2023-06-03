from typing import Sequence


def get_sorted(s: Sequence):
    return sorted(s)


def get_zipped(a: Sequence, b: Sequence):
    return [e for e in zip(a, b)]


def original_issue(a: Sequence, b: Sequence):
    A, B = get_sorted(a), get_sorted(b)
    return get_zipped(A, B)
