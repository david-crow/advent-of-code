# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from itertools import permutations

data = [d.split() for d in data.split("\n")]
routes = {(line[0], line[2]) : int(line[4]) for line in data}

for k, v in list(routes.items()):
    routes[(k[1], k[0])] = v

cities = list(set([route[0] for route in routes.keys()]))
answer = int(1e10)

for route in permutations(cities):
    distance = 0

    for i in range(len(route) - 1):
        distance += routes[(route[i], route[i + 1])]

    answer = min(answer, distance)

# submission

submit(answer, part=part, day=day, year=year)
