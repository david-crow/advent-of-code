# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

x, y = 0, 0
locations = {(x, y) : 1}

for d in data:
    x += 1 if d == ">" else (-1 if d == "<" else 0)
    y += 1 if d == "^" else (-1 if d == "v" else 0)

    if (x, y) in locations.keys():
        locations[(x, y)] += 1
    else:
        locations[(x, y)] = 1

answer = len(locations.values()) - list(locations.values()).count(0)

# submission

submit(answer, part=part, day=day, year=year)
