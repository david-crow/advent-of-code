# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import math

sug = [3, 0, 0, -3, 2]
spr = [-3, 3, 0, 0, 9]
can = [-1, 0, 4, 0, 1]
cho = [0, 0, -2, 2, 9]

answer = 0

for a in range(101):
    for b in range(101 - a):
        for c in range(101 - a - b):
            d = 100 - a - b - c

            cap = max(0, a * sug[0] + b * spr[0] + c * can[0] + d * cho[0])
            dur = max(0, a * sug[1] + b * spr[1] + c * can[1] + d * cho[1])
            fla = max(0, a * sug[2] + b * spr[2] + c * can[2] + d * cho[2])
            tex = max(0, a * sug[3] + b * spr[3] + c * can[3] + d * cho[3])

            score = cap * dur * fla * tex
            answer = max(answer, score)

# submission

submit(answer, part=part, day=day, year=year)
