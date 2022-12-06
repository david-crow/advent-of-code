# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from itertools import combinations

combs = [c for i in range(150 // min(numbers)) for c in combinations(numbers, i) if sum(c) == 150]
answer = len([d for d in combs if len(d) == len(min(combs, key = lambda x : len(x)))])

# submission

submit(answer, part=part, day=day, year=year)
