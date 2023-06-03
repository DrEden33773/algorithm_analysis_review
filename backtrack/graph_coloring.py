def get_solutions(graph: list[list[int]], N: int = 3):
    assert len(graph) > 0 and N > 0
    solution, solutions = [-1] * len(graph), []

    def dfs(v: int = 0):
        if v == len(graph):
            solutions.append(solution[:])
            return
        for color in range(N):
            solution[v] = color
            unique = True
            for adj in graph[v]:
                unique &= False if solution[v] == solution[adj] else True
            if unique:
                dfs(v + 1)
        solution[v] = -1

    dfs()
    return solutions


def demo():
    graph = [[1, 2], [0, 2], [0, 1]]
    solutions = get_solutions(graph)
    print(f"{solutions}")


demo()
