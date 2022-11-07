# API stuff

from re import M
from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

message = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

message = [m.split(": ") for m in message.split("\n")]
message = {m[0] : int(m[1]) for m in message}

lines = data.split("\n")
sues = []

for line in lines:
    line = [l[1:] for l in line.replace(":", ",").split(",")[1:]]
    line = {line[i] : int(line[i + 1]) for i in range(0, len(line), 2)}
    sues.append(line)

for i, sue in enumerate(sues):
    for key in sue:
        if key in ["cats", "trees"]:
            if sue[key] <= message[key]:
                break
        elif key in ["pomeranians", "goldfish"]:
            if sue[key] >= message[key]:
                break
        elif sue[key] != message[key]:
            break
    else:
        answer = i + 1
        break

# submission

submit(answer, part=part, day=day, year=year)
