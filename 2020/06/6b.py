# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import Counter

def get_yes_count(d, group_size):
    return len([c for c in set(d) if Counter(d)[c] == group_size])

data = [d.split("\n") for d in data.split("\n\n")]
answer = sum([get_yes_count("".join(d), len(d)) for d in data])

# submission

submit(answer, part=part, day=day, year=year)
