# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import numpy as np

data = data.replace("addx", "noop\naddx").split("\n")
data = [0 if d == "noop" else int(d.split()[-1]) for d in data]
data.insert(0, 1)
data = list(np.cumsum(data))
answer = sum([n * data[n - 1] for n in [20, 60, 100, 140, 180, 220]])

# submission

submit(answer, part=part, day=day, year=year)
