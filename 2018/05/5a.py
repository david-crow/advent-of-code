# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from string import ascii_lowercase

new_data = None

while data != new_data:
    new_data = data

    for c in ascii_lowercase:
        data = data.replace(c + c.upper(), "").replace(c.upper() + c, "")

answer = len(data)

# submission

submit(answer, part=part, day=day, year=year)
