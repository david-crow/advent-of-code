# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = list(map(int, data.split(",")))
data[1] = 12
data[2] = 2

for i in range(0, len(data), 4):
    match data[i]:
        case 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
        case 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
        case 99:
            break

answer = data[0]

# submission

submit(answer, part=part, day=day, year=year)
