# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

code, data = data.split("\n\n")
code = "".join(code.split())
data = [list("." + d + ".") for d in data.split("\n")]

h, w = len(data) + 2, len(data[0])
data.insert(0, ["."] * w)
data.append(["."] * w)

for step in range(50):
    temp = [d[:] for d in data]
    fill = "." if code[0] == "." or step % 2 == 0 else "#"
    next_fill = "." if code[0] == "." or step % 2 == 1 else "#"

    for y in range(h):
        for x in range(w):
            idx = ""

            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if x + j in range(w) and y + i in range(h):
                        idx += data[y + i][x + j]
                    else:
                        idx += fill

            idx = idx.replace(".", "0").replace("#", "1")
            temp[y][x] = code[int(idx, 2)]

    data = [list(next_fill + "".join(t[:]) + next_fill) for t in temp]
    h, w = h + 2, w + 2
    data.insert(0, [next_fill] * w)
    data.append([next_fill] * w)

data = ["".join(d) for d in data]
answer = sum(d.count("#") for d in data)

# submission

submit(answer, part=part, day=day, year=year)
