# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = data.splitlines()
x, y = 0, 0
answer = 0

while y < len(data) - 1:
    x = (x + 3) % len(data[0])
    y += 1
    answer += 1 if data[y][x] == "#" else 0

# submission

submit(answer, part=part, day=day, year=year)
