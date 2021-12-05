# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
year, day = int(__file__.split("/")[-3]), int(__file__.split("/")[-2])
data = get_data(day=day, year=year)

# solution

lines = data.replace(",", " ").replace("-> ", "").split("\n")
lines = [list(map(int, line.split())) for line in lines]
diameter = max(max(line) for line in lines) + 1
diagram = [[0] * diameter for _ in range(diameter)]

for line in lines:
    if line[0] == line[2]: # vertical
        diagram[line[0]][line[3]] += 1

        for i in range(line[1], line[3], 1 if line[1] < line[3] else -1):
            diagram[line[0]][i] += 1

    elif line[1] == line[3]: # horizontal
        diagram[line[2]][line[1]] += 1
        
        for i in range(line[0], line[2], 1 if line[0] < line[2] else -1):
            diagram[i][line[1]] += 1

answer = sum([1 if n >= 2 else 0 for line in diagram for n in line])

# submission

submit(answer, part=part, day=day, year=year)
