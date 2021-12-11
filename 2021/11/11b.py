# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

big = int(1e10)
data = [[-big] * 12] + [[-big] + list(map(int, line)) + [-big] for line in data.split("\n")] + [[-big] * 12]

def check_flashed(data):
    return not any(any(line[1 : -1]) for line in data[1 : -1])

def flash(i, j):
    data[i][j] = 0

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if data[i + di][j + dj] != 0:
                data[i + di][j + dj] += 1

for step in range(big):
    flashing = True

    for i in range(1, 11):
        for j in range(1, 11):
            data[i][j] += 1

    while flashing:
        flashing = False

        for i in range(1, 11):
            for j in range(1, 11):
                if data[i][j] > 9 and data[i][j] != 0:
                    flash(i, j)
                    flashing = True

    if check_flashed(data):
        answer = step + 1
        break

# submission

submit(answer, part=part, day=day, year=year)
