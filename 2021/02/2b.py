# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [d.split() for d in data.split("\n")]
x, y, aim = 0, 0, 0

for d in data:
    direction, distance = d[0], int(d[1])

    if direction == "forward":
        x += distance
        y += distance * aim
    else:
        aim += distance if direction == "down" else -distance

answer = x * y

# submission

submit(answer, part=part, day=day, year=year)
