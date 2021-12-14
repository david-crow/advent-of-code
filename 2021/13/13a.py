# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import numpy as np

points, folds = [], []

for line in data.split("\n"):
    if "fold" in line:
        line = line.split("=")
        folds.append([line[0][-1], int(line[1])])
    elif "," in line:
        line = line.split(",")
        points.append([int(line[0]), int(line[1])])

points = np.array(points)
xmax, ymax = points.max(axis=0) + 1
grid = np.zeros((ymax, xmax), dtype=int)

for p in points:
    grid[p[1]][p[0]] += 1

for f in folds[:1]:
    p = f[1]

    if f[0] == "y":
        for y in range(1, p + 1):
            grid[p - y, :] = grid[p - y, :] | grid[p + y, :]

        grid = grid[:y]

    else:
        for x in range(1, p + 1):
            grid[:, p - x] = grid[:, p - x] | grid[:, p + x]

        grid = grid[:, :x]

answer = np.sum(grid)

# submission

submit(answer, part=part, day=day, year=year)
