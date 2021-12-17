# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [d.split() for d in data.split("\n")]
data = [(d[0], int(d[3]), int(d[6]), int(d[13])) for d in data]
limit = 2503

distances = [0 for _ in data]
points = [0 for _ in data]
moving = [d[2] for d in data]

for _ in range(limit):
    for i, d in enumerate(data):
        if moving[i] > 0:
            moving[i] -= 1
            distances[i] += d[1]

            if moving[i] == 0:
                moving[i] = -d[3]

        elif moving[i] < 0:
            moving[i] += 1

            if moving[i] == 0:
                moving[i] = d[2]

    best = max(distances)

    for i in range(len(points)):
        points[i] += 1 if distances[i] == best else 0

answer = max(points)

# submission

submit(answer, part=part, day=day, year=year)
