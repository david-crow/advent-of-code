# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = data
answer = -1

for i in range(len(data) - 14):
    if len(set(data[i : i + 14])) == 14:
        answer = i + 14
        break

# submission

submit(answer, part=part, day=day, year=year)
