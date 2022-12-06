# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

answer = -1

for i in range(len(data) - 4):
    if len(set(data[i : i + 4])) == 4:
        answer = i + 4
        break

# submission

submit(answer, part=part, day=day, year=year)
