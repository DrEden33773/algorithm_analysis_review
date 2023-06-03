def dijkstra(
    src: int,
    mat: list[list[float]],
):
    assert (
        len(mat) > 0
        and len(mat[0]) > 0
        and len(mat) == len(mat[0])
        and 0 <= src < len(mat)
    )
    v_num = len(mat)
    v_set = set(range(v_num))
    joined = {src}
    unjoined = v_set - {src}
    dist = [mat[src][i] for i in range(v_num)]
    adj = [(i if mat[src][i] < float("inf") else -1) for i in range(v_num)]
    while joined != v_set:
        closest, _ = min([(v, d) for v, d in enumerate(dist)], key=lambda pair: pair[1])
        joined.add(closest)
        unjoined.remove(closest)
        for v in unjoined:
            new_dist = dist[closest] + mat[closest][v]
            if new_dist < dist[v]:
                dist[v] = new_dist
                adj[v] = closest
    return dist, adj
