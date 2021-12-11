# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [[-1e10] * 12] + [[-1e10] + list(map(int, line)) + [-1e10] for line in data.split("\n")] + [[-1e10] * 12]
answer = 0

def neighbors(i, j):
    return [(i + 1, j + 1), (i - 1, j - 1), 
            (i + 1, j - 1), (i - 1, j + 1), 
            (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

def flash(i, j):
    data[i][j] = 0

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if data[i + di][j + dj] != 0:
                data[i + di][j + dj] += 1

for _ in range(100):
    for i in range(1, 11):
        for j in range(1, 11):
            data[i][j] += 1

    flashing = True

    while flashing:
        flashing = False

        for i in range(1, 11):
            for j in range(1, 11):
                if data[i][j] > 9 and data[i][j] != 0:
                    flash(i, j)
                    flashing = True
                    answer += 1

# submission

submit(answer, part=part, day=day, year=year)
