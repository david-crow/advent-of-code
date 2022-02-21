# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [[int(n) for n in d.split()] for d in data.split("\n")]
answer = sum([max(row) - min(row) for row in data])

# submission

submit(answer, part=part, day=day, year=year)
