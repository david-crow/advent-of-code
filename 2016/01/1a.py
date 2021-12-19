# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [(list(d)[0], int("".join(list(d)[1:]))) for d in data.split(", ")]
facing, x, y = 0, 0, 0

for d in data:
    facing = (facing + 4 + (1 if d[0] == "R" else -1)) % 4

    if facing == 0:
        y += d[1]
    elif facing == 1:
        x += d[1]
    elif facing == 2:
        y -= d[1]
    elif facing == 3:
        x -= d[1]

answer = abs(x) + abs(y)

# submission

submit(answer, part=part, day=day, year=year)
