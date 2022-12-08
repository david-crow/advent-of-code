# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

diffs = []

for n in numbers:
    diff = 2020 - n
    diffs.append(diff)

    if n in diffs:
        answer = n * diff
        break

# submission

submit(answer, part=part, day=day, year=year)
