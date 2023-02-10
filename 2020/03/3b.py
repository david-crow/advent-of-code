# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from math import prod

data = data.splitlines()
x_lim, y_lim = len(data[0]), len(data)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def count_trees(slope):
    x, y, trees_hit = 0, 0, 0

    while y < y_lim - 1:
        x = (x + slope[0]) % x_lim
        y += slope[1]
        trees_hit += 1 if data[y][x] == "#" else 0

    return trees_hit

# submission

answer = prod([count_trees(slope) for slope in slopes])
submit(answer, part=part, day=day, year=year)
