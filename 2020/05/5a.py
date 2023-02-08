# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

def getID(ticket):
    row = (0, 127)
    col = (0, 7)

    for r in ticket[:7]:
        update = sum(row) // 2
        row = (row[0], update) if r == "F" else (update + 1, row[1])

    for c in ticket[7:]:
        update = sum(col) // 2
        col = (col[0], update) if c == "L" else (update + 1, col[1])

    return 8 * row[0] + col[0]

answer = max([getID(ticket) for ticket in data.splitlines()])

# submission

submit(answer, part=part, day=day, year=year)
