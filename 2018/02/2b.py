# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = data.split("\n")

def findBoxes():
    for i, a in enumerate(data):
        for b in data[i:]:
            count = 0

            for idx, letter in enumerate(b):
                if a[idx] != letter:
                    count += 1

            if count == 1:
                return "".join([letter for i, letter in enumerate(a) if b[i] == letter])

answer = findBoxes()

# submission

submit(answer, part=part, day=day, year=year)
