# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

def solve(data):
    data = [(list(d)[0], int("".join(list(d)[1:]))) for d in data.split(", ")]
    facing, x, y = 0, 0, 0
    visited = set((x, y))

    for d in data:
        facing = (facing + 4 + (1 if d[0] == "R" else -1)) % 4
        new_x, new_y = x, y

        if facing == 0:
            new_y += d[1]
        elif facing == 1:
            new_x += d[1]
        elif facing == 2:
            new_y -= d[1]
        elif facing == 3:
            new_x -= d[1]

        if x == new_x:
            yrange = range(y + 1, new_y + 1) if y <= new_y else range(new_y, y)

            for i in yrange:
                if (new_x, i) in visited:
                    return abs(new_x) + abs(i)

                visited |= {(new_x, i)}

        elif y == new_y:
            xrange = range(x + 1, new_x + 1) if x <= new_x else range(new_x, x)

            for i in xrange:
                if (i, new_y) in visited:
                    return abs(i) + abs(new_y)

                visited |= {(i, new_y)}

        x, y = new_x, new_y

answer = solve(data)

# submission

submit(answer, part=part, day=day, year=year)
