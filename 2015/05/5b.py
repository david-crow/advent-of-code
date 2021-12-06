# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

def isNice(s):
    repeats = False
    pair_repeats = False

    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            repeats = True
            break

    for i in range(len(s) - 3):
        pair = s[i : i + 2]

        if pair in s[i + 2 :]:
            pair_repeats = True
            break

    return repeats and pair_repeats

answer = len([s for s in data.split() if isNice(s)])

# submission

# print(answer)
submit(answer, part=part, day=day, year=year)
