# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from itertools import groupby

data = [int(n) for n in data.split("-")]

def valid(s):
    return list(s) == sorted(s) and any(len(list(v)) >= 2 for k, v in groupby(s))

answer = len([n for n in range(data[0], data[1] + 1) if valid(str(n))])

# submission

submit(answer, part=part, day=day, year=year)
