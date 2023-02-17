# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import defaultdict

def int_if_num(s):
    try:
        return int(s)
    except ValueError as _:
        return s

data = [list(map(int_if_num, d.split())) for d in data.splitlines()]
reg = {"a": 0, "b": 0, "c": 0, "d": 0}
i = 0

while i < len(data):
    val = data[i][1] if type(data[i][1]) == int else reg[data[i][1]]

    if data[i][0] == "jnz":
        i += data[i][2] if val else 1
    else:
        if data[i][0] == "cpy":
            reg[data[i][2]] = val
        elif data[i][0] == "inc":
            reg[data[i][1]] += 1
        else: # data[i][0] == "dec"
            reg[data[i][1]] -= 1

        i += 1

answer = reg["a"]

# submission

submit(answer, part=part, day=day, year=year)
