# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

fish = [int(d) for d in data.split(",")]
fish = [fish.count(i) for i in range(9)]

for _ in range(80):
    num = fish.pop(0)
    fish[6] += num
    fish.append(num)

answer = sum(fish)

# submission

submit(answer, part=part, day=day, year=year)
