# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

crabs = [int(d) for d in data.split(",")]
answer = int(1e10)

for x in crabs:
    fuel = 0

    for crab in crabs:
        triangle = lambda n : int(n * (n + 1) / 2)
        fuel += triangle(abs(crab - x))

    answer = min(answer, fuel)

# submission

submit(answer, part=part, day=day, year=year)
