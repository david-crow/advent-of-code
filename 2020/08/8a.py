# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import defaultdict


def run(instructions):
    visited = defaultdict(int)
    acc, ptr = 0, 0

    while True:
        if visited[ptr]:
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

    return acc

data = [d.split(" ") for d in data.splitlines()]
data = [[a, int(b)] for a, b in data]
answer = run(data)

# submission

submit(answer, part=part, day=day, year=year)
