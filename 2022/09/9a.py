# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

def updateHead():
    hx = hy = 0

    for line in lines:
        direction, distance = line.split()

        for _ in range(int(distance)):
            hx += (direction == "R") - (direction == "L")
            hy += (direction == "U") - (direction == "D")

            yield hx, hy

def updateTail(head):
    tx = ty = 0

    for hx, hy in head:
        if abs(hx - tx) > 1 or abs(hy - ty) > 1:
            ty += (hy > ty) - (hy < ty)
            tx += (hx > tx) - (hx < tx)

        yield tx, ty

answer = len(set(updateTail(updateHead())))

# submission

submit(answer, part=part, day=day, year=year)
