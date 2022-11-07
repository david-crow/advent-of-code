# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import re

def findABAs(s):
    abas = []

    for i in range(len(s) - 2):
        check = s[i : i + 3]

        if check[0] == check[-1] and check[0] != check[1]:
            abas.append(check)

    return abas

def supportsSSL(s):
    abas = set()

    # outside brackets
    for chunk in s[0::2]:
        abas.update(findABAs(chunk))

    babs = [aba[1] + aba[0] + aba[1] for aba in abas]

    if len(babs) == 0:
        return False

    # inside brackets
    for chunk in s[1::2]:
        if any(bab in chunk for bab in babs):
            return True

    return False

answer = sum([1 if supportsSSL(re.split("\[|\]", d)) else 0 for d in data.split()])

# submission

submit(answer, part=part, day=day, year=year)
