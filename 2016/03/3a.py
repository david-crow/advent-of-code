# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [list(map(int, d.split())) for d in data.split("\n")]
answer = sum(1 if (d[0] + d[1] > d[2] and d[0] + d[2] > d[1] and d[1] + d[2] > d[0]) else 0 for d in data)

# submission

submit(answer, part=part, day=day, year=year)
