# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = data.split("\n")
answer = 0

while True:
    data = [max(0, int(d) // 3 - 2) for d in data]
    answer += (fuel_sum := sum(data))

    if fuel_sum == 0:
        break

# submission

submit(answer, part=part, day=day, year=year)
