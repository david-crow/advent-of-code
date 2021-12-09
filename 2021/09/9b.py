# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import math

data = ["9" + d + "9" for d in data.split("\n")]
width = len(data[0])

data.insert(0, "9" * width)
data.append("9" * width)

visited = [[False] * width for _ in range(width)]
sizes = []

for i in range(1, width - 1):
    for j in range(1, width - 1):
        if data[i][j] != "9" and not visited[i][j]:
            visited[i][j] = True
            q = [(i, j)]
            size = 1

            while q:
                s = q.pop(0)
                x, y = s[0], s[1]

                for n in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if data[n[0]][n[1]] != "9" and not visited[n[0]][n[1]]:
                        visited[n[0]][n[1]] = True
                        q.append((n[0], n[1]))
                        size += 1

            sizes.append(size)

answer = math.prod(sorted(sizes, reverse=True)[:3])

# submission

submit(answer, part=part, day=day, year=year)
