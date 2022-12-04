# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import Counter

data = [d.split(": ") for d in data.split("\n")]
data = [[a.split(" @ "), list(map(int, b.split("x")))] for a, b in data]
data = [[int(a[0][1:]), list(map(int, a[1].split(","))), b] for a, b in data]

grid = [[0] * 1000 for _ in range(1000)]

for d in data:
    for col in range(d[1][0], d[1][0] + d[2][0]):
        for row in range(d[1][1], d[1][1] + d[2][1]):
            grid[row][col] += 1

grid = "".join(["".join(list(map(str, row))) for row in grid])
answer = sum([v for k, v in Counter(grid).items() if int(k) > 1])

# submission

submit(answer, part=part, day=day, year=year)
