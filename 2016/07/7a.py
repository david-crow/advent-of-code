# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import re

def hasABBA(s):
    for i in range(len(s) - 3):
        check = s[i : i + 4]

        if check[:2] == check[2:][::-1] and check[0] != check[1]:
            return True

    return False

def supportsTLS(s):
    # inside brackets
    for sub in s[1::2]:
        if hasABBA(sub):
            return False

    # outside brackets
    for sub in s[0::2]:
        if hasABBA(sub):
            return True
    
    return False

answer = sum([1 if supportsTLS(re.split("\[|\]", d)) else 0 for d in data.split()])

# submission

submit(answer, part=part, day=day, year=year)
