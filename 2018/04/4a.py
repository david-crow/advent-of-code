# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import re
from collections import defaultdict

data = [d.split("] ") for d in sorted(data.split("\n"))]
data = [(list(map(int, re.findall("[0-9]+", d[0]))), d[1].split(" ")) for d in data]
times = defaultdict(lambda: [0] * 60)

for d in data:
    match event := d[1][0]:
        case "Guard":
            guard = d[1][1][1:]
        case "falls":
            sleep_time = d[0][4]
        case "wakes":
            for t in range(sleep_time, d[0][4]):
                times[guard][t] += 1

guard = max(times, key=lambda k: sum(times[k]))
answer = int(guard) * times[guard].index(max(times[guard]))

# submission

submit(answer, part=part, day=day, year=year)
