"""
    Partition sequence with positive and negative number
"""


def s_n_algo(s: list[int]):
    negatives = [e for e in s if e < 0]
    non_negatives = [e for e in s if e >= 0]
    return [e for e in (negatives + non_negatives)]


def s_1_algo(s: list[int]):
    seq = s
    par = -1
    for i in range(len(seq)):
        if seq[i] < 0:
            par += 1
            seq[i], seq[par] = seq[par], seq[i]
    return seq


def demo():
    s = [-1, 0, 4, -2, 0, 5, -7]
    s1 = s_1_algo(s)
    sn = s_n_algo(s)
    print(f"s1 => {s1}")
    print(f"sn => {sn}")


demo()
