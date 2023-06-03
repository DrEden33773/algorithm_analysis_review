"""
    - The MOST IMPORTANT Thing: Figure out the task itself!
"""


def discarded_minimum_num_of_boat(
    people: list[int],
    limit: int,
):
    if people == []:
        return 0
    people.sort()
    boat_num, last_boat_cap = 1, limit - people[0]
    for e in people[1:]:
        if e > last_boat_cap:
            boat_num += 1
            last_boat_cap = limit
        last_boat_cap -= e
    return boat_num


def minimum_num_of_boat(
    people: list[int],
    limit: int,
):
    if people == []:
        return 0
    ans = 0
    people.sort(reverse=True)
    info = [(id, weight) for id, weight in enumerate(people)]
    sent = set[int]()
    for curr_id, curr_weight in info:
        if curr_id in sent:
            continue
        ans += 1
        sent.add(curr_id)
        for candidate_id, candidate_weight in info[curr_id + 1 :]:
            if candidate_weight + curr_weight <= limit:
                sent.add(candidate_id)
                break
    return ans


def demo():
    people, limit = [3, 2, 2, 1], 3
    people, limit = [1, 2], 3
    people, limit = [3, 5, 3, 4], 5
    ans = minimum_num_of_boat(people, limit)
    print(ans)


demo()
