# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [d.split()[-4:] for d in data.split("\n")]
answer = 0

for d in data:
    for i in d:
        answer += 1 if len(i) in [2, 4, 3, 7] else 0

# submission

submit(answer, part=part, day=day, year=year)
