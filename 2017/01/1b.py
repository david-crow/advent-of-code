# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [int(d) for d in data]
dist, half = len(data), len(data) // 2
answer = 0

for i, n in enumerate(data):
    loc = i + half
    loc = loc if loc < dist else loc - dist
    answer += n * (n == data[loc])

# submission

submit(answer, part=part, day=day, year=year)
