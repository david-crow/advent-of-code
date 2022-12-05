# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import defaultdict
import re

data = [d.split("\n") for d in data.split("\n\n")]
data[1] = [list(map(int, re.findall("[0-9]+", d))) for d in data[1]]
stacks = defaultdict(list)

# generalizable to any set of stacks
# rows must use four chars between stacks, e.g., [A]  [B]  [ ]  [C]
for d in data[0][:-1]:
    for i, letter in enumerate(d[1::4]):
        if letter != " ":
            stacks[i + 1].append(letter)

# make the moves
for move in data[1]:
    stacks[move[2]] = stacks[move[1]][:move[0]] + stacks[move[2]]
    stacks[move[1]] = stacks[move[1]][move[0]:]

answer = "".join([v[0] for _, v in sorted(stacks.items())])

# submission

submit(answer, part=part, day=day, year=year)
