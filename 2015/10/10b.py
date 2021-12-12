# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from itertools import groupby

for _ in range(50):
    groups = ["".join(g) for _, g in groupby(data)]
    data = "".join([str(len(g)) + g[0] for g in groups])

answer = len(data)

# submission

submit(answer, part=part, day=day, year=year)
