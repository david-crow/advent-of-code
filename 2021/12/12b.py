# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import defaultdict

routes = defaultdict(list)

for line in data.split("\n"):
    a, b = line.split("-")
    routes[a].append(b)
    routes[b].append(a)

def route(cave, visited, repeated):
    if cave == "end":
        return 1

    if cave == "start" and visited:
        return 0

    if cave.islower() and cave in visited:
        if repeated is None:
            repeated = cave
        else:
            return 0

    visited = visited.union({cave})
    paths = 0

    for neighbor in routes[cave]:
        paths += route(neighbor, visited, repeated)

    return paths

answer = route("start", set(), None)

# submission

submit(answer, part=part, day=day, year=year)
