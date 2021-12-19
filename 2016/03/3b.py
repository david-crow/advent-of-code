# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [list(map(int, d.split())) for d in data.split("\n")]
triangles = []

for i in range(0, len(data), 3):
    triangles.append([data[i][0], data[i + 1][0], data[i + 2][0]])
    triangles.append([data[i][1], data[i + 1][1], data[i + 2][1]])
    triangles.append([data[i][2], data[i + 1][2], data[i + 2][2]])

answer = sum(1 if (d[0] + d[1] > d[2] and d[0] + d[2] > d[1] and d[1] + d[2] > d[0]) else 0 for d in triangles)

# submission

print(answer)
submit(answer, part=part, day=day, year=year)
