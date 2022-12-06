# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from string import ascii_lowercase

answer = len(data)

def react(s):
    new_s = None

    while s != new_s:
        new_s = s

        for c in ascii_lowercase:
            s = s.replace(c + c.upper(), "").replace(c.upper() + c, "")

    return s

for c in ascii_lowercase:
    new_data = data.replace(c, "").replace(c.upper(), "")
    answer = min(answer, len(react(new_data)))

# submission

submit(answer, part=part, day=day, year=year)
