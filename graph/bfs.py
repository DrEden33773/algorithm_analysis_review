def bfs(graph: list[list[int]], start: int = 0):
    """
    graph: `adjacency list` := [current_vertex: [adjacent_vertex, ...], ...]

    start: `vertex`
    """
    queue = [start]  # queue
    visited = {start}  # visited vertices
    while not len(queue) == 0:
        layer_scale = len(queue)
        for _ in range(layer_scale):  # iterate all nods in the layer
            curr = queue.pop(0)
            print(curr, end=" ")
            for adj in filter(lambda x: x not in visited, graph[curr]):
                queue.append(adj)
                visited.add(adj)
        print()


def demo():
    graph = [[1, 2, 3], [0, 4], [0, 3], [0, 2, 4], [1, 3]]
    for i in range(len(graph)):
        print(f"starting vertex: {i}")
        bfs(graph, i)
        print()


demo()
