# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

x1, y1, x2, y2 = 0, 0, 0, 0
locations = {(x1, y1) : 2}

for i, d in enumerate(data):
    if i % 2 == 0:
        x1 += 1 if d == ">" else (-1 if d == "<" else 0)
        y1 += 1 if d == "^" else (-1 if d == "v" else 0)

        if (x1, y1) in locations.keys():
            locations[(x1, y1)] += 1
        else:
            locations[(x1, y1)] = 1

    else:
        x2 += 1 if d == ">" else (-1 if d == "<" else 0)
        y2 += 1 if d == "^" else (-1 if d == "v" else 0)

        if (x2, y2) in locations.keys():
            locations[(x2, y2)] += 1
        else:
            locations[(x2, y2)] = 1

answer = len(locations.values()) - list(locations.values()).count(0)

# submission

submit(answer, part=part, day=day, year=year)
