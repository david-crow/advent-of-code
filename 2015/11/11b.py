# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from itertools import groupby


def next_c(c):
    return chr(ord(c) + 1)

def increment(pw):
    if pw[-1] == "z":
        return increment(pw[:-1]) + "a"

    return pw[:-1] + next_c(pw[-1])

def invalid(pw):
    if any(c in pw for c in ["i", "o", "l"]):
        return True

    groups = ["".join(g) for _, g in groupby(pw)]
    groups = [len(g) > 1 for g in groups]

    if groups.count(True) < 2:
        return True

    for i in range(len(pw) - 2):
        if next_c(pw[i]) == pw[i + 1] and next_c(pw[i + 1]) == pw[i + 2]:
            return False

    return True

answer = increment("cqjxxyzz")

while invalid(answer):
    answer = increment(answer)

# submission

submit(answer, part=part, day=day, year=year)
