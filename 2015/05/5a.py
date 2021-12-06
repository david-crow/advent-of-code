# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

def isNice(s):
    repeats = False
    vowel_count = 0

    if any(n in s for n in ["ab", "cd", "pq", "xy"]):
        return False

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats = True
            break

    for c in s:
        if c in "aeiou":
            vowel_count += 1

        if vowel_count > 2:
            break

    return repeats and vowel_count > 2

answer = len([s for s in data.split() if isNice(s)])

# submission

submit(answer, part=part, day=day, year=year)
