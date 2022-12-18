# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = data.split("\n\n")

def isValid(d):
    d = {x.split(":")[0] : x.split(":")[1] for x in d.split()}

    if not all(f in d for f in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
        return False

    for k, v in d.items():
        if k == "cid":
            continue
        elif k == "byr" and int(v) in range(1920, 2003):
            continue
        elif k == "iyr" and int(v) in range(2010, 2021):
            continue
        elif k == "eyr" and int(v) in range(2020, 2031):
            continue
        elif k == "hgt":
            if "cm" in v and int(v[:-2]) in range(150, 194):
                continue
            elif "in" in v and int(v[:-2]) in range(59, 77):
                continue
        elif k == "hcl" and v[0] == "#" and len(v) == 7 and all(c in list("0123456789abcdef") for c in v[1:]):
            continue
        elif k == "ecl" and v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue
        elif k == "pid" and len(v) == 9 and int(v):
            continue

        return False

    return True

answer = len([d for d in data if isValid(d)])

# submission

submit(answer, part=part, day=day, year=year)
