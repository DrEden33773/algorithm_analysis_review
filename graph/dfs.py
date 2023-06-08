def dfs(graph: list[list[int]], start: int = 0):
    visited = {start}

    def dfs_helper(curr: int):
        print(curr, end=" ")
        for adj in graph[curr]:
            if adj not in visited:
                visited.add(adj)
                dfs_helper(adj)

    dfs_helper(start)
    print()


def demo():
    graph = [[1, 2, 3], [0, 4], [0, 3], [0, 2, 4], [1, 3]]
    for i in range(len(graph)):
        print(f"starting vertex: {i}")
        dfs(graph, i)
        print()


demo()
