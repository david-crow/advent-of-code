# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import defaultdict

data = [d.split() for d in data.splitlines()]
reg = defaultdict(int)
answer = 0

for i, d in enumerate(data):
    if eval(f"reg['{d[4]}'] {d[5]} {int(d[6])}"):
        reg[d[0]] += int(d[2]) * (1 if d[1] == "inc" else -1)
        answer = max(answer, reg[d[0]])

# submission

submit(answer, part=part, day=day, year=year)
