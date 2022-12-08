# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [list(map(int, list(d))) for d in lines]
size = len(data)

def isVisible(x, y):
    return any([all(data[y][x] > data[i][x] for i in range(y)),
                all(data[y][x] > data[y][i] for i in range(x)),
                all(data[y][x] > data[i][x] for i in range(y + 1, size)),
                all(data[y][x] > data[y][i] for i in range(x + 1, size))])

answer = len([(i, j) for j in range(size) for i in range(size) if isVisible(i, j)])

# submission

submit(answer, part=part, day=day, year=year)
