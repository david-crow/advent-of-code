# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import defaultdict

path = []
sizes = defaultdict(int)

for line in lines:
    if line.startswith("$ cd"):
        target = line.split()[2]

        if target == "/":
            path.append("/")
        elif target == "..":
            path.pop()
        else:
            path.append(f"{path[-1]}{'' if path[-1] == '/' else '/'}{target}")

    if line[0].isnumeric():
        for p in path:
            sizes[p] += int(line.split()[0])

space_needed = 30_000_000 - (70_000_000 - sizes["/"])
answer = min(s for s in sizes.values() if s >= space_needed)

# submission

submit(answer, part=part, day=day, year=year)
