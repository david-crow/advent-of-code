# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [d.split() for d in data.split("\n")]
grid = [[False] * 1000 for _ in range(1000)]

for d in data:
    if d[0] == "toggle":
        x1, y1 = [int(n) for n in d[1].split(",")]
        x2, y2 = [int(n) for n in d[3].split(",")]

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] = not grid[x][y]
    else:
        x1, y1 = [int(n) for n in d[2].split(",")]
        x2, y2 = [int(n) for n in d[4].split(",")]

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] = d[1] == "on"

answer = sum(sum(row) for row in grid)

# submission

submit(answer, part=part, day=day, year=year)
