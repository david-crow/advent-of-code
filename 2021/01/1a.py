# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [int(d) for d in data.split()]
count = 0

for i, d in enumerate(data[:-1]):
    if data[i + 1] > d:
        count += 1

answer = count

# submission

submit(answer, part=part, day=day, year=year)
