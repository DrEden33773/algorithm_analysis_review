class StaticDSU:
    def __init__(self, N: int) -> None:
        self.pa = [i for i in range(N)]

    def get_root(self, i: int):
        return self.pa[i] if self.pa[i] == i else self.get_root(self.pa[i])

    def find(self, l: int, r: int):
        return self.get_root(l) == self.get_root(r)

    def union(self, l: int, r: int):
        self.pa[self.get_root(l)] = self.get_root(r)


def solution(edges: list[tuple[int, int, int]], v_num: int):
    assert len(edges) > 0 and v_num > 0
    edges = sorted(edges, key=lambda info: info[2])
    ans = type(edges)()
    dsu = StaticDSU(v_num)
    for beg, end, cost in edges:
        if len(ans) == v_num - 1:
            break
        if not dsu.find(beg, end):
            ans.append((beg, end, cost))
            dsu.union(beg, end)
    return sorted(ans, key=lambda info: info[2])
