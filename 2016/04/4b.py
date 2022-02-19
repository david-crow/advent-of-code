# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import defaultdict, Counter

counts = defaultdict(list)
rooms = []
answer = 0

data = [d.split("-") for d in data.split("\n")]
data = [["-".join(d[:-1]), int(d[-1][:-7]), d[-1][-6:-1]] for d in data]

def isLetter(c):
    return 97 <= c and c <= 122

for room in data:
    code = [ord(c) + room[1] % 26 for c in room[0]]
    code = [c - 26 if c >= 122 else c for c in code]
    code = [chr(c) if isLetter(c) else " " for c in code]
    room[0] = "".join(code)

    if "northpole" in room[0]:
        answer = room[1]
        break

# submission

submit(answer, part=part, day=day, year=year)
