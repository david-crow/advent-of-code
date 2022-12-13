# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import numpy as np
from textwrap import wrap

data = data.replace("addx", "noop\naddx").split("\n")
data = [0 if d == "noop" else int(d.split()[-1]) for d in data]
data = list(np.cumsum([1] + data))
crt = ["#" if abs(cycle % 40 - x) <= 1 else " " for cycle, x in enumerate(data[:-1])]

picture = "\n".join(wrap("".join(crt), 40))
answer = "EFUGLPAP"
print(f"\n{picture}\n")

# submission

submit(answer, part=part, day=day, year=year)
