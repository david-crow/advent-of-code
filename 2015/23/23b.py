# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [d.split() for d in data.replace(",", "").splitlines()]
reg = {"a": 1, "b": 0}
i = 0

while i < len(data):
    d = data[i]

    match d[0]:
        case "hlf":
            reg[d[1]] //= 2
        case "tpl":
            reg[d[1]] *= 3
        case "inc":
            reg[d[1]] += 1
        case "jmp":
            i += int(d[1])
            continue
        case "jie":
            if reg[d[1]] % 2 == 0:
                i += int(d[2])
                continue
        case "jio":
            if reg[d[1]] == 1:
                i += int(d[2])
                continue

    i += 1

answer = reg["b"]

# submission

submit(answer, part=part, day=day, year=year)
