# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [d.strip(",").split("=") for d in data.split()]
xlim, ylim = [int(d) for d in data[2][1].split("..")], [int(d) for d in data[3][1].split("..")]

valid = set()

for start_x in range(xlim[1] + 1):
    for start_y in range(ylim[0], abs(ylim[0]) + 1):
        vx, vy = start_x, start_y
        x, y = 0, 0

        while x <= xlim[1] and ylim[0] <= y:
            if x in range(xlim[0], xlim[1] + 1) and y in range(ylim[0], ylim[1] + 1):
                valid |= {(start_x, start_y)}

            x += vx
            y += vy
            vx -= 1 if vx > 0 else 0
            vy -= 1

answer = len(valid)

# submission

submit(answer, part=part, day=day, year=year)
