# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from math import prod

data = [list(map(int, list(d))) for d in lines]
size = len(data)

def calcScore(y, x):
    return (prod([max([x - i for i in range(x + 1) if all(d < data[y][x] for d in data[y][i + 1 : x])]),
                  max([i - x for i in range(x, size) if all(d < data[y][x] for d in data[y][x + 1 : i])]),
                  max([y - i for i in range(y + 1) if all(d[x] < data[y][x] for d in data[i + 1 : y])]),
                  max([i - y for i in range(y, size) if all(d[x] < data[y][x] for d in data[y + 1 : i])])]))

answer = max([calcScore(y, x) for y in range(size) for x in range(size)])

# submission

submit(answer, part=part, day=day, year=year)
