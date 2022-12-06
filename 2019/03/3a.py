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
    x, y = 0, 0
    points = set()

    for dir, steps in wire:
        for _ in range(steps):
            dx, dy = directions[dir]
            x, y = x + dx, y + dy
            points.add((x, y))

    return points

points = (
    calcPoints(data[0]),
    calcPoints(data[1])
)

intersections = [p for p in points[0] if p in points[1]]
answer = min(abs(x) + abs(y) for x, y in intersections)

# submission

submit(answer, part=part, day=day, year=year)
