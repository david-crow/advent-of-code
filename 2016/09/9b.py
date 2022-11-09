# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

def decompress(data):
    i, total = 0, 0

    while i < len(data):
        if data[i] == "(":
            i += 1
            marker = ""

            while data[i] != ")":
                marker += data[i]
                i += 1

            marker = [int(n) for n in marker.split("x")]
            total += marker[1] * decompress(data[i + 1 : i + 1 + marker[0]])
            i += marker[0]

        else:
            total += 1

        i += 1

    return total

answer = decompress(data)

# submission

submit(answer, part=part, day=day, year=year)
