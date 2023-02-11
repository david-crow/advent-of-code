# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import defaultdict
from copy import deepcopy

def run(instructions, size):
    visited = defaultdict(int)
    acc, ptr = 0, 0

    while True:
        if visited[ptr] or ptr >= size:
            break

        else:
            visited[ptr] = True

            match instructions[ptr][0]:
                case "acc":
                    acc += instructions[ptr][1]
                    ptr += 1
                case "jmp":
                    ptr += instructions[ptr][1]
                case "nop":
                    ptr += 1

    return acc, ptr >= size

data = [d.split(" ") for d in data.splitlines()]
data = [[a, int(b)] for a, b in data]
candidates = [i for i, d in enumerate(data) if d[0] != "acc"]
size = len(data)

for c in candidates:
    new_data = deepcopy(data)
    new_data[c][0] = "nop" if data[c][0] == "jmp" else "jmp"
    acc, terminated = run(new_data, size)

    if terminated:
        answer = acc
        break

# submission

submit(answer, part=part, day=day, year=year)
