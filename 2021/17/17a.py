# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [d.strip(",").split("=") for d in data.split()]
ylim = [int(d) for d in data[3][1].split("..")]

y = 0

for i in range(abs(min(ylim) - y)):
    y += i

answer = y

# submission

submit(answer, part=part, day=day, year=year)
