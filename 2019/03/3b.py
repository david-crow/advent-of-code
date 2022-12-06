# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = (
    [(d[0], int(d[1:])) for d in lines[0].split(",")],
    [(d[0], int(d[1:])) for d in lines[1].split(",")]
)

directions = {
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
    "R": [1, 0]
}

def calcPoints(wire): 
    loc = (0, 0)
    step = 0
    points = {}

    for dir, steps in wire:
        for _ in range(steps):
            dx, dy = directions[dir]
            loc = (loc[0] + dx, loc[1] + dy)
            step += 1

            if loc not in points:
                points[loc] = step

    return points

points = (
    calcPoints(data[0]),
    calcPoints(data[1])
)

intersections = [p for p in points[0] if p in points[1]]
answer = min(points[0][loc] + points[1][loc] for loc in intersections)

# submission

submit(answer, part=part, day=day, year=year)
