def get_all_sub_arrays(sum: int, origin: list[int]):
    vector, vectors = [False] * len(origin), []

    def helper(
        decide_on: int = 0,
        target: int = sum,
    ):
        # record
        if decide_on == len(origin):
            if target == 0:
                vectors.append(vector[:])
            return
        # pick => decide_on
        vector[decide_on] = True
        helper(decide_on + 1, target - origin[decide_on])
        # ignore => decide_on
        vector[decide_on] = False
        helper(decide_on + 1, target)

    def predicate(vec: list[bool]):
        return [origin[i] for i in filter(lambda i: vec[i], range(len(vec)))]

    helper()
    return [sub_array for sub_array in map(predicate, vectors)]


def demo():
    sum, origin = 60, [i for i in range(10, 70, 10)]
    all_sub_arrays = get_all_sub_arrays(sum, origin)
    print(all_sub_arrays)


demo()
