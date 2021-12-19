# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
x, y = 1, 1

answer = ""

for line in data.split():
    for c in line:
        if c == "L":
            x = max(0, x - 1)
        elif c == "R":
            x = min(2, x + 1)
        elif c == "U":
            y = max(0, y - 1)
        elif c == "D":
            y = min(2, y + 1)

    answer += keypad[y][x]

# submission

submit(answer, part=part, day=day, year=year)
