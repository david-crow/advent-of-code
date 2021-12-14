# API stuff

import collections
from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import Counter

data = data.split("\n")
rules = {d.split(" -> ")[0] : d.split(" -> ")[1] for d in data[2:]}
pairs = Counter(data[0][i] + data[0][i + 1] for i in range(len(data[0]) - 1))

for _ in range(40):
    new_pairs = Counter()

    for p in list(pairs):
        new_pairs[p[0] + rules[p]] += pairs[p]
        new_pairs[rules[p] + p[1]] += pairs[p]

    pairs = new_pairs

counts = Counter()

for p in pairs:
    counts[p[0]] += pairs[p]
    counts[p[1]] += pairs[p]

# all but the first and last characters are double-counted
# so double-count these two
counts[data[0][0]] += 1
counts[data[0][-1]] += 1

answer = (max(counts.values()) - min(counts.values())) // 2

# submission

submit(answer, part=part, day=day, year=year)