# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = data.replace("#", "1").replace(".", "0").split("\n")
size = len(data[0])
data = [[0] + [int(n) for n in line] + [0] for line in data]
data.insert(0, (size + 2) * [0])
data.append((size + 2) * [0])

for _ in range(100):
    update = [row[:] for row in data]

    for row in range(1, len(data) - 1):
        for col in range(1, len(data) - 1):
            neighbors = -data[row][col]

            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbors += data[row + i][col + j]

            if data[row][col] == 1:
                if neighbors not in [2, 3]:
                    update[row][col] = 0
            else:
                if neighbors == 3:
                    update[row][col] = 1

    data = [row[:] for row in update]

answer = sum([sum(row) for row in data])

# submission

submit(answer, part=part, day=day, year=year)
