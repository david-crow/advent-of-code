# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

def threeSum():
    for a in numbers:
        diffs = []

        for b in numbers:
            c = 2020 - a - b
            diffs.append(c)

            if b in diffs:
                return a * b * c

answer = threeSum()

# submission

submit(answer, part=part, day=day, year=year)
