# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import Counter

data = data.split("\n")

two_counts = 0
three_counts = 0

for d in data:
    counts = Counter(d).values()
    two_counts += 2 in counts
    three_counts += 3 in counts

# submission

answer = two_counts * three_counts
submit(answer, part=part, day=day, year=year)
