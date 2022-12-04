# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from string import ascii_letters

data = data.split("\n")
scores = {l: i + 1 for i, l in enumerate(ascii_letters)}

answer = 0

for i in range(0, len(data), 3):
    s = set(data[i]) & set(data[i + 1]) & set(data[i + 2])
    answer += scores[list(s)[0]]

# submission

submit(answer, part=part, day=day, year=year)
