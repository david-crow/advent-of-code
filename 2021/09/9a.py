# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = ["9" + d + "9" for d in data.split("\n")]
width = len(data[0])

data.insert(0, "9" * width)
data.append("9" * width)
answer = 0

for i in range(1, width - 1):
    for j in range(1, width - 1):
        adjacents = [data[i - 1][j], data[i + 1][j], data[i][j - 1], data[i][j + 1]]

        if all(data[i][j] < adj for adj in adjacents):
            answer += int(data[i][j]) + 1

# submission

submit(answer, part=part, day=day, year=year)
