# API stuff

import collections
from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import Counter

data = data.split("\n")
string, rules = data[0], [d.split(" -> ") for d in data[2:]]
rules = {r[0] : r[1] for r in rules}

for _ in range(10):
    i = 0

    while i < len(string) - 1:
        pair = "".join(string[i : i + 2])

        if pair in rules:
            string = string[: i + 1] + rules[pair] + string[i + 1 :]#(i + 1, rules[pair])
            i += 1

        i += 1

counts = collections.Counter(string).most_common()
answer = counts[0][1] - counts[-1][1]

# submission

submit(answer, part=part, day=day, year=year)
