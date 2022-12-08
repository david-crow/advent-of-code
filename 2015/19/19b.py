# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import re

data = sorted([d.split(" => ") for d in lines[:-2]], key=lambda d: len(d[1]), reverse=True)
m = lines[-1]
answer = 0

while m != "e":
    for d in data:
        if d[1] in m:
            idx = m.index(d[1])
            m = m[:idx] + d[0] + m[idx + len(d[1]):]
            answer += 1

# submission

submit(answer, part=part, day=day, year=year)
