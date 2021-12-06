# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

floor = 0

for i, c in enumerate(data):
    floor += 1 if c == "(" else -1

    if floor < 0:
        answer = i + 1
        break

# submission

submit(answer, part=part, day=day, year=year)
