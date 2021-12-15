# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import defaultdict

data = [list(map(int, list(d))) for d in data.split("\n")]
xmax, ymax = len(data[0]), len(data)

def neighbors(v):
    x, y = v[0], v[1]
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def valid(v):
    x, y = v[0], v[1]
    return 0 <= x and x < xmax and 0 <= y and y < ymax

def search():
    q = set()
    distance = defaultdict()
    previous = defaultdict()

    for x in range(xmax):
        for y in range(ymax):
            distance[(x, y)] = int(1e10)
            previous[(x, y)] = None
            q |= {(x, y)}

    distance[(0, 0)] = 0

    while q:
        u = min(q, key = lambda x : distance[x])
        q.remove(u)

        for v in neighbors(u):
            if valid(v):
                alternate = distance[u] + data[v[1]][v[0]]

                if alternate < distance[v]:
                    distance[v] = alternate
                    previous[v] = u

    return distance

answer = search()[(xmax - 1, ymax - 1)]

# submission

submit(answer, part=part, day=day, year=year)
