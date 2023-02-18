# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)
lines = data.splitlines()

# solution

import numpy as np

def identify_color(stack):
    for pixel in stack:
        if pixel != "2":
            return pixel

x, y = 25, 6
layers = np.array([list(data[i : i + x * y]) for i in range(0, len(data), x * y)])
layers = np.apply_along_axis(identify_color, 0, layers).reshape((y, x))

for row in layers:
    print("".join(row).replace("1", "#").replace("0", " "))

answer = "EBZUR"

# submission

submit(answer, part=part, day=day, year=year)
