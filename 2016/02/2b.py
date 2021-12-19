# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

keypad = [
    ["-", "-", "1", "-", "-"], 
    ["-", "2", "3", "4", "-"], 
    ["5", "6", "7", "8", "9"], 
    ["-", "A", "B", "C", "-"], 
    ["-", "-", "D", "-", "-"]]

x, y = 0, 2
answer = ""

for line in data.split():
    for c in line:
        if c == "L":
            x = x - 1 if x - 1 >= 0 and keypad[y][x - 1] != "-" else x
        elif c == "R":
            x = x + 1 if x + 1 < 5 and keypad[y][x + 1] != "-" else x
        elif c == "U":
            y = y - 1 if y - 1 >= 0 and keypad[y - 1][x] != "-" else y
        elif c == "D":
            y = y + 1 if y + 1 < 5 and keypad[y + 1][x] != "-" else y

    answer += keypad[y][x]

# submission

submit(answer, part=part, day=day, year=year)
