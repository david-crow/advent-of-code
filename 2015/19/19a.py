# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import re

data = [d.split(" => ") for d in lines]
m = data[-1][0]
molecules = set([m[:match.start()] + d[1] + m[match.end():] for d in data[:-2] for match in re.finditer(d[0], m)])
answer = len(molecules)

# submission

submit(answer, part=part, day=day, year=year)
